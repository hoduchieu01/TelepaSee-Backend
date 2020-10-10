from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ReplyTTSBroadCastDTO:
    name: str
    voice_data: str
    pass
