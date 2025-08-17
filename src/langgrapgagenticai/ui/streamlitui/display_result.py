import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import json

class DisplayresultStreamlit:
    def __init__(self, usecase, graph, user_input):
        self.usecase = usecase
        self.graph = graph
        self.user_input = user_input

    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_input = self.user_input

            # ---------------- Basic Chatbot ----------------
        if usecase == "Basic Chatbot":
            for event in graph.stream({"messages": user_input}):
                for value in event.values():
                    with st.chat_message("user"):
                        st.write(user_input)
                    with st.chat_message("assistant"):
                        st.write(value["messages"].content)

        # ---------------- Chatbot with Web Tool ----------------
        elif usecase == "Chatbot with Web Tool":
            # Always display user input first
            with st.chat_message("user"):
                st.write(user_input)

            for event in graph.stream({"messages": user_input}):
                for value in event.values():
                    for msg in value["messages"]:
                        if msg.type == "ai":
                            with st.chat_message("assistant"):
                                st.write(msg.content)

                        elif msg.type == "tool":
                            with st.chat_message("assistant"):
                                st.write(f"🔧 Tool `{msg.name}` returned:\n\n{msg.content}")

                
            
