from flask_restx import Resource, Namespace
from flask import Flask, jsonify
import requests
import json
router = Namespace('api', description='Semua Endpoint yang digunakan untuk aplikasi ini')

@router.route('/')
class HealthCheck(Resource):
    def get(self):
        ml_api_url = 'https://asia-southeast2-callysta-api.cloudfunctions.net/function-2'
        response = requests.get(ml_api_url)
        try:
            result = response.data()
            return jsonify({'status': 'healthy', 'result': result})
        except json.JSONDecodeError as e:
            return jsonify({'status': 'unhealthy', 'error': str(e)})
