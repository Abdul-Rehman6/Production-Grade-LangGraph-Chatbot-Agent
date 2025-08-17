from src.langgrapgagenticai.state.state import State

class BasicChatbotNode:
    """
    Basic Chatbot implementation"""

    def __init__(self, model):
        self.llm = model

    def process(self, state:State) -> dict:
        """
        Process the imput state and generates a chatbot response"""

        return {"messages": self.llm.invoke(state["messages"])}