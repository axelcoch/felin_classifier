import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow_hub as hub
from tensorflow_hub import KerasLayer
from PIL import Image
import io

SAVED_MODEL = "saved_models/felin.h5"
MODEL = keras.models.load_model(SAVED_MODEL, custom_objects={'KerasLayer':hub.KerasLayer})
LABELS = ['Acinonyx Jubatus', 'Neofelis Nebulosa', 'Panthera Leo', 'Panthera Onca', 'Panthera Pardus', 'Panthera Tigris', 'Puma Concolor']


def load_image_from_file(image_path):
  """
    Load and preprocess image from a file path.
    
    Args:
      image_path (str): The file path to the image.
    
    Returns:
      image
  """
  image = keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
  image = keras.preprocessing.image.img_to_array(image)
  image = image / 255.0
  image = tf.expand_dims(image, 0)
  return image

def load_image_from_bytes(img_bytes):
  """
    load and preprocess image from bytes

    Args:
      img_bytes (bytes): The bytes of the image.
    
    Returns:
      image
  """
  image = Image.open(io.BytesIO(img_bytes))
  image = image.convert('RGB')
  image = image.resize((224, 224), Image.NEAREST)
  image_array = np.array(image)  # Convertir l'image en un tableau numpy
  image_array = image_array / 255.0  # Normalisation
  image_array = tf.expand_dims(image_array, 0)
  return image_array

def prediction_felin(img, model=MODEL, labels=LABELS, file=False):
  """
    Make a prediction with our model

    Args:
      img
      model
      labels
      file (boolean) : True for path, False for bytes
    
    Returns:
      predicted_label: str.
  """
  if file:
    image = load_image_from_file(img)
  else:
    image = load_image_from_bytes(img)
  predictions = model.predict(image)
  class_index = tf.argmax(predictions[0])
  predicted_label = labels[class_index]
  return predicted_label
