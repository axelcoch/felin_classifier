import streamlit as st
import numpy as np
from utils import prediction_felin
from data import dict_felin

def main():

    st.title(":tiger: Quel est le félin ? :tiger:")
    st.subheader("Drop l'image dans le champs ci-dessous et découvre a quel famille de félin elle appartient :")

    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)

    if not uploaded_files:
        st.write("")
    else:
        bytes_data = uploaded_files[-1].read()
        str = prediction_felin(img=bytes_data)
        st.write("Il s'agit d'un ", str,'. Pour en savoir plus sur cette espèce, voici un lien :',dict_felin[str][0])
        st.image(dict_felin[str][1])
    
if __name__ == "__main__":
    main()