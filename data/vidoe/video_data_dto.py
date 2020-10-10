from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class VideoDataDTO:
    name: str
    video_data: str
    sound_data: str
    room: str