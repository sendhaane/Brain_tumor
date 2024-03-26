from flask import Flask, request, render_template
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import os

app = Flask(__name__)

# Get the absolute path to your application's directory
app_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to model.keras
model_file_path = os.path.join(app_directory, "brain_model4.h5")

# Load the trained Keras model without custom objects
model_keras = tf.keras.models.load_model(model_file_path)


# Specify the directory and model file name
#directory = ''
#model_filename = 'brain_model3.keras'

# Construct the full filepath
#model_filepath = os.path.join(directory, model_filename)
#print(model_filepath)
# Load the Keras model
#model_keras = tf.keras.models.load_model(model_filepath)


output_class = ["HEALTHY","unhealthy"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the uploaded image
    img = request.files['image']

    if img.filename == '':
        return render_template('index.html', error="No file selected")

    img_path = os.path.join(app_directory, "static", "uploaded_image.jpg")
    img.save(img_path)



    test_image = image.load_img(img_path, target_size=(224, 224))
    test_image = image.img_to_array(test_image) / 255
    test_image = np.expand_dims(test_image, axis=0)

    predicted_array = model_keras.predict(test_image)
    predicted_value = output_class[np.argmax(predicted_array)]
    predicted_accuracy = round(np.max(predicted_array) * 100, 2)



    return render_template('index.html', prediction_value=predicted_value,
                               prediction_accuracy=predicted_accuracy,image_path=img_path)


if __name__ == '__main__':
    app.run(debug=True)
