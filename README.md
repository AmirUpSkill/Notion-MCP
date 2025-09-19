

# Notion MCP Agent



A powerful Python-based AI agent that connects to your Notion workspace using the official Model Context Protocol (MCP). It leverages Google's state-of-the-art `gemini-2.5-pro` model via LangChain to understand natural language commands, search your Notion pages, and perform tasks like summarization.

This project serves as a perfect starting point for building more complex AI-powered applications that integrate deeply with Notion.

## ✨ Key Features

-   **Seamless Notion Integration**: Connects directly to Notion's official hosted MCP server.
-   **Natural Language Understanding**: Ask questions in plain English (e.g., "summarize my 'Project Phoenix' PRD").
-   **Powered by Gemini Pro**: Utilizes a powerful LLM for reasoning and task execution.
-   **Secure Authentication**: Handles Notion OAuth securely using the `mcp-remote` proxy tool.
-   **Extensible**: Easily add more tools and capabilities (e.g., creating pages, updating databases).
-   **Lightweight & Modern Stack**: Built with `mcp-use`, LangChain, and `uv` for a fast and clean development experience.

## ⚙️ Tech Stack

-   **Language**: Python 3.11+
-   **AI Frameworks**: LangChain, `mcp-use`
-   **LLM**: Google Gemini 2.5 Pro
-   **Package Manager**: `uv`
-   **Core Protocol**: Model Context Protocol (MCP)
-   **Authentication Helper**: `mcp-remote` (via npm/npx)

## 🚀 Getting Started

Follow these steps to get the Notion MCP Agent up and running on your local machine.

### Prerequisites

-   Python 3.11 or higher
-   Node.js and npm (for the `mcp-remote` authentication tool)
-   `uv` (a fast Python package installer):
    ```bash
    pip install uv
    ```
-   A Google Gemini API Key: Get yours from [Google AI Studio](https://aistudio.google.com/app/apikey).
-   A Notion Account.

### 1. Clone the Repository

```bash
git clone https://github.com/AmirUpSkill/Notion-MCP.git
cd Notion-MCP
```

### 2. Set Up the Environment

Create and activate a virtual environment using `uv`.

```bash
# Create the virtual environment
uv venv

# Activate it
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages from the `requirements.txt` file.

```bash
uv pip install -r requirements.txt
```

### 4. Configure Your API Key

Create a `.env` file in the root of the project to store your Gemini API key.

```bash
# Create the file (e.g., using 'touch' on macOS/Linux or 'echo.' on Windows)
touch .env
```

Open the `.env` file and add your key:

```
GEMINI_API="YOUR_GOOGLE_GEMINI_API_KEY_HERE"
```

The `config/mcp_config.json` file is already set up to use `mcp-remote` for Notion authentication. No changes are needed there.

## 🏃‍♀️ How to Run the Agent

### First-Time Run: Authentication

The very first time you run the script, `mcp-remote` will automatically open your web browser to the Notion authentication page.

1.  Log in to your Notion account.
2.  Select the workspace and pages you want to grant the agent access to.
3.  Click "**Allow access**".

After successful authorization, your credentials will be cached locally (in `~/.mcp-auth`), and you won't need to do this again unless the token expires or is revoked.

### Execute the Script

Run the main Python script from your terminal:

```bash
python notion_mcp.py
```

The agent will initialize, connect to Notion, and execute the predefined task in the script.


### Customizing the Task

To ask a different question, simply edit the prompt inside the `notion_mcp.py` file:

```python
# in notion_mcp.py
...
# --- Example: Search Notion for a PRD ---
result = await agent.run(
    "Find the page titled 'Q3 Marketing Plan' and tell me the key objectives."
)
...
```

## 🔧 How It Works

The agent uses the `mcp-use` library to manage connections to MCP servers.

1.  **Client Initialization**: The `MCPClient` reads `config/mcp_config.json`.
2.  **Local Proxy**: It finds the `notionMCP` server configuration and runs `npx mcp-remote` as a local subprocess.
3.  **Authentication**: `mcp-remote` handles the browser-based OAuth2 flow to get a secure access token from Notion.
4.  **Connection**: The local `mcp-remote` process now acts as an authenticated proxy, forwarding requests from our Python script to Notion's hosted MCP server (`https://mcp.notion.com/mcp`).
5.  **Agent Execution**: The `MCPAgent` combines the LLM's reasoning abilities with the tools provided by the Notion MCP server (like `search` and `fetch`) to execute your command.

## 💡 Troubleshooting

-   **401 Unauthorized Error**: This usually means the authentication failed.
    -   Make sure your browser is not blocking pop-ups.
    -   Clear the authentication cache and try again:
        -   **Windows**: `rmdir /s /q %USERPROFILE%\.mcp-auth`
        -   **macOS/Linux**: `rm -rf ~/.mcp-auth`
-   **Google API Quota Error**: If you see a `429 ResourceExhausted` error, you have exceeded the free tier limit for the Gemini API. You can either wait for the quota to reset or set up billing on your Google Cloud project for higher limits.

## 🗺️ Roadmap for a Full MVP

This project is the foundational client. The next steps to build a full-fledged "Notion AI Chat" application would be:

-   **Build a Chat Interface**: Create a web UI (e.g., using Streamlit, Gradio, or FastAPI with a React frontend).
-   **Implement More Tools**: Extend the agent to use other Notion tools like `create-page`, `update-page`, and `create-comment`.
-   **Dynamic Configuration**: Add a UI element to enable/disable the Notion connection.
-   **Improve Error Handling**: Provide user-friendly feedback for API errors or failed tool calls.

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.