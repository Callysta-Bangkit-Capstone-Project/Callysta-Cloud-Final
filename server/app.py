from dotenv import load_dotenv
from flask import Flask
from flask_restx import Api, Resource, fields, Namespace
from server.extensions import api, cors
from routes.speech_Totext import router as speech_to_text
from routes.input_test import router as input_gambar
from routes.health_model import router as health_check

load_dotenv()

app = Flask(__name__)
api.init_app(app)
cors.init_app(app)

# Register the inputGambar namespace and resource
api.add_namespace(speech_to_text, path='/ml/speech-to-text')
api.add_namespace(input_gambar, path='/ml/inputGambar')
api.add_namespace(health_check, path='/ml/healthModel')

