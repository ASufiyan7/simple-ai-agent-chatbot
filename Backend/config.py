# D:\Python\Multiverse\Backend\config.py

import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env.local')

print(f"DEBUG: Attempting to load .env.local from: {dotenv_path}")
load_dotenv(dotenv_path=dotenv_path)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

print(f"DEBUG: GROQ_API_KEY loaded: {GROQ_API_KEY is not None}")
if GROQ_API_KEY:
    print(f"DEBUG: GROQ_API_KEY value (first 5 chars): {GROQ_API_KEY[:5]}...")
else:
    print("DEBUG: GROQ_API_KEY is None.")

print(f"DEBUG: TAVILY_API_KEY loaded: {TAVILY_API_KEY is not None}")
if TAVILY_API_KEY:
    print(f"DEBUG: TAVILY_API_KEY value (first 5 chars): {TAVILY_API_KEY[:5]}...")
else:
    print("DEBUG: TAVILY_API_KEY is None.")


if not GROQ_API_KEY:
    print("WARNING: GROQ_API_KEY is not set in .env.local or environment variables.")
if not TAVILY_API_KEY:
    print("WARNING: TAVILY_API_KEY is not set in .env.local or environment variables.")