from flask import Flask, request, jsonify
import base64
import cv2
import numpy as np
from keras.models import load_model

app = Flask(__name__)

model = load_model('models/my_model.h5')

@app.route('/api/result2', methods=['POST'])
def convert_image():
    if 'image' not in request.json:
        return 'No image file in the request!', 400

    alphabets = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z'}

    image_data = request.json['image']
    
    image_array = np.frombuffer(base64.b64decode(image_data), np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    resized_image = cv2.resize(image, (200, 240))
    resized_image_copy = resized_image.copy()
    resized_image_copy = cv2.GaussianBlur(resized_image_copy, (7, 7), 0)
    gray_image = cv2.cvtColor(resized_image_copy, cv2.COLOR_BGR2GRAY)
    _, img_thresh = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY_INV)
    final_image = cv2.resize(img_thresh, (28, 28))
    final_image = np.reshape(final_image, (1, 28, 28, 1))

# Make the prediction using the loaded model
    prediction_label = alphabets[np.argmax(model.predict(final_image))] 

    answer = {
        'actual-answer': request.json['actual-answer'],
        'image-answer': prediction_label
    }

    if answer['image-answer'] == answer['actual-answer']:
        response = jsonify(True)
    else:
        response = jsonify(False)

    response.headers['Content-Type'] = 'application/json'
    return response

if __name__ == '__main__':
    app.run(debug=True)
