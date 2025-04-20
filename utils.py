import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Load model only once
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load the CSV with Q&A
df = pd.read_csv("formatted_qa.csv")

# Precompute embeddings of all questions
df['embedding'] = df['Question'].apply(lambda x: model.encode(x, convert_to_tensor=True))

def get_answer(query):
    query_embedding = model.encode(query, convert_to_tensor=True)
    
    # Compute cosine similarities
    similarities = df['embedding'].apply(lambda x: float(util.cos_sim(x, query_embedding)))
    
    # Get best match
    best_idx = similarities.idxmax()
    best_question = df.iloc[best_idx]['Question']
    best_answer = df.iloc[best_idx]['Answer']
    
    return f"**Answer:** {best_answer}\n\n_(Matched with: '{best_question}')_"
