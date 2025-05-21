import tiktoken
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

load_dotenv()

# Const LLM models
LLM_OPENAI_GPT_4O_MINI = 'OPENAI_GPT_4O_MINI'

# Const Embedding models
EMBEDDING_OPENAI_TEXT_3_SMALL = 'OPENAI_TEXT_3_SMALL'


class AIModel:

    def __init__(self, _model=LLM_OPENAI_GPT_4O_MINI):
        self.client_llm = self.select_model(_model=_model)

    @staticmethod
    def select_model(_model=LLM_OPENAI_GPT_4O_MINI):
        return ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
            timeout=None,
            max_retries=2,
            streaming=False
        )

    def chat(self, service_spec):
        prompt_template = PromptTemplate.from_template(
            """
            Using the openapi service specification: 
            
            {SERVICE}
            
            Generate a Java service code using Spring Boot RestTemplate 
            and generate parameter and response documentation of service 
            usage.
                        
            Don't explain your reasoning, just provide the answer.
            """
        )
        chain = prompt_template | self.client_llm
        return chain.invoke(
            {
                "SERVICE": service_spec
            }
        )


class AIEmbedding:
    def __init__(self, _embedding_model=EMBEDDING_OPENAI_TEXT_3_SMALL):
        self.embedding_model = self.select_embedding_model()

    @staticmethod
    def select_embedding_model():
        return OpenAIEmbeddings(model="text-embedding-3-small")

    def generate_embedding(self, sentence):
        return self.embedding_model.embed_query(sentence)


class AIToken:

    @staticmethod
    def num_tokens_from_string(_text: str, _encoding_name) -> int:
        encoding = tiktoken.get_encoding(_encoding_name)
        num_tokens = len(encoding.encode(_text))
        return num_tokens
