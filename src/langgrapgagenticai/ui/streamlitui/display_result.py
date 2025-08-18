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
            
        elif usecase == "Ai News":
            frequency = self.user_input
            print("in the  Ai News usecase in displayui file frequency: ", frequency)
            with st.spinner("Fetching and summarizing news... ⏳"):
                result = graph.invoke({"messages": [HumanMessage(content=frequency)]})
                try:
                    # Read the markdown file
                    AI_NEWS_PATH = f"./AINews/{frequency.lower()}_summary.md"
                    with open(AI_NEWS_PATH, "r") as file:
                        markdown_content = file.read()

                    # Display the markdown content in    Streamlit
                    st.markdown(markdown_content, unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error(f"News Not Generated or File not found: {AI_NEWS_PATH}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                
            
