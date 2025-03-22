import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("Error: GROQ_API_KEY is missing in .env file!")
if not HUGGINGFACE_API_KEY:
    raise ValueError("Error: HUGGINGFACE_API_KEY is missing in .env file!")

print("Environment variables loaded successfully.")
