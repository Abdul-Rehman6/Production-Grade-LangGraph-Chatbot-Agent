from langgraph.graph import StateGraph, START, END
from src.langgrapgagenticai.state.state import State
from src.langgrapgagenticai.nodes.basic_chatbot_node import BasicChatbotNode

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
        

    def setup_graph(self, usecase):
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()

        return self.graph_builder.compile()