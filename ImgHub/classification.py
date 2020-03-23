from django.db import models
from django.urls import reverse
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from tensorflow.python.keras.models import load_model, model_from_json
from tensorflow.python.keras.initializers import glorot_uniform
from keras.utils import CustomObjectScope
from keras.applications.mobilenet import MobileNet
from keras.preprocessing import image
from keras.applications.mobilenet import preprocess_input
from keras.applications import imagenet_utils
from keras import backend as K
import os


class Classification():
    def __init__(self, image):
        self.img = image
        print("from classification.py")

    def predict(self):
        K.reset_uids()
        model = 'model/model_mobilenet.json'
        weights = 'model/weights_mobilenet.h5'
        with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
            with open(model, 'r') as f:
                model = model_from_json(f.read())
                model.load_weights(weights)
        img = load_img(self.img, target_size=(224, 224))
        print("Image loaded")
        x = img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        result = model.predict(x)
        return imagenet_utils.decode_predictions(result)
        # print("Prediction---->")
        # print(result_decode)
        # # for (i, (predId, pred, prob)) in enumerate(result_decode[0]):
        # #     return "{}.-  {}: {:.2f}%".format(i + 1, pred, prob * 100)
        # print("Prediction---->")
        # print(self.predict())

    def save(self, *args, **kwargs):
        self.prediction = self.predict()
        super().save(*args, **kwargs)
