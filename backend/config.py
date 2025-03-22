import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

FAISS_MODEL = os.getenv("FAISS_MODEL", "sentence-transformers/paraphrase-MiniLM-L3-v2")
FAISS_NUM_NEIGHBORS = int(os.getenv("FAISS_NUM_NEIGHBORS", 5))

LLM_MODEL = os.getenv("LLM_MODEL", "mixtral-8x7b-32768")

