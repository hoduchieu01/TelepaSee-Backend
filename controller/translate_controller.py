import ast
import base64

from flask_socketio import send

from TTS.text_to_speech import tts
from controller import socketio
from data.translate.rep_translate_dto import ReplyTranslateDTO
from data.translate.req_translate_dto import RequestTranslateDTO
from data.tts.rep_tts_broad_cast_dto import ReplyTTSBroadCastDTO
from data.tts.req_tts_broad_cast_dto import RequestTTSBroadCastDTO


@socketio.on('translate')
def stt_controller(data):
    request_translate_dto = RequestTranslateDTO("", "", "")
    if type(data) == str:
        dict_request_data_json = ast.literal_eval(data)
        request_translate_dto = RequestTranslateDTO.from_dict(dict_request_data_json)
    else:
        request_translate_dto = RequestTranslateDTO.from_dict(data)

    translated_message = translate(request_translate_dto.message)
    reply_dto = ReplyTranslateDTO(request_translate_dto.name, translated_message)

    send(reply_dto.to_json(), room=request_translate_dto.room)

    pass