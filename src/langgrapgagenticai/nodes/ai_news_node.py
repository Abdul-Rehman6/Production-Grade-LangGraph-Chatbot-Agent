from tavily import TavilyClient
from src.langgrapgagenticai.state.state import State
from langchain_core.prompts import ChatPromptTemplate

class AiNewsNode:
    """
    Initilize the AiNewsNode with API key for Tavily and OPEN AI"""

    def __init__(self, model):
        self.llm = model
        self.tavily = TavilyClient()
        # this is used to capture various steps in this file so that later can be used for steps shown
        self.state = {}
        print("inside ainewsnode init")


    def fetch_news(self, state: State)-> State:
        """
        Fetch AI news based on the specified frequency.
        Args:
        state (dict): The state dictionary containing 'frequency'.
        Returns:
        dict: Updated state with 'news_data' key containing fetched news.
        """
        print("inside fetchnews")


        # in frontend i am doing this  ->> result = graph.invoke({"messages": frequency}) and getting here
        frequency = state['messages'][0].content.lower()    
        # self.state is defined in this paticulor function scope, its not the graph state
        self.state['frequency'] = frequency
        time_range_map = {'daily': 'd', 'weekly': 'w', 'monthly': 'm', 'year': 'y'}
        days_map = {'daily': 1, 'weekly': 7, 'monthly': 30, 'year': 366}

        response = self.tavily.search(
        query="Top Artificial Intelligence (AI) technology news in Pakistan and globally", 
        topic="news", 
        time_range=time_range_map[frequency], 
        include_answer="advanced", 
        max_results=20, 
        days=days_map[frequency],
        )

        state['news_data'] = response.get('results', [])
        self.state['news_data'] = state['news_data']
        # print("News Data node name fetch_news ", state['news_data'])
        return state
    

    def summarize_news(self, state: State)-> State:
        """
        Summarize the fetched news using an LLM.
        
        Args:
            state (dict): The state dictionary containing 'news_data'.
        
        Returns:
            dict: Updated state with 'summary' key containing the summarized news.
        """
        print("inside summarize_news")
        news_items = self.state['news_data']
        # print("News Data node name summarize_news ", news_items)
        prompt_template = ChatPromptTemplate.from_messages([
            ("system", """Summarize AI news articles into markdown format. For each item include:
            - Date in **YYYY-MM-DD** format in IST timezone
            - Concise sentences summary from latest news
            - Sort news by date wise (latest first)
            - Source URL as link
            Use format:
            ### [Date]
            - [Summary](URL)"""),
            ("user", "Articles:\n{articles}")
        ])

        articles_str = "\n\n".join([
            f"Content: {item.get('content', '')}\nURL: {item.get('url', '')}\nDate: {item.get('published_date', '')}"
            for item in news_items
        ])

        response = self.llm.invoke(prompt_template.format(articles=articles_str))
        state['summary'] = response.content
        self.state['summary'] = state['summary']
        return state
    
    def save_result(self,state: State)-> State:
        print("inside save_results")
        frequency = self.state['frequency']
        summary = self.state['summary']
        filename = f"./AINews/{frequency.lower()}_summary.md" # i can save this in pdf, csv or whatever i want.
        with open(filename, 'w') as f:
            f.write(f"# {frequency.capitalize()} AI News Summary\n\n")
            f.write(summary)
        self.state['filename'] = filename
        state['filename'] = filename
        return state



