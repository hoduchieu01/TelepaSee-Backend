from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class RequestTTSBroadCastDTO:
    name: str
    text_data: str
    room: str
{"name":"laskdj", "text_data":"Hello world", "room":"1234"}