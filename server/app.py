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
model = tf.keras.models.load_model(model_path)

class_labels = ['paper', 'rock', 'scissors']

@app.route('/')
def home():
    return "Home"

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        img = Image.open(io.BytesIO(file.read()))

        img = img.resize((224, 224))

        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  

        predictions = model.predict(img_array)
        predicted_class = class_labels[np.argmax(predictions[0])]

        return jsonify({'prediction': predicted_class})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)