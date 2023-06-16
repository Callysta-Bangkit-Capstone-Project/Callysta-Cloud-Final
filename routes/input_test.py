from flask import Flask, request, jsonify
from flask_restx import Resource, fields, Namespace
from server.extensions import api
import requests
import string

# Define the model for a user
router = Namespace('api', description='Semua Endpoint yang digunakan untuk aplikasi ini')

# Define the model for the Flask-RESTX API
model = api.model('InputGambar', {
    'image': fields.String(required=True),
    'actual-answer': fields.String(required=True)
})

@router.route('/')
class InputGambarController(Resource):
    @api.doc(responses={200: 'Success', 400: 'Invalid Request'})
    @api.expect(model)
    def post(self):
        ml_api_url = 'https://asia-southeast2-callysta-api.cloudfunctions.net/function-2'
        payload = {
            "image": request.json['image'],
            "actual-answer": request.json['actual-answer']
        }
        
        result = requests.post(ml_api_url, json=payload)
        
        return result.json()

