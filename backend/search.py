import json
import faiss


class ShoeSearch:
    def __init__(
        self,
        index_path="shoes.faiss",
        paths_path="shoe_paths.json"
    ):
        self.index = faiss.read_index(index_path)

        with open(paths_path, "r") as f:
            self.paths = json.load(f)

    def search(self, query_embedding, top_k=10):
        scores, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for score, index in zip(
            scores[0],
            indices[0]
        ):
            results.append({
                "score": float(score),
                "path": self.paths[index]
            })

        return results
