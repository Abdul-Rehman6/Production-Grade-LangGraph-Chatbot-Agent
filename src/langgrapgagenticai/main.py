import streamlit as st
from src.langgrapgagenticai.ui.streamlitui.loadui import LoadStreamlitUI

class load_langgrapg_agenticai_app:
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model, sets up the graph based on the selected use case, and displays the output while implementing exception handling.
    """
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("ERROR: Failed to load user input from UI")

    user_message = st.chat_input("Enter your message: ")

