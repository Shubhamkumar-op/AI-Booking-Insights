import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer
from huggingface_hub import login
from backend.config import HUGGINGFACE_API_KEY, FAISS_MODEL, FAISS_NUM_NEIGHBORS

df = pd.read_csv("data/hotel_bookings.csv")

# Authenticate Hugging Face API Key
login(HUGGINGFACE_API_KEY)

# Initialize FAISS model
model = SentenceTransformer(FAISS_MODEL)

embeddings = model.encode(df['hotel'].astype(str).tolist(), convert_to_numpy=True)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

def query_faiss(query):
    query_vector = model.encode([query])
    _, indices = index.search(query_vector, k=FAISS_NUM_NEIGHBORS)
    return df.iloc[indices[0]].to_dict()
