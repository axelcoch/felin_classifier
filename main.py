import streamlit as st
# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers
# import tensorflow_hub as hub
import numpy as np

# from scipy.ndimage.interpolation import zoom
# from streamlit_drawable_canvas import st_canvas

# # Define a function to wrap the model loading
# def load_model_with_hub(path):
#     with hub.KerasLayer.register(): # Register the KerasLayer
#         hub_layer = hub.KerasLayer("https://tfhub.dev/google/imagenet/mobilenet_v2_130_224/classification/5")
#         model = keras.models.load_model(path, custom_objects={'KerasLayer': hub_layer})
#     return model


# SAVED_MODEL = "saved_models/felin.h5"
# # MODEL = keras.models.load_model((SAVED_MODEL), custom_objects={'KerasLayer':hub.KerasLayer})
# MODEL = keras.models.load_model(SAVED_MODEL, custom_objects={'KerasLayer': hub.KerasLayer})
# # MODEL = load_model_with_hub(SAVED_MODEL)
# LABELS = ['Acinonyx_Jubatus', 'Neofelis_Nebulosa', 'Panthera_Leo', 'Panthera_Onca', 'Panthera_Pardus', 'Panthera_Tigris', 'Puma_Concolor']


def main():
    st.title("Classification des grands félins")
    st.subheader("Enter your text below:")

    user_input = st.text_area("Your Text:")
    
    # if st.button("Analyze Sentiment"):
    #     result = analyze_sentiment(user_input)
    #     st.write("Sentiment:", result)

# def analyze_sentiment(text):
#     # Your sentiment analysis logic goes here
#     # This could be achieved using various libraries like NLTK, TextBlob, or transformers
#     # For simplicity, let's assume a basic example
#     if "happy" in text.lower():
#         return "Positive"
#     elif "sad" in text.lower():
#         return "Negative"
#     else:
#         return "Neutral"

if __name__ == "__main__":
    main()