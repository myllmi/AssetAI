from ai.gen_ai import AIEmbedding
from db.db_mongo import DBMongo


class ContextualRetrieve:
    def __init__(self, _db=None, _collection=None, _query=None, _index=None):
        self._db = _db
        self._collection = _collection
        self._query = _query
        self._index = _index
        self.ai = AIEmbedding()
        self._dao = DBMongo()

    def get_retriever(self):
        embeddings = self.ai.generate_embedding(self._query)
        return self._dao.find_similar(_db=self._db, _collection=self._collection, _index=self._index, _query_embedding=embeddings)
