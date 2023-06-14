from flask import Flask, request, jsonify
from flask_restx import Resource, fields, Namespace
from models.image_preprocess import preprocess_image
from app.extensions import api
from keras.models import load_model
import numpy as np
import string

# Define the model for a user
router = Namespace('api', description='Semua Endpoint yang digunakan untuk aplikasi ini')

@router.route('/')
class InputGambar(Resource):
    @api.doc(responses={200: 'Success', 400: 'Invalid Request'})
    @api.expect(api.model('InputGambar', {'image': fields.String(required=True), 'actual-answer': fields.String(required=True)}))
    def post(self):
        # Load the model
        model = load_model('models/my_model.h5')
      
        if 'image' not in request.json:
            return 'No image file in the request!', 400
          
        # Preprocess the image
        image_data = request.json['image']
        final_image = preprocess_image(image_data)

        # Make the prediction using the loaded model
        prediction_index = np.argmax(model.predict(final_image))
        alphabets = string.ascii_uppercase
        prediction_label = alphabets[prediction_index]

        answer = {
            'actual-answer': request.json['actual-answer'],
            'image-answer': prediction_label
        }

        if answer['image-answer'] == answer['actual-answer']:
             response = {'result': True}
        else:
             response = {'result': False}

        return response

