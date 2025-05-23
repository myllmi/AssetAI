import json

from langgraph.constants import END

from mission_control.mission_control import State

ROUTE_MAP = {
    'search': 'search_service_agent',
    'documentation': 'generate_documentation_agent',
    'code': 'generate_code_agent',
    'unknown': 'unknown_agent'
}


def router(state: State):
    """Router the user query to the appropriate agent base on Mission Control's classification."""
    mission_control_output = json.loads(state["messages"][-1].content)
    intention = mission_control_output.get('intention', 'unknown')
    context = mission_control_output.get('context', 'No context found')
    confidence = mission_control_output.get('confidence', 0.0)

    return {
        "next_agent": ROUTE_MAP.get(intention, END),
        "context": context,
        "confidence": confidence
    }
