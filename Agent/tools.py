# D:\Python\Multiverse\Agent\tools.py

import datetime
import pytz
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool 
from Backend.config import TAVILY_API_KEY

def get_tavily_search_tool():
    if not TAVILY_API_KEY:
        raise ValueError(
            "TAVILY_API_KEY is not set. "
            "Please ensure it's defined in your .env.local file "
            "and loaded via D:\\Python\\Multiverse\\Backend\\config.py."
        )
    return TavilySearchResults(max_results=5, tavily_api_key=TAVILY_API_KEY)

# New Math Tools
@tool
def add(a: float, b: float) -> float:
    """Adds two numbers, a and b. Returns their sum.
    Example: add(5, 3) returns 8.0
    """
    return a + b

@tool
def subtract(a: float, b: float) -> float:
    """Subtracts number b from number a. Returns the difference.
    Example: subtract(10, 4) returns 6.0
    """
    return a - b

@tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers, a and b. Returns their product.
    Example: multiply(2, 6) returns 12.0
    """
    return a * b

@tool
def divide(a: float, b: float) -> float:
    """Divides number a by number b. Returns the quotient.
    Raises ValueError if b is zero.
    Example: divide(10, 2) returns 5.0
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
