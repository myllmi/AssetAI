from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_voyageai import VoyageAIEmbeddings

load_dotenv()

# Const Embedding models
EMBEDDING_OPENAI_TEXT_3_SMALL = 'OPENAI_TEXT_3_SMALL'   # Dimensions: 1536
EMBEDDING_VOYAGE_3_5 = 'VOYAGE_3_5'                     # Dimensions: 512
EMBEDDING_META_LLAMA_3 = 'META_LLAMA_3'                 # Dimensions: 4096 for LLaMA 3 8B / 8192 for LLaMA 3 70B

# Const generate models
LLM_OPENAI_GPT_4O_MINI = 'OPENAI_GPT_4O_MINI'
LLM_META_LLAMA_32 = 'META_LLAMA_32'
LLM_MISTRAL_DEVSTRAL = 'MISTRAL_DEVSTRAL'


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


class AIModel:

    def __init__(self, _model=LLM_OPENAI_GPT_4O_MINI):
        self.client_llm = self.select_model(_generative_model=_model)

    @staticmethod
    def select_model(_generative_model=LLM_OPENAI_GPT_4O_MINI):
        if _generative_model == LLM_META_LLAMA_32:
            return OllamaLLM(
                model="llama3.2",
                temperature=0,
                base_url="http://localhost:11434"
            )
        elif _generative_model == LLM_MISTRAL_DEVSTRAL:
            return OllamaLLM(
                model="devstral",
                temperature=0,
                base_url="http://localhost:11434")
        else:
            return ChatOpenAI(
                model="gpt-4o-mini",
                temperature=0,
                timeout=None,
                max_retries=2,
                streaming=False
            )

    def get_llm(self):
        return self.client_llm

    def chat_spec(self, _context, _prompt, _stream=False):
        prompt_template = PromptTemplate.from_template(_prompt)
        chain = prompt_template | self.client_llm
        return chain.invoke(
            {
                "SERVICE": _context
            },
            stream=_stream
        )

    def chat_knowledge_base(self, _question, _context, _prompt, _stream=False):
        prompt_template = PromptTemplate.from_template(_prompt)
        chain = prompt_template | self.client_llm
        return chain.invoke(
            {
                "KNOWLEDGE_BASE_ENTRIES": _context,
                "USER_QUESTION": _question
            },
            stream=_stream
        )
