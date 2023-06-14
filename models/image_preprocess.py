import base64
import numpy as np
import cv2

def preprocess_image(image_data):
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
    return final_image
