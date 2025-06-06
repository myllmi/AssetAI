import os
import uuid

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

QDRANT__URI = f'{os.environ['QDRANT_URL']}'

class DBQdrant:
    def __init__(self):
        self.qdrant_client = QdrantClient(url=QDRANT__URI)

    def insert_one_spec(self, _dict):
        point_spec = PointStruct(
            id=str(uuid.uuid4()),
            vector=_dict['plot_embedding'],
            payload={
                'service_spec': _dict['service_spec'],
                'summary': _dict['summary'],
                'description': _dict['description']
            }
        )
        self.qdrant_client.upsert(collection_name='API_EXTERNAL', points=[point_spec])

    def insert_one_knowledge(self, _dict):
        point_spec = PointStruct(
            id=str(uuid.uuid4()),
            vector=_dict['plot_embedding'],
            payload={
                'description': _dict['description'],
                'summary': _dict['summary'],
                'solution': _dict['solution']
            }
        )
        self.qdrant_client.upsert(collection_name='KNOWLEDGE_BASE', points=[point_spec])