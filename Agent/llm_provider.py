# D:\Python\Multiverse\Agent\llm_provider.py

from langchain_groq import ChatGroq
from Backend.config import GROQ_API_KEY 

def get_llm(model_name: str):
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is not set.")
    
    return ChatGroq(
            model=model_name,
            api_key=GROQ_API_KEY,
        )