from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import tensorflow as tf

# Load your machine learning model
# Replace this with your own model loading code
def load_model():
    # Example code to load a pre-trained model using TensorFlow
    model = tf.keras.models.load_model('your_model_path')
    return model

# Perform image classification/prediction
# Replace this with your own prediction code
def predict_image(model, image):
    # Example code to preprocess the image and make a prediction
    # You'll need to modify this based on your model's requirements
    image = image.resize((224, 224))  # Resize image to the required dimensions
    image = np.array(image) / 255.0  # Normalize pixel values between 0 and 1
    image = np.expand_dims(image, axis=0)  # Add a batch dimension
    prediction = model.predict(image)
    
@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'})

    image = request.files['image']
    try:
        img = Image.open(image)
        predicted_class = predict_image(model, img)
        result = 'True' if predicted_class == 1 else 'False'
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()
