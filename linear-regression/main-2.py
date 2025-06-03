import pandas as pd
import streamlit as st
import pickle


st.title("Linear Regression With insurance ")
Quotes = st.number_input("Quotes  : ")

# click button than prediction sell values
if st.button("Predict"):
    df = pd.DataFrame(data={"Quotes":[Quotes]})    
    f = open('insurance_model.pkl','rb')
    model = pickle.load(f)
    pred = model.predict(df)
    st.header(f"Predict TV advert are : {pred[0]:.2f}")

