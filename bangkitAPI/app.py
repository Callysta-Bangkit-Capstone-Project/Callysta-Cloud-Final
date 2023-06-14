from flask import Flask, request, jsonify
import base64
import pickle
import cv2
import numpy as np
from keras.models import load_model

app = Flask(__name__)

model = load_model('models/my_model.h5')

@app.route('/api/result', methods=['POST'])
def convert_image():
    if 'image' not in request.json:
        return 'No image file in the request!', 400

    image_data = request.json['image']
    
    image_array = np.frombuffer(base64.b64decode(image_data), np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_resized = cv2.resize(image_gray, (28, 28))

    image_resized = image_resized.astype(np.float32) / 255.0  # Normalize the image between 0 and 1
    image_resized = np.expand_dims(image_resized, axis=0)  # Add a batch dimension
    image_resized = np.expand_dims(image_resized, axis=-1)  # Add a channel dimension

    predictions = model.predict(image_resized)

    predicted_label_index = np.argmax(predictions)
    predicted_label = chr(ord('A') + predicted_label_index)

    answer = {
        'actual-answer': request.json['actual-answer'],
        'image-answer': predicted_label
    }

    if answer['image-answer'] == answer['actual-answer']:
        return jsonify(True)
    else:
        return jsonify(False)


if __name__ == '__main__':
    app.run(debug=True)
