from flask import Flask, make_response
import os
import signal

application = Flask(__name__)

@application.route('/index', methods=['GET'])
def index():
    server_identifier = os.getenv('SERVER_ID')
    response_data = {
        'msg': f"Greetings from Server: {server_identifier}",
        'status': 'success'
    }
    return make_response(response_data), 200

@application.route('/ping', methods=['GET'])
def ping():
    return make_response({}), 200

@application.route('/terminate', methods=['POST'])
def terminate():
    print("Initiating graceful shutdown...")
    os.kill(os.getpid(), signal.SIGINT)
    return make_response({'msg': 'Server is shutting down...'}), 200

if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0', port='5000')