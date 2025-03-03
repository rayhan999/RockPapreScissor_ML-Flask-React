from flask import Flask, request, jsonify
import numpy as np
from flask_cors import CORS
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import io
import os

app = Flask(__name__)
CORS(app)

model_path = 'rps_mobilenetv2.h5'
# model_path = '/content/drive/MyDrive/fruit_classifier.h5'  # Update this path
model = tf.keras.models.load_model(model_path)

# Class labels
class_labels = ['paper', 'rock', 'scissors']

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        # Read the image file
        img = Image.open(io.BytesIO(file.read()))

        # Resize the image to 224x224 (MobileNetV2 input size)
        img = img.resize((224, 224))

        # Convert the image to a numpy array and preprocess it
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # Normalize pixel values

        # Make prediction
        predictions = model.predict(img_array)
        predicted_class = class_labels[np.argmax(predictions[0])]

        # Return the prediction
        return jsonify({'prediction': predicted_class})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)