import json
from typing import TypedDict, Annotated

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langgraph.graph import add_messages
from pydantic import BaseModel

from ai.gen_ai import AIModel, LLM_OPENAI_GPT_4O_MINI
from ai.prompts import MISSION_CONTROL_PROMPT


class State(TypedDict):
    messages: Annotated[list, add_messages]


class Decision(BaseModel):
    intention: str
    context: str
    confidence: float

llm = AIModel(_model=LLM_OPENAI_GPT_4O_MINI)
structured_llm = llm.get_llm().with_structured_output(Decision)


def mission_control(state: State):
    """Extract intent from user input using a structured prompt and returns a parsed JSON as an AIMessage."""
    messages = [
        SystemMessage(content=MISSION_CONTROL_PROMPT),
        HumanMessage(content=state["messages"][-1].content)
    ]
    _output = structured_llm.invoke(messages)
    print(_output)

    return {"messages": [AIMessage(content=json.dumps(_output.model_dump()))]}
