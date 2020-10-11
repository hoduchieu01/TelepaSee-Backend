import ast
import base64
import os

from flask_socketio import send

from controller import socketio
from data.translate.rep_translate_dto import ReplyTranslateDTO
from data.translate.req_translate_dto import RequestTranslateDTO
from translation.translation_with_mic import translation_once_from_mic


@socketio.on('translate')
def translate_controller(data):
    request_translate_dto = RequestTranslateDTO("", "", "")
    if type(data) == str:
        dict_request_data_json = ast.literal_eval(data)
        request_translate_dto = RequestTranslateDTO.from_dict(dict_request_data_json)
    else:
        request_translate_dto = RequestTranslateDTO.from_dict(data)

    # 갖고온 음성데이터를 파일로 만듬
    with open("translate_voice_source.wav", 'wb') as f:
        # base64로 되어있는 음성데이터를 test wav 파일로 변경함
        byte_array = base64.b64decode(request_translate_dto.voice_data)
        f.write(byte_array)

    translated_message = translation_once_from_mic("translate_voice_source.wav")
    os.remove("translate_voice_source.wav")

    reply_dto = ReplyTranslateDTO(request_translate_dto.name, translated_message[1])
    send(reply_dto.to_json(), room=request_translate_dto.room)

    # 갖고온 음성 파일을 제거
    pass