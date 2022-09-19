from PIL import Image, UnidentifiedImageError
from flask import Flask, request, render_template, jsonify
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import numpy as np
import time
import config


def transform_image(file):
    image_size = (224, 224)
    image = Image.open(file)
    image = image.convert("RGB")
    image = image.resize(image_size)
    image_nparray = img_to_array(image)
    input_batch = np.array([image_nparray])
    return input_batch


def predict_image(input_batch):
    labels = ['고철(캔)', '유리병', '일반쓰레기(종이, 비닐)', '플라스틱(페트병)']
    prediction = model.predict(input_batch)
    prediction = np.argmax(prediction)
    prediction_name = labels[prediction]
    return prediction_name


app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)


@app.get('/')
@app.get('/index/')
def index():
    return render_template('upload_image.html')


@app.post('/predict/')
def predict():
    label = '지원하지 않는 파일 형식입니다.'
    file = request.files['file']
    try:
        input_batch = transform_image(file)
        start_time = time.time()
        label = predict_image(input_batch)
        end_time = time.time()
        app.logger.info(end_time - start_time)
    except UnidentifiedImageError:
        pass
    finally:
        return jsonify({'predicted_label': label})


if __name__ == '__main__':
    model = load_model('./DL/models/savings/trash_model.h5')
    app.run(host='0.0.0.0', port=9999)
