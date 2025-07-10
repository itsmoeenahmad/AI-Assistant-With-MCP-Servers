# Importing the necessary libraries
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient
import os


# Main Function
async def ai_assistant(user_query):
    # Loading the environment variables
    load_dotenv()
    groq_api_key = os.getenv("GROQ_API_KEY")
    if groq_api_key is not None:
        os.environ["GROQ_API_KEY"] = groq_api_key

    # Config File - Where we define all the mcp_servers
    config_file = "mcp_servers.json"

    # Creating MCP Cliet
    mcp_client = MCPClient.from_config_file(config_file)

    # Defining LLM-Groq
    llm = ChatGroq(
        model='qwen-qwq-32b'
    )

    # Creating an Agent with memory enabled
    agent = MCPAgent(
        client = mcp_client,
        llm = llm,
        max_steps = 20,
        memory_enabled = True,
        verbose = True 
    )


    # Agent Response
    agent_response = await agent.run(user_query)
    return agent_response