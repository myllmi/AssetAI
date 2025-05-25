import json

from langchain_core.messages import AIMessage

from ai.gen_ai import AIModel, LLM_OPENAI_GPT_4O_MINI
from ai.prompts import SIMPLE_DOCUMENTATION_PROMPT
from retrive.contextual_retrieve import ContextualRetrieve


def search_service_agent(state):
    """
    An agent to search from the Mission Control's response and return a list of the services.
    """
    last_ai_message = state['messages'][-1]
    intent_data = json.loads(last_ai_message.content)
    context = intent_data.get('context', 'No context available')
    confidence = intent_data.get('confidence', 0.0)

    contextual_retrieve = ContextualRetrieve(_db='MYLLMI', _collection='LABS', _query=context, _index='CONTEXT_INDEX')
    retriever = contextual_retrieve.get_retriever()

    # spec = retriever[0]['service_spec']
    arr_spec = []
    for spec in retriever:
        arr_spec.append(spec['service_spec'])
    ai = AIModel(_model=LLM_OPENAI_GPT_4O_MINI)
    answer = ai.chat('\n\n'.join(arr_spec), SIMPLE_DOCUMENTATION_PROMPT, _stream=True)

    return {
        "messages": [AIMessage(content=answer.content)]
    }
