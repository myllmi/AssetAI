from dotenv import load_dotenv
from langchain_ollama import OllamaEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_voyageai import VoyageAIEmbeddings

load_dotenv()

# Const Embedding models
EMBEDDING_OPENAI_TEXT_3_SMALL = 'OPENAI_TEXT_3_SMALL'   # Dimensions: 1536
EMBEDDING_VOYAGE_3_5 = 'VOYAGE_3_5'                     # Dimensions: 1024
EMBEDDING_META_LLAMA_3 = 'META_LLAMA_3'                 # Dimensions: 4096 for LLaMA 3 8B / 8192 for LLaMA 3 70B


class AIEmbedding:
    def __init__(self, _embedding_model=EMBEDDING_OPENAI_TEXT_3_SMALL):
        self.embedding_model = self.select_embedding_model(_embedding_model)

    @staticmethod
    def select_embedding_model(_embedding_model=EMBEDDING_OPENAI_TEXT_3_SMALL):
        if _embedding_model == EMBEDDING_VOYAGE_3_5:
            return VoyageAIEmbeddings(model='voyage-3.5', batch_size=1)
        elif _embedding_model == EMBEDDING_META_LLAMA_3:
            return OllamaEmbeddings(model="llama3")
        else:
            return OpenAIEmbeddings(model="text-embedding-3-small")

    def generate_embedding(self, _sentence):
        return self.embedding_model.embed_query(_sentence)
