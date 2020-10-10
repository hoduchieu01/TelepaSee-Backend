from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ReplySTTBroadCastDTO:
    name: str
    text_data: str
    pass
