import numpy as np
import tensorflow as tf
from tensorflow import keras


# from keras.preprocessing.image import ImageDataGenerator
# from keras.applications import NASNetMobile
# from keras.utils import to_categorical
# from tensorflow.keras import layers
# from tensorflow.keras.models import Sequential

def load_image(image_path):
  image = keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
  image = keras.preprocessing.image.img_to_array(image)
  image = image / 255.0
  image = tf.expand_dims(image, 0)
  return image

def prediction_felin(model, img, labels):
  image = load_image(img)
  predictions = model.predict(image)
  class_index = tf.argmax(predictions[0])
  predicted_label = labels[class_index]
  return predicted_label