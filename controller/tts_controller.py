from flask_socketio import send

from controller import socketio

@socketio.on('echo')
def connect(data):
    print("connect complete")
    send("connect complete")
    pass