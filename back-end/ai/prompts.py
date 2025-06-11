SIMPLE_DOCUMENTATION_PROMPT = """
I have a list of OpenAPI 3.0.1 specification for a list of REST services. I want you to generate simple API documentation for each endpoint.

The documentation should include:

An overview of the API (title, version, description of endpoint))

Endpoint documentation including:

Summary/description of what the endpoint does

Please structure the output as clean, well-formatted Markdown. Use headings for each section and include code blocks where appropriate..

Here is the list OpenAPI service specification:

{SERVICE}

Don't explain your reasoning, just provide the answer.
"""

FULL_DOCUMENTATION_PROMPT = """
I have an OpenAPI 3.0.1 specification for a REST service. I want you to generate complete, human-readable API documentation from the endpoint.

The documentation should include:

An overview of the API (title, version, base URL if applicable)

Detailed endpoint documentation including:

HTTP method and path

Summary/description of what the endpoint does

Parameters (path, query, header, cookie) with names, types, descriptions, and whether required

Request body details (media type, schema, required fields, field descriptions)

Response details (status codes, response bodies with schemas and examples)

Data models with field descriptions and required/optional flags

Please structure the output as clean, well-formatted Markdown. Use headings for each section and include code blocks where appropriate. Include examples where possible, even if they must be generated from the schema.

Here is the OpenAPI service specification:

{SERVICE}

Don't explain your reasoning, just provide the answer.
"""

LANGUAGE_CODE_PROMPT = """
I have an OpenAPI (Swagger) specification for a REST API endpoint. Please generate a code that calls this API using.

Your output should include everything needed to integrate and call the service from a app, including:

Classes (models) for the request and response bodies

A API service class to make the HTTP request

The API method with full implementation (handling headers, body, query params if any)

An example usage of the generated code

Use best practices for null safety and error handling

Add comments to explain the generated code

Use this OpenAPI specification as the source for all information:

{SERVICE}

Don't explain your reasoning, just provide the answer.
"""

KNOWLEDGE_BASE_PROMPT = """
You are a helpful assistant with access to a structured knowledge base. Given the following question, 
retrieve relevant information from the knowledge base and provide a clear, concise, and accurate solution.

Knowledge Base Context:
{KNOWLEDGE_BASE_ENTRIES}

User Question:
{USER_QUESTION}

Instructions:
- Summarize or synthesize the information into a solution.
- If multiple solutions exist, briefly compare them.
- If information is missing, state what additional data would be needed.

Don't explain your reasoning, just provide the answer.
"""

MISSION_CONTROL_PROMPT = """
You are a Mission Control, responsible for analyzing user input and determining the correct intent.
Your only task is to classify the query into one of the following categories:

1. **Search Services ('search')**
- If user asks for a list or to search a REST service or endpoint REST
- Examples:
    - 'Give a list the services to quotation'
    - 'I need a service REST to search drivers'
    - 'Give me a service REST to search a catalog of vehicles'

2. **Generate Documentation ('documentation')**
- If user asks to generate a documentation for a specific service REST
- Examples:
    - 'Generate a documentation to service to quotation'
    - 'I need a documentation of the service REST to search drivers'
    - 'Create a full documentation of the service REST to allocate drivers'
    - 'Give me a complete documentation of the service REST catalog of vehicles'

3. **Generate Code ('code')**
- If user asks to generate a programing language code for a specific service REST
- Examples:
    - 'Generate a Java code to service to quotation'
    - 'I need a Python code with request of the service REST to search drivers'
    - 'Create a Java code with resttemplate of the service REST to allocate drivers'
    - 'Give me a complete code of the service REST catalog of vehicles in NodeJS'

4. **Knowledge Base ('knowledge')**
- if the user asks about an error he encountered
- Examples:
    - 'I am receiving an error about target to add digitalized signature'
    - 'When a tried to generate a report I get an error'
    - 'How can I fix the problem to generate report'

5. **Unknown ('unknown')**
- For requests that don't fit into above categories

---

**Important guidelines:**
- **Only classify the request. Do **not** generate an answer or provide additional reasoning.**
- **Return exactly on of the labels:** 'stock', 'crm', 'email', 'research', or 'unknown'.**
- **If unsure, default to 'unknown' and do not attempt ot guess**
- **Your output must follow this structured JSON format:**
{
    "intention": "<one of the labels above>",
    "context": "<original user message>",
    "confidence": "<confidence score between 0 and 1>"
}
"""
