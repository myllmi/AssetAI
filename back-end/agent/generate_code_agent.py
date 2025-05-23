import json

from langchain_core.messages import AIMessage

from ai.gen_ai import AIModel, LLM_OPENAI_GPT_4O_MINI
from ai.prompts import LANGUAGE_CODE_PROMPT
from retrive.contextual_retrieve import ContextualRetrieve


def generate_code_agent(state):
    """
    An agent to generate code of the service REST from the Mission Control's response using OpenAPI specification.
    """

    last_ai_message = state['messages'][-1]
    intent_data = json.loads(last_ai_message.content)
    context = intent_data.get('context', 'No context available')
    confidence = intent_data.get('confidence', 0.0)

    contextual_retrieve = ContextualRetrieve(_db='MYLLMI', _collection='LABS', _query=context, _index='CONTEXT_INDEX')
    retriever = contextual_retrieve.get_retriever()

    spec = retriever[0]['service_spec']
    ai = AIModel(_model=LLM_OPENAI_GPT_4O_MINI)
    answer = ai.chat(spec, context + '\n' + LANGUAGE_CODE_PROMPT)

    return {
        "messages": [AIMessage(content=answer.content)]
    }


