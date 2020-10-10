import ast
import base64

from flask import request, jsonify
from flask_cors import CORS

from TTS.texttospeech import tts
from controller import tts_blueprint
from data.tts_data import TTSDataDTO

CORS(tts_blueprint, supports_credentials=True, resources={r"/*": {"origins": "*"}})


@tts_blueprint.route("/echo", methods=["POST"])
def convert_to_tts():
    data_str = request.data.decode("UTF_8")
    data_json = ast.literal_eval(data_str)
    tts_data_dto = TTSDataDTO.from_dict(data_json)

    audio_data = tts(tts_data_dto.message)

    print("encoding audio data to base64")
    base_64_encode = audio_data
    e = base64.b64encode(base_64_encode)

    print("reply audio data to client")
    return jsonify(name=tts_data_dto.name,
                   data_message=e.decode("UTF-8"))