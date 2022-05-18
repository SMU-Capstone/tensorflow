from keras import Input
from keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from keras.layers import Dense, Dropout, Flatten
from keras.models import Model
from DL.models import hparams as hp


class ImageModel:
    def __init__(self):
        self.base_model = MobileNetV2(input_shape=hp.input_shape,
                                      include_top=False,
                                      weights='imagenet')

    def create_model(self):
        inputs = Input(shape=hp.input_shape)
        x = preprocess_input(inputs)
        x = self.base_model(x, training=False)
        x = Dropout(rate=0.2)(x)
        x = Flatten()(x)
        x = Dense(units=128, activation='relu')(x)
        outputs = Dense(units=15, activation='softmax')(x)
        model = Model(inputs, outputs)
        model.compile(optimizer='adam',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])
        return model
