import ast
import base64

from flask import request, jsonify
from flask_cors import CORS

from TTS.texttospeech import tts
from controller import stt_blueprint
from data.tts_data import TTSDataDTO

CORS(stt_blueprint, supports_credentials=True, resources={r"/*": {"origins": "*"}})


@stt_blueprint.route("/echo", methods=["POST"])
def stt_data():
    pass