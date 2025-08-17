from  src.langgrapgagenticai.state.state import State

class Chatbot_with_tools_node:
    """
    Chatbot logic enhanced with tool integration"""
    
    def __init__(self, model):
        self.llm = model

    def create_chatbot(self, tools):
        """
        Returns a chatbot node function"""

        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State)-> dict:
            """chatbot logic for processing the input state and returning the response"""

            return {"messages": [llm_with_tools.invoke(state["messages"])]}
        
        return chatbot_node