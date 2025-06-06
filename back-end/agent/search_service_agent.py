import json
from datetime import datetime

from langchain_core.messages import AIMessage

from ai.gen_ai import AIModel, LLM_OPENAI_GPT_4O_MINI
from ai.prompts import SIMPLE_DOCUMENTATION_PROMPT
from retrive.QDrantRetriever import QDrantRetriever
from retrive.mongo_retrieve import MongoRetrieve


def search_service_agent(state):
    """
    An agent to search from the Mission Control's response and return a list of the services.
    """
    last_ai_message = state['messages'][-1]
    intent_data = json.loads(last_ai_message.content)
    context = intent_data.get('context', 'No context available')
    confidence = intent_data.get('confidence', 0.0)

    print('START RETRIEVE ', datetime.now())
    # contextual_retrieve = MongoRetrieve(_db='MYLLMI', _collection='LABS', _query=context, _index='CONTEXT_INDEX')
    contextual_retrieve = QDrantRetriever(_query=context)
    retriever = contextual_retrieve.get_retriever(_collection="API_EXTERNAL")
    print('END RETRIEVE ', datetime.now())

    arr_spec = []
    for spec in retriever:
        arr_spec.append(spec.payload['service_spec'])
        # arr_spec.append(spec['service_spec']) # MongoDB
    print('START AI Model ', datetime.now())
    ai = AIModel(_model=LLM_OPENAI_GPT_4O_MINI)
    answer = ai.chat_spec('\n\n'.join(arr_spec), SIMPLE_DOCUMENTATION_PROMPT, _stream=True)
    print('END AI Model ', datetime.now())

    return {
        "messages": [AIMessage(content=answer.content)]
    }
