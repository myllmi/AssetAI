from ai.gen_ai import AIEmbedding
from db.db_qdrant import DBQdrant


class QDrantRetriever:
    def __init__(self, _query=None):
        self.ai = AIEmbedding()
        self._db_qdrant = DBQdrant()
        self._query = _query

    def get_retriever(self, _collection):
        embeddings = self.ai.generate_embedding(self._query)
        return self._db_qdrant.search_similar(_query_embedding=embeddings, _collection=_collection)
