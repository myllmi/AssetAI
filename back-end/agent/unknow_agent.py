import json

from langchain_core.messages import AIMessage


def unknown_agent(state):
    """
    A simple Unknown Agent that extracts `content` and `confidence` from the Mission Control's response and returns a message.
    """
    last_ai_message = state['messages'][-1]
    try:
        intent_data = json.loads(last_ai_message.content)
        context = intent_data.get('context', 'No context available')
        confidence = intent_data.get('confidence', 0.0)
    except json.JSONDecodeError:
        context = 'Error decoding context'
        confidence = 0.0
    return {
        "messages": [AIMessage(
            content=f"Sorry, I can't help with this question {context}. Try question related to Developer Portal")]
    }
