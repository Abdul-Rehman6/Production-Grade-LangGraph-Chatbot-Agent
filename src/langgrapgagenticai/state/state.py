from typing import Annotated, List, TypedDict
from langgraph.graph.message import add_messages


class State(TypedDict):
    """
    Represent the structure of the state used in graph
    """
    messages: Annotated[List, add_messages]
    news_data: str
    summary: str
    filename: str        