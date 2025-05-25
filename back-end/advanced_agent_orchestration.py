from dotenv import load_dotenv
from langgraph.constants import END
from langgraph.graph import StateGraph

from agent.generate_code_agent import generate_code_agent
from agent.generate_documentation_agent import generate_documentation_agent
from agent.search_service_agent import search_service_agent
from agent.unknow_agent import unknown_agent
from mission_control.mission_control import State, mission_control
from router.router import router

load_dotenv()

graph_builder = StateGraph(State)
graph_builder.add_node('mission_control', mission_control)

graph_builder.add_node('router', router)
graph_builder.add_edge('mission_control', 'router')


def get_next_agent(state):
    return state['next_agent']


graph_builder.add_conditional_edges('router', get_next_agent, {
    'search_service_agent': 'search_service_agent',
    'generate_documentation_agent': 'generate_documentation_agent',
    'generate_code_agent': 'generate_code_agent',
    'unknown_agent': 'unknown_agent',
    END: END
})

graph_builder.add_node('search_service_agent', search_service_agent)
graph_builder.add_edge('search_service_agent', END)

graph_builder.add_node('generate_documentation_agent', generate_documentation_agent)
graph_builder.add_edge('generate_documentation_agent', END)

graph_builder.add_node('generate_code_agent', generate_code_agent)
graph_builder.add_edge('generate_code_agent', END)

graph_builder.add_node('unknown_agent', unknown_agent)
graph_builder.add_edge('unknown_agent', END)

graph_builder.set_entry_point('mission_control')

graph = graph_builder.compile()


def get_response(_prompt):
    # return graph.invoke({'messages': ('user', _prompt)})['messages'][-1].content
    return graph.stream({'messages': ('user', _prompt)}, stream_mode="messages")


# response = graph.invoke({'messages': ('user', 'How is my life?')})
# response = graph.invoke({'messages': ('user', 'can you get me my contacts')})
# response = graph.invoke({'messages': ('user', 'how is google doing in the market today')})
# response = graph.invoke({'messages': ('user', 'what can you tell me about langchain?')})
# response = graph.invoke({'messages': ('user', 'Send email to Michael Smith')})
# response = graph.invoke({'messages': ('user', 'I need a service REST to get allocated drivers')})
# response = graph.invoke({'messages': ('user', 'Generate a documentation for the service Update Allocated Driver')})
# response = graph.invoke({'messages': ('user', 'Generate a Java code using RestTemplate to call the service Update Allocated Driver')})
# response = graph.invoke({'messages': ('user', 'Crie um código Kotlin usando Spring WebFlux para chamar o serviço REST Upload Applicant Credit Score Stipulation Document')})
# print('Assistant: ', response['messages'][-1].content)

# res_stream = graph.stream({'messages': ('user', 'I need a service REST to get allocated drivers')}, stream_mode="messages")
# for message, metadata in res_stream:
#     # if metadata["langgraph_node"] == "generate":
#     print(message.content)
