from flask_socketio import SocketIO

socketio = SocketIO(always_connect=True, cors_allowed_origins='*')

from . import tts_controller, connect_controller