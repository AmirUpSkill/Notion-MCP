import asyncio
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from mcp_use import MCPAgent, MCPClient

async def main():
    # --- Load env variables ---
    load_dotenv()

    # --- Initialize LLM ---
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", google_api_key=os.getenv("GEMINI_API"))

    # --- Create MCP Client from Config ---
    client = MCPClient.from_config_file("config/mcp_config.json")

    # --- Create Agent ---
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # ---  Test The Notion  MCP Server  ---
    result = await agent.run(
        "give me summary of the page title 'MCP Quick Start' ."
    )

    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())