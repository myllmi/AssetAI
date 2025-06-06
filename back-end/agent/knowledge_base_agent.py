import json
from datetime import datetime

from langchain_core.messages import AIMessage

from ai.gen_ai import AIModel, LLM_OPENAI_GPT_4O_MINI
from ai.prompts import KNOWLEDGE_BASE_PROMPT
from retrive.QDrantRetriever import QDrantRetriever


def knowledge_base_agent(state):
    """
    An agent to identify and generate a response with the solution for the question from knowledge base
    """
    last_ai_message = state['messages'][-1]
    intent_data = json.loads(last_ai_message.content)
    context = intent_data.get('context', 'No context available')
    confidence = intent_data.get('confidence', 0.0)

    print('START RETRIEVE ', datetime.now())
    # contextual_retrieve = MongoRetrieve(_db='MYLLMI', _collection='LABS', _query=context, _index='CONTEXT_INDEX')
    contextual_retrieve = QDrantRetriever(_query=context)
    retriever = contextual_retrieve.get_retriever(_collection="KNOWLEDGE_BASE")
    print('END RETRIEVE ', datetime.now())

    # spec = retriever[0]['service_spec'] # MongoDB
    solution = retriever[0].payload['solution']
    print('START AI Model ', datetime.now())
    ai = AIModel(_model=LLM_OPENAI_GPT_4O_MINI)
    print(context)
    print(solution)
    answer = ai.chat_knowledge_base(context, solution, KNOWLEDGE_BASE_PROMPT, True)
    print('END AI Model ', datetime.now())

    return {
        "messages": [AIMessage(content=answer.content)]
    }
