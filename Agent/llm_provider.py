# D:\Python\Multiverse\Agent\llm_provider.py

from langchain_groq import ChatGroq
from Backend.config import GROQ_API_KEY # Corrected import to reflect config's location

def get_llm(model_name: str):
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is not set. Please ensure it's loaded via Backend/config.py.")
    
    return ChatGroq(
            model=model_name,
            api_key=GROQ_API_KEY,
        )