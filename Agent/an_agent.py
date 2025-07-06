# D:\Python\Multiverse\Agent\an_agent.py

from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from .llm_provider import get_llm
from .tools import (
    get_tavily_search_tool,
    add,      
    subtract, 
    multiply, 
    divide    
)

def get_response(llm_id: str, query_history: list, use_search: bool, system_prompt: str):
    llm = get_llm(llm_id)
    
    tools = []
    if use_search:
        tools.append(get_tavily_search_tool())
        
    tools.append(add)
    tools.append(subtract)
    tools.append(multiply)
    tools.append(divide)

    agent_executor = create_react_agent(
        model=llm,
        tools=tools
    )

    messages = [SystemMessage(content=system_prompt)]
    for i, message_content in enumerate(query_history):
        
        if i % 2 == 0:
            messages.append(HumanMessage(content=message_content))
        else:
            messages.append(AIMessage(content=message_content))

    state = {
        "messages": messages
    }

    response = agent_executor.invoke(state)
    
    final_messages = response.get("messages", [])
    ai_message = [msg.content for msg in final_messages if isinstance(msg, AIMessage)]
    
    return ai_message[-1] if ai_message else "Sorry, I couldn't generate a response."