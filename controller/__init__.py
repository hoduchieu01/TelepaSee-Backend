from flask_socketio import SocketIO

socketio = SocketIO(always_connect=True, cors_allowed_origins='*')

from . import video_controller, translate_controller, stt_controller, tts_controller, connect_controller
