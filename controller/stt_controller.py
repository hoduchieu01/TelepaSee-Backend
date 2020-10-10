import ast
import base64

from flask_socketio import send

from TTS.text_to_speech import tts
from controller import socketio
from data.tts.rep_tts_broad_cast_dto import ReplyTTSBroadCastDTO
from data.tts.req_tts_broad_cast_dto import RequestTTSBroadCastDTO


@socketio.on('stt')
def stt_controller(data):
    stt_broadcast_dto = RequestTTSBroadCastDTO("", "", "")
    if type(data) == str:
        dict_request_data_json = ast.literal_eval(data)
        stt_broadcast_dto = RequestTTSBroadCastDTO.from_dict(dict_request_data_json)
    else:
        stt_broadcast_dto = RequestTTSBroadCastDTO.from_dict(data)

    audio_data = tts(stt_broadcast_dto.text_data)
    base64_audio_data = base64.b64encode(audio_data).decode("UTF-8")
    reply_dto = ReplyTTSBroadCastDTO(stt_broadcast_dto.name, base64_audio_data)

    room = stt_broadcast_dto.room
    send(reply_dto.to_json(), room=stt_broadcast_dto.room)

    pass
