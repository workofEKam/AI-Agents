from agent.bot import setup_agent

def main():
    agent = setup_agent()
    
    # This list acts as our agent's memory.
    messages = []
    
    print("Weather Bot is online. (Type 'quit' to exit)")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'quit':
            break
            
        # 1. Add the user's message to memory
        messages.append({"role": "user", "content": user_input})
        
        # 2. Pass the entire conversation history to the agent
        response = agent.invoke({"messages": messages})
        
        # 3. The agent returns an updated list containing its tool calls, 
        # the tool results, and its final text answer. 
        # We overwrite our memory with this complete updated history.
        messages = response["messages"]
        
        # 4. Print the very last message (the AI's final response to the user)
        bot_reply = messages[-1].content
        print(f"Bot: {bot_reply}")

if __name__ == "__main__":
    main()