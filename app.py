import streamlit as st
import pandas as pd
import numpy as np  # Import numpy for data manipulation

# Load the model from the pickle file
classifier = pd.read_pickle('random_forest_model.pkl')

def prediction(SPX, USO, SLV, EUR):
    # Convert input strings to numeric values
    SPX = float(SPX)
    USO = float(USO)
    SLV = float(SLV)
    EUR = float(EUR)

    # Predict using the loaded model
    prediction = classifier.predict([[SPX, USO, SLV, EUR]])
    return prediction

def main():
    # Giving the webpage a title
    st.title("Gold Price Prediction")

    # Text inputs for user input
    SPX = st.text_input("SPX: Standard & Poor's 500 Index")
    USO = st.text_input("USO: United States Oil Fund")
    SLV = st.text_input("SLV: iShares Silver Trust")
    EUR = st.text_input("EUR/USD: Euro to US Dollar exchange rate")
    result = ""

    # Convert empty strings to NaN and replace with default value 0
    SPX = float(SPX) if SPX else 0.0
    USO = float(USO) if USO else 0.0
    SLV = float(SLV) if SLV else 0.0
    EUR = float(EUR) if EUR else 0.0

    if st.button("Predict"):
        result = prediction(SPX, USO, SLV, EUR)
    st.success('The output is {}'.format(result))

if __name__=='__main__':
    main()
