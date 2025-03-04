from flask import Flask, request, jsonify
import numpy as np
from flask_cors import CORS
import tensorflow as tf
from PIL import Image
import io
import gc
import os

# Configure TensorFlow to use memory growth
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print(f"GPU memory config error: {e}")

# Limit TensorFlow memory usage
tf.config.threading.set_inter_op_parallelism_threads(1)
tf.config.threading.set_intra_op_parallelism_threads(1)

app = Flask(__name__)
CORS(app)

# Load model only once during initialization
model_path = 'rps_mobilenetv2.h5'
model = tf.keras.models.load_model(model_path, compile=False)  # compile=False saves memory
class_labels = ['paper', 'rock', 'scissors']

# Warm up the model with a dummy prediction to initialize cache
dummy_input = np.zeros((1, 224, 224, 3), dtype=np.float32)
model.predict(dummy_input)
print("Model loaded and ready")

@app.route('/')
def home():
    return "Rock Paper Scissors Prediction API"

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    try:
        # Process image
        img = Image.open(io.BytesIO(file.read()))
        img = img.resize((224, 224))
        img_array = np.array(img, dtype=np.float32)  # Use float32 instead of float64
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0
        
        # Make prediction with reduced precision
        with tf.device('/CPU:0'):  # Force CPU prediction to save memory
            predictions = model.predict(img_array, verbose=0)
        
        predicted_class = class_labels[np.argmax(predictions[0])]
        
        # Manual garbage collection
        del img, img_array, predictions
        gc.collect()
        
        return jsonify({'prediction': predicted_class})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Set environment variable for Flask workers
    os.environ["FLASK_WORKERS"] = "1"
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)