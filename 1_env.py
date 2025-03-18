import os
from dotenv import load_dotenv

load_dotenv()

value = os.getenv("API_KEY")
print(f"環境變數 API_KEY: {value}")