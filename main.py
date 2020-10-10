from flask import Flask

import controller

app = Flask(__name__)
app.register_blueprint(controller.tts_blueprint, url_prefix="/tts")

if __name__ == '__main__':
    app.run('0.0.0.0', 8080, use_reloader=False)