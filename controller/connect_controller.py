import ast
import json

from flask import request
from flask_socketio import join_room, leave_room, send, rooms, emit

from controller import socketio
from data.room_data_dto import RoomDataDTO


@socketio.on('leave')
def levae_room_request(data):
    if 'room' not in data:
        send("Room parameter is not exsist. require room infomation")
        print("접속자의 room 정보가 없어서 저장하지 못했습니다.")
        return

    room_data_dto = RoomDataDTO("", "")
    if type(data) == str:
        dict_request_data_json = ast.literal_eval(data)
        room_data_dto = RoomDataDTO.from_dict(dict_request_data_json)
    else:
        room_data_dto = RoomDataDTO.from_dict(data)

    send(f"leave {room_data_dto.room}")
    leave_room(room_data_dto.room)


@socketio.on('join')
def join_room_request(data):
    if 'room' not in data:
        send("Room parameter is not exsist. require room infomation")
        print("접속자의 room 정보가 없어서 저장하지 못했습니다.")
        return

    room_data_dto = RoomDataDTO("", "")
    if type(data) == str:
        dict_request_data_json = ast.literal_eval(data)
        room_data_dto = RoomDataDTO.from_dict(dict_request_data_json)
    else:
        room_data_dto = RoomDataDTO.from_dict(data)

    room = room_data_dto.room
    join_room(room)

    send(f"enter {room} room!!")
    print(f"enter {room} room!!")


@socketio.on('connect')
def connect_request():
    print(f"{request.sid} has connect form chat")
    send(f"{request.sid} has connect form chat")
    pass


@socketio.on('disconnect')
def emit_disconnect():
    print(f"{request.sid} has disconnect form chat")
    send(f"{request.sid} goodbye!!")
    pass
