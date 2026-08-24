import os
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
from langchain.agents import create_agent
# pyrefly: ignore [missing-import]
from langchain_groq import ChatGroq
from tools.weather import get_current_weather

load_dotenv()

def setup_agent():

    llm = ChatGroq(
        model="openai/gpt-oss-120b", 
        temperature=0
    )
    
    # 2. Create the agent and bind the tools to it
    agent = create_agent(
        model=llm,
        tools=[get_current_weather],
        system_prompt="You are a helpful weather assistant. Always ask the user for a city if they do not provide one."
    )
    
    return agent