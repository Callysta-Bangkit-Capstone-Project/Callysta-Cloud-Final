from flask import Flask
from flask_cors import CORS
from .extensions import api, cors
from routes.speechTotext import router as speech_to_text
from routes.input_gambar import router as input_gambar

app = Flask(__name__)
api.init_app(app)
cors.init_app(app)

# Register the inputGambar namespace and resource
api.add_resource(speech_to_text, '/speech-to-text')
api.add_resource(input_gambar, '/inputGambar')

if __name__ == '__main__':
    app.run()
