# 🤖 Agentic AI Chatbot with LangGraph

A powerful, multi-functional AI chatbot application built with LangGraph and Streamlit that demonstrates various agentic AI capabilities including basic conversation, web-enabled search, and automated AI news aggregation

## ✨ Features

### 🎯 Three Core Use Cases

1. **Basic Chatbot** 
   - Simple conversational AI interface
   - Direct interaction with OpenAI models
   - Clean, straightforward Q&A experience

2. **Chatbot with Web Tool**
   - Enhanced chatbot with real-time web search capabilities
   - Powered by Tavily Search API
   - Provides up-to-date information beyond training data
   - Automatic tool invocation when needed

3. **AI News Explorer** 📰
   - Automated fetching of latest AI news from Pakistan and globally
   - Intelligent summarization using LLM
   - Time-based filtering (Daily, Weekly, Monthly)
   - Automatic markdown report generation
   - Saves summaries for future reference

## 🏗️ Architecture

### Project Structure

```
├── app.py                          # Application entry point
├── README.md                       # Project documentation
├── .gitignore                      # Git ignore rules
├── AINews/                         # Generated news summaries
│   ├── daily_summary.md
│   ├── weekly_summary.md
│   └── monthly_summary.md
└── src/
    └── langgrapgagenticai/
        ├── __init__.py
        ├── main.py                 # Main application logic
        ├── LLMS/                   # LLM configurations
        │   ├── __init__.py
        │   └── openai.py           # OpenAI integration
        ├── graph/                  # LangGraph definitions
        │   ├── __init__.py
        │   └── graph.py            # Graph builder & workflows
        ├── nodes/                  # Graph node implementations
        │   ├── __init__.py
        │   ├── basic_chatbot_node.py
        │   ├── chatbot_with_tool_node.py
        │   └── ai_news_node.py
        ├── state/                  # State management
        │   ├── __init__.py
        │   └── state.py            # State definitions
        ├── tools/                  # External tools
        │   ├── __init__.py
        │   └── search_tool.py      # Tavily search integration
        └── ui/                     # User interface
            ├── __init__.py
            ├── uiconfigfile.py
            ├── uiconfigfile.ini
            └── streamlitui/
                ├── loadui.py       # UI loader
                └── display_result.py  # Result renderer
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API Key ([Get one here](https://platform.openai.com/api-keys))
- Tavily API Key ([Get one here](https://app.tavily.com/home)) - Required for web search and AI news features

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd <repository-name>
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Required packages:
   - `streamlit`
   - `langchain`
   - `langchain-openai`
   - `langchain-tavily`
   - `langgraph`
   - `tavily-python`

4. **Set up environment variables (Optional)**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## 📖 Usage Guide

### Basic Setup

1. **Select LLM Provider**: Choose "OPEN AI" from the sidebar
2. **Select Model**: Pick from available OpenAI models (gpt-4o, gpt-4o-mini, etc.)
3. **Enter API Key**: Provide your OpenAI API key
4. **Choose Use Case**: Select your desired functionality

### Use Case: Basic Chatbot

Simply type your message in the chat input and receive AI responses. Perfect for:
- General questions
- Creative writing
- Problem-solving
- Casual conversation

### Use Case: Chatbot with Web Tool

The chatbot automatically searches the web when needed. Great for:
- Current events and news
- Real-time data queries
- Fact-checking
- Research assistance

**Note**: Requires Tavily API key

### Use Case: AI News Explorer

1. Enter your Tavily API key
2. Select time frame (Daily, Weekly, or Monthly)
3. Click "🔍 Fetch Latest AI News"
4. View formatted news summary with:
   - Date-organized entries
   - Concise summaries
   - Source links
   - Saved markdown files in `/AINews` directory

## 🛠️ Technical Details

### LangGraph Workflows

#### Basic Chatbot Flow
```
START → chatbot → END
```

#### Web-Enabled Chatbot Flow
```
START → chatbot ⇄ tools → END
           ↓
    (conditional edge)
```

#### AI News Flow
```
START → fetch_news → summarize_news → save_result → END
```

### State Management

The application uses a typed state structure:
```python
class State(TypedDict):
    messages: Annotated[List, add_messages]
    news_data: str
    summary: str
    filename: str
```

### Node Implementations

- **BasicChatbotNode**: Simple message processing
- **Chatbot_with_tools_node**: Tool-enhanced responses
- **AiNewsNode**: Multi-step news aggregation pipeline

## 🎨 Customization

### Adding New Models

Edit `src/langgrapgagenticai/ui/uiconfigfile.ini`:
```ini
OPENAI_MODEL_OPTIONS = gpt-4o, gpt-4o-mini, your-new-model
```

### Adding New Use Cases

1. Create a new node in `src/langgrapgagenticai/nodes/`
2. Add graph logic in `graph.py`
3. Update UI options in `uiconfigfile.ini`
4. Add display logic in `display_result.py`

### Styling the UI

Modify Streamlit configuration in `loadui.py`:
```python
st.set_page_config(
    page_title="Your Title",
    layout="wide",
    initial_sidebar_state="expanded"
)
```

## 🔐 Security Notes

- API keys are handled securely through session state
- Passwords are masked in input fields
- `.env` file is gitignored
- No credentials are stored in code

## 📝 Generated Outputs

News summaries are saved in markdown format:
- **Location**: `./AINews/`
- **Naming**: `{frequency}_summary.md`
- **Format**: Structured markdown with dates, summaries, and source links

## 🐛 Troubleshooting

### Common Issues

**"Please enter OpenAI API Key"**
- Ensure your API key is valid and properly entered
- Check for extra spaces or line breaks

**"Graph setup failed"**
- Verify all required packages are installed
- Check for typos in use case selection

**"File not found" in AI News**
- Ensure the `AINews` directory exists
- Check write permissions for the directory

**Tavily API errors**
- Verify API key is active
- Check your API usage limits

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **LangGraph**: For the powerful graph-based AI framework
- **Streamlit**: For the intuitive UI framework
- **OpenAI**: For advanced language models
- **Tavily**: For web search capabilities

## 📧 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review LangGraph docs: [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)

---

**Built with ❤️ using LangGraph, Streamlit, and OpenAI**
