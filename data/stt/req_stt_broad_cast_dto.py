from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class RequestSTTBroadCastDTO:
    name: str
    voice_data: str
    room: str
