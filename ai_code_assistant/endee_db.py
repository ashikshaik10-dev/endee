import numpy as np

class EndeeDB:
    def __init__(self):
        self.data = []

    def insert(self, vector, metadata):
        self.data.append({
            "vector": np.array(vector),
            "metadata": metadata
        })

    def search(self, query_vector, top_k=3):
        query_vector = np.array(query_vector)

        results = []
        for item in self.data:
            score = np.dot(query_vector, item["vector"]) / (
                np.linalg.norm(query_vector) * np.linalg.norm(item["vector"])
            )
            results.append((score, item))

        results.sort(reverse=True, key=lambda x: x[0])
        return results[:top_k]