import streamlit as st
import numpy as np
import pickle

# loading the model
loaded_model = pickle.load(open("saved_model/wine_trained_model.sav", 'rb'))

def wine_quality_prediction(input_list):
    input_data_arr = np.asarray([input_list])

    prediction = loaded_model.predict(input_data_arr)
    if prediction[0] == 0:
        return 'Bad Quality'
    else:
        return 'Good Quality'

def main():
    
    # tite for the app
    st.set_page_config(page_title="Wine Quality Prediction", page_icon="🍷", layout="centered")
    st.title("🍷 Wine Quality Prediction")

    # inputs from user
    form = st.form(key="annotation")

    with form:
        cols = st.columns((1, 1))
        fixed_acidity = cols[0].text_input("Fixed Acidity:")
        volatile_acidity = cols[1].text_input("Volatile Acidity:")
        citric_acid = cols[0].text_input("Citric Acid:")
        residual_sugar = cols[1].text_input("Residual Sugar:")
        chlorides = cols[0].text_input("Chlorides:")
        free_sulfur_dioxide = cols[1].text_input("Free Sulfur Dioxide:")
        total_sulfur_dioxide = cols[0].text_input("Total Sulfur Dioxide:")
        density = cols[1].text_input("Density:")
        pH = cols[0].text_input("pH:")
        sulphates = cols[1].text_input("Sulphates:")
        alcohol = cols[0].text_input("Alcohol:")
        submitted = st.form_submit_button(label="Submit")
    
    quality=""

    if submitted:
        quality = wine_quality_prediction([fixed_acidity, volatile_acidity, citric_acid,\
                                       residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide,\
                                       density, pH, sulphates, alcohol])
        st.success(quality)

if __name__ == "__main__":
    main()