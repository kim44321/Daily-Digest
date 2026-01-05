import os 
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv('NEWS_API_KEY')
WIKIPEDIA_API_KEY = os.getenv('WIKIPEDIA_API_KEY')
WIKIPEDIA_USER_AGENT = os.getenv('WIKIPEDIA_USER_AGENT')
