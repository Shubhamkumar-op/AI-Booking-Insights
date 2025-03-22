import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer
from huggingface_hub import login
from config import HUGGINGFACE_API_KEY, FAISS_MODEL, FAISS_NUM_NEIGHBORS
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(BASE_DIR, "data/hotel_bookings.csv")
df = pd.read_csv(csv_path, usecols=["hotel", "arrival_date_year", "adr"], nrows=5000)  # Load fewer rows



login(HUGGINGFACE_API_KEY)

model = SentenceTransformer(FAISS_MODEL)

embeddings = model.encode(df['hotel'].astype(str).tolist(), convert_to_numpy=True)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

def query_faiss(query):
    query_vector = model.encode([query])
    _, indices = index.search(query_vector, k=FAISS_NUM_NEIGHBORS)
    return df.iloc[indices[0]].to_dict()
