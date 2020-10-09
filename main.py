from flask import Flask

from controller import socketio

if __name__ == '__main__':
    app = Flask(__name__)
    socketio.init_app(app)
    socketio.run(app, host='0.0.0.0', port=8080, debug=False, use_reloader=False)
