import ast

from flask_socketio import send

from controller import socketio
from data.vidoe.video_data_dto import VideoDataDTO


@socketio.on('tts')
def video_chat_controller(data):
    video_data_dto = VideoDataDTO("", "", "", "")

    if type(data) == str:
        dict_request_data_json = ast.literal_eval(data)
        video_data_dto = VideoDataDTO.from_dict(dict_request_data_json)
    else:
        video_data_dto = VideoDataDTO.from_dict(data)


    # broadcast of chat groop users
    send(video_data_dto.to_json(), room=video_data_dto.room)
