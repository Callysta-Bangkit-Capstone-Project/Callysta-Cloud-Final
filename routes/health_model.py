from server.extensions import api
from flask_restx import Resource, fields, Namespace
from flask import Flask, jsonify, request


# Define the model for a user
router = Namespace('api', description='Semua Endpoint yang digunakan untuk aplikasi ini')

@router.route('/')
class HealthCheck(Resource):
    def get(self):
        ml_api_url = 'https://asia-southeast1-callysta-api.cloudfunctions.net/function-1'
        response = requests.get(ml_api_url)
        if response.status_code == 200:
            return jsonify({'status': 'healthy'})
        else:
            return jsonify({'status': 'unhealthy'})
