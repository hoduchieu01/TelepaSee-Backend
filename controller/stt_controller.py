import ast
import base64
import os

from flask_socketio import send

from STT.speech_to_text import stt
from controller import socketio
from data.stt.rep_stt_broad_cast_dto import ReplySTTBroadCastDTO
from data.stt.req_stt_broad_cast_dto import RequestSTTBroadCastDTO


@socketio.on('stt')
def stt_controller(data):
    stt_broadcast_dto = RequestSTTBroadCastDTO("", "", "")
    if type(data) == str:
        dict_request_data_json = ast.literal_eval(data)
        stt_broadcast_dto = RequestSTTBroadCastDTO.from_dict(dict_request_data_json)
    else:
        stt_broadcast_dto = RequestSTTBroadCastDTO.from_dict(data)

    with open("stt_sound.wav", 'wb') as f:
        # base64로 되어있는 음성데이터를 test wav 파일로 변경함
        byte_array = base64.b64decode(stt_broadcast_dto.voice_data)
        f.write(byte_array)

    text_data = stt("stt_sound.wav")
    os.remove("stt_sound.wav")
    reply_dto = ReplySTTBroadCastDTO(stt_broadcast_dto.name, text_data)

    room = stt_broadcast_dto.room
    send(reply_dto.to_json(), room=stt_broadcast_dto.room)

    pass