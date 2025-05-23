import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.operations import SearchIndexModel

load_dotenv()

MONGODB_ATLAS_CLUSTER_URI = f'mongodb+srv://{os.environ['MONGODB_USR']}:{os.environ['MONGODB_PWD']}@{os.environ['MONGODB_URL']}/?retryWrites=true&w=majority'


class DBMongo:

    def __init__(self):
        self.mongo_client = MongoClient(MONGODB_ATLAS_CLUSTER_URI)

    def get_db(self, db):
        return self.mongo_client[db]

    def get_collection(self, db, collection):
        conn = self.get_db(db)
        return conn[collection]

    def find_similar(self, _db='MYLLMI', _collection='LABS', _query_embedding=None, _index='CONTEXT_INDEX',
                     _plot_embedding='plot_embedding'):
        collection = self.get_collection(_db, _collection)
        result = collection.aggregate([
            {"$vectorSearch": {
                "queryVector": _query_embedding,
                "path": _plot_embedding,
                "numCandidates": 100,
                "limit": 5,
                "index": _index,
            }}
        ])
        return list(result)

    def create_db(self, _db):
        self.get_db(_db)

    def create_collection(self, _db, _collection):
        self.get_collection(_db, _collection)

    def create_index(self, _db, _collection, _index):
        search_index_model = SearchIndexModel(
            definition={
                "fields": [
                    {
                        "type": "vector",
                        "numDimensions": 1536,
                        "path": "plot_embedding",
                        "similarity": "cosine"
                    }
                ]
            },
            name=_index,
            type="vectorSearch",
        )
        self.get_collection(_db, _collection).create_search_index(model=search_index_model)

    def insert_one(self, _db, _collection, _dict):
        collection = self.get_collection(_db, _collection)
        return collection.insert_one(_dict)

    def delete_one(self, _db, _collection, _dict):
        collection = self.get_collection(_db, _collection)
        collection.delete_one(_dict)

    def update_one(self, _db, _collection, _filter, _dict):
        collection = self.get_collection(_db, _collection)
        new_values = {'$set': _dict}
        return collection.update_one(_filter, new_values)

    ### OLD ###
    def get_one(self, _db, _collection, _dict):
        collection = self.get_collection(_db, _collection)
        return collection.find_one(_dict)

    def get_many(self, _db, _collection, _dict):
        collection = self.get_collection(_db, _collection)
        return list(collection.find(_dict))

    def search_collection(self, _db, _collection, _aggregate):
        collection = self.get_collection(_db, _collection)
        result = collection.aggregate(_aggregate)
        return list(result)

    ### DANGER ZONE ###
    # def clean_collection(self, _db, _collection):
    #     collection = self.get_collection(_db, _collection)
    #     list_docs = self.get_many(_db, _collection, {})
    #     for doc in list_docs:
    #         collection.delete_one({'_id': doc['_id']})
