import os

from qdrant_client import QdrantClient

QDRANT__URI = f'{os.environ['QDRANT_URL']}'


class DBQdrant:
    def __init__(self):
        self.qdrant_client = QdrantClient(url=QDRANT__URI)

    def search_similar(self, _query_embedding):
        hits = self.qdrant_client.query_points(collection_name="API_EXTERNAL", query=_query_embedding, limit=3)
        return hits.points
