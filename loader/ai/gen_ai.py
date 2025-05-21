from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_voyageai import VoyageAIEmbeddings

load_dotenv()

# Const Embedding models
EMBEDDING_OPENAI_TEXT_3_SMALL = 'OPENAI_TEXT_3_SMALL'
EMBEDDING_VOYAGE_TEXT_3_SMALL = 'VOYAGE_TEXT_3_SMALL'


class AIEmbedding:
    def __init__(self, _embedding_model=EMBEDDING_OPENAI_TEXT_3_SMALL):
        self.embedding_model = self.select_embedding_model(_embedding_model)

    @staticmethod
    def select_embedding_model(_embedding_model=EMBEDDING_OPENAI_TEXT_3_SMALL):
        if _embedding_model == EMBEDDING_VOYAGE_TEXT_3_SMALL:
            return VoyageAIEmbeddings(model='voyage-3.5', batch_size=1)
        else:
            return OpenAIEmbeddings(model="text-embedding-3-small")

    def generate_embedding(self, _sentence):
        return self.embedding_model.embed_query(_sentence)
