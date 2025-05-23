from flask import Flask, json, request, Response, stream_with_context
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

from advanced_agent_orchestration import get_response

app = Flask(__name__)
CORS(app)

arr_content = []


@app.before_request
def auth_filter():
    if request.path.startswith('/protected/') and request.method != 'OPTIONS':
        pass
        # response_helper = ResponseHelper()
        # token = request.headers.get('Authorization')
        # login_service = LoginService()
        # try:
        #     login_service.validate_access_token(token)
        # except (TokenExpiredException, NotFoundException):
        #     response_helper.set_code(401, 'Access token expired')
        # return response_helper.get_response()


@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


@app.route('/')
def index():
    return 'Hello from Asset AI!'


@app.route('/chat/listen')
def stream():
    def event_stream():
        global arr_content
        while True:
            arr_chunk = arr_content
            arr_content = []
            for i in arr_chunk:
                yield i

    return Response(stream_with_context(event_stream()), content_type='text/event-stream')


@app.route('/chat/q', methods=['POST'])
def query():
    print(request)
    object_request = request.get_json()
    print(object_request)
    res_stream = get_response(object_request['_question'])
    for message, metadata in res_stream:
        # print(message)
        # print(metadata)
        if metadata["langgraph_node"] != "mission_control":
            arr_content.append('data: ' + message.content + '\n\n' + 'id: ' + object_request['randomEvent'] + '\n\n')
    return {}, 200
    #
    # response_helper = ResponseHelper()
    # response_helper.set_data({
    #     'llm': get_response(object_request['term'])
    # })
    # return response_helper.get_response()


if __name__ == '__main__':
    app.run(debug=True)
