import numpy as np
from embed import model

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search(query, db_data, top_k=3):
    query_emb = model.encode([query])[0]

    results = []
    for item in db_data:
        score = cosine_similarity(query_emb, item["vector"])
        results.append((score, item))

    results.sort(reverse=True, key=lambda x: x[0])
    return results[:top_k]