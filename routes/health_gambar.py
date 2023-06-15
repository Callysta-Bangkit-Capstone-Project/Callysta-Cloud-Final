from server.extensions import api
from keras.models import load_model
from flask_restx import Resource, fields, Namespace
from flask import Flask, jsonify, request


# Define the model for a user
router = Namespace('api', description='Semua Endpoint yang digunakan untuk aplikasi ini')

@router.route('/')
class ModelHealth(Resource):
    def get(self):
        try:
            # Load the model
            model = load_model('models/my_model.h5')
            
            # Check if the model is loaded successfully
            if model:
                return {'status': 'Model is healthy'}
            else:
                return {'status': 'Model is not loaded'}, 500
        except Exception as e:
            return {'status': 'An error occurred', 'error': str(e)}, 500
