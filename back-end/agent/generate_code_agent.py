import json
from datetime import datetime

from langchain_core.messages import AIMessage

from ai.gen_ai import AIModel, LLM_OPENAI_GPT_4O_MINI
from ai.prompts import LANGUAGE_CODE_PROMPT
from retrive.QDrantRetriever import QDrantRetriever
from retrive.mongo_retrieve import MongoRetrieve


def generate_code_agent(state):
    """
    An agent to generate code of the service REST from the Mission Control's response using OpenAPI specification.
    """

    last_ai_message = state['messages'][-1]
    intent_data = json.loads(last_ai_message.content)
    context = intent_data.get('context', 'No context available')
    confidence = intent_data.get('confidence', 0.0)

    print('START RETRIEVE ', datetime.now())
    # contextual_retrieve = MongoRetrieve(_db='MYLLMI', _collection='LABS', _query=context, _index='CONTEXT_INDEX')
    contextual_retrieve = QDrantRetriever(_query=context)
    retriever = contextual_retrieve.get_retriever()
    print('END RETRIEVE ', datetime.now())

    # spec = retriever[0]['service_spec'] # MongoDB
    spec = retriever[0].payload['service_spec']
    print('START AI Model ', datetime.now())
    ai = AIModel(_model=LLM_OPENAI_GPT_4O_MINI)
    answer = ai.chat(spec, context + '\n' + LANGUAGE_CODE_PROMPT)
    print('END AI Model ', datetime.now())

    return {
        "messages": [AIMessage(content=answer.content)]
    }


