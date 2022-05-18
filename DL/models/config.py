from keras.preprocessing.image import image_dataset_from_directory
from keras.callbacks import ModelCheckpoint
import hparams as hp


training_set = image_dataset_from_directory(
    directory='./data/train/',
    image_size=hp.image_size,
    batch_size=hp.batch_size,
    label_mode='categorical',
    shuffle=True)

validation_set = image_dataset_from_directory(
    directory='./data/valid/',
    image_size=hp.image_size,
    batch_size=hp.batch_size,
    label_mode='categorical',
    shuffle=False)

checkpoint_dir = './checkpoints/'
checkpoint_path = checkpoint_dir + 'cp-{epoch:d}-{accuracy:.3f}.ckpt'
cp_callback = ModelCheckpoint(
    filepath=checkpoint_path,
    monitor='accuracy',
    mode='max',
    save_weights_only=True,
    save_best_only=True,
    save_freq=5
)

savings_dir = './savings/'

labels = ['가구류', '고철류', '나무', '도기류', '비닐',
          '스티로폼', '유리병', '의류', '자전거', '전자제품',
          '종이류', '캔류', '페트병', '플라스틱류', '형광등']
