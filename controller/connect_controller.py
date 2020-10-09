from flask import request
from flask_socketio import join_room, leave_room, send, rooms, emit

from controller import socketio


@socketio.on('leave')
def leave_room_handler(data):
    if 'room' not in data:
        send("Room parameter is not exsist. require room infomation")
        print("접속자의 room 정보가 없어서 저장하지 못했습니다.")
        return

    room = data['room']
    send(f"leave {room}")
    leave_room(room)


@socketio.on('join')
def recv_message(data):
    if 'room' not in data:
        send("Room parameter is not exsist. require room infomation")
        print("접속자의 room 정보가 없어서 저장하지 못했습니다.")
        return

    room = data['room']
    join_room(room)
    send(f"enter {room} room!!")
    print(f"enter {room} room!!")


@socketio.on('echo')
def echo(data):
    send(f"data")

@socketio.on('connect')
def connect_request():
    print(f"{request.sid} has connect form chat")
    send(f"{request.sid} has connect form chat"))


@socketio.on('disconnect')
def emit_disconnect():
    print(f"{request.sid} has disconnect form chat")
    send(f"{request.sid} goodbye!!")
    pass
