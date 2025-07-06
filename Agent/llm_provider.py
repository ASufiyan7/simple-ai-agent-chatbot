from langchain_groq import ChatGroq
from app.config import GROQ_API_KEY

def get_llm(provider, model_name):
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is not set. Please set it in your environment variables.")
    
    return ChatGroq(
            model = model_name,
            api_key = GROQ_API_KEY,
        )