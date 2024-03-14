import streamlit as st
import numpy as np
from utils import prediction_felin
# from scipy.ndimage.interpolation import zoom
# from streamlit_drawable_canvas import st_canvas

# # Define a function to wrap the model loading
# def load_model_with_hub(path):
#     with hub.KerasLayer.register(): # Register the KerasLayer
#         hub_layer = hub.KerasLayer("https://tfhub.dev/google/imagenet/mobilenet_v2_130_224/classification/5")
#         model = keras.models.load_model(path, custom_objects={'KerasLayer': hub_layer})
#     return model


def main():

    st.title(":tiger: Quel est le félin ? :tiger:")
    st.subheader("Drop l'image dans le champs ci-dessous et découvre a quel famille de félin elle appartient :")

    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        # st.write("filename:", uploaded_file.name)
        # st.write(bytes_data)
        str = prediction_felin(img=bytes_data)
        st.write("Il s'agit d'un ", str,'. Pour en savoir plus, voici un lien vers la page wikipédia :')
        st.write("")

    
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