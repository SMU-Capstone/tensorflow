import tensorflow as tf
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import numpy as np
import os
from model import ImageModel
import hparams as hp
import config


class ImageModelClassifier(ImageModel):
    def __init__(self):
        super().__init__()
        self.model = super().create_model()
        self.labels = config.labels

    def create_model_by_load_model(self, path):
        self.model = load_model(path)

    def update_weight_by_load_weights(self, path):
        latest = tf.train.latest_checkpoint(path)
        self.model.load_weights(latest)

    def train(self,
              training_set=config.training_set,
              training_epochs=hp.training_epochs,
              validation_set=config.validation_set,
              checkpoint_dir=config.checkpoint_dir,
              callbacks=config.cp_callback):

        if not os.path.exists(checkpoint_dir):
            os.mkdir(checkpoint_dir)

        self.model.fit(training_set,
                       epochs=training_epochs,
                       validation_data=validation_set,
                       verbose=1,
                       callbacks=[callbacks])

    def save_model(self, checkpoint_dir=config.checkpoint_dir):
        self.model.save(checkpoint_dir + 'trash_model.h5')

    def predict(self, path):
        image = load_img(path, target_size=hp.image_size)
        image_nparray = img_to_array(image)
        input_batch = np.array([image_nparray])
        prediction = self.model.predict(input_batch)
        prediction = np.argmax(prediction)
        prediction_name = self.labels[prediction]
        print(prediction_name)

    def evaluate(self, validation_set=config.validation_set):
        return self.model.evaluate(validation_set, verbose=1)
