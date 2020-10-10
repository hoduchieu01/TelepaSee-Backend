from flask import Blueprint

tts_blueprint = Blueprint('tts', __name__)
stt_blueprint = Blueprint('tts', __name__)

from . import tts_controller
from . import stt_controller