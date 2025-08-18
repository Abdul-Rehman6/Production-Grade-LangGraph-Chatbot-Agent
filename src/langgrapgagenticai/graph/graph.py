from langgraph.graph import StateGraph, START, END
from src.langgrapgagenticai.state.state import State
from src.langgrapgagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgrapgagenticai.tools.search_tool import get_tools, create_tool_node
from langgraph.prebuilt import ToolNode, tools_condition
from src.langgrapgagenticai.nodes.chatbot_with_tool_node import Chatbot_with_tools_node
from src.langgrapgagenticai.nodes.ai_news_node import AiNewsNode

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)


    def basic_chatbot_build_graph(self):
        """
            Builds a basic chatbot graph using LangGraph.
            This yethod initializes a chatbot node using the 'BasicChatbotNode class and integrates it into the graph. The chatbot node is set as both the entry and exit point of the graph.
        """

        self.basic_chatbot_node = BasicChatbotNode(self.llm)

        # Chatbot Node
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)

        # Edges of Graph
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
        

    def chatbot_with_tools_build_graph(self):
        """
            Builds an advanced chatbot graph with tool integration.
            This method creates a chatbot graph that includes both a chatbot node and a tool node. It defines tools, initializes the chatbot with tool capabilities, and sets up conditional and direct edges between nodes. The chatbot node is set as the entry point.
            """
        
        # tools and tool node 
        tools = get_tools()
        tool_node = create_tool_node(tools = tools)

        # defining LLM 
        llm = self.llm

        # defining the chatbot node
        chatbot_with_tools_obj = Chatbot_with_tools_node(model = llm)
        chatbot_node = chatbot_with_tools_obj.create_chatbot(tools = tools)


        # nodes and edges of graph
        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)

        # edges
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")        
        self.graph_builder.add_edge("chatbot", END)


    def ai_news_builder_graph(self):
        

        ai_news_node = AiNewsNode(self.llm)
        print("in the  ai_news_builder_graph")

        # nodes
        self.graph_builder.add_node("fetch_news",ai_news_node.fetch_news)
        self.graph_builder.add_node("summarize_news",ai_news_node.summarize_news)
        self.graph_builder.add_node("save_result",ai_news_node.save_result)

        print("in the  ai_news_builder_graph after nodes")

        # edges
        self.graph_builder.add_edge(START, "fetch_news")     # replacement of .add_edge(START, "fetch_news")
        self.graph_builder.add_edge("fetch_news", "summarize_news")
        self.graph_builder.add_edge("summarize_news", "save_result")
        self.graph_builder.add_edge("save_result", END)

        print("in the  ai_news_builder_graph after edges")


    def setup_graph(self, usecase):
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        if usecase == "Chatbot with Web Tool":
            self.chatbot_with_tools_build_graph()
        if usecase == "Ai News":
            self.ai_news_builder_graph()

        return self.graph_builder.compile()