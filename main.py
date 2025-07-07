# Importing the necessary libraries
import asyncio
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient
import os


async def ai_assistant():
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


    while True:
        # Taking user input
        user_input = input("\n Your Query: ")

        # checking for exiting
        if user_input.lower() in ['exit','quit']:
            print('Ending Conversation!')
            break

        # Agent Response
        agent_response = await agent.run(user_input)
        print("\n AI Assistant Response: ",agent_response)


# Calling the ai_assistant function
asyncio.run(ai_assistant())