import pandas as pd
import streamlit as st
import pickle


st.title("Linear Regression With Advertising ")
tv = st.number_input("TV Advertising : ")
radio = st.number_input("Radio Advertising : ")
newspaper = st.number_input("News Paper Advertising : ")

# click button than prediction sell values
if st.button("Predict"):
    df = pd.DataFrame(data={"TV":[tv],"radio":[radio],"newspaper":[newspaper]})    
    f = open('advertising_model.pkl','rb')
    model = pickle.load(f)
    pred = model.predict(df)
    st.header(f"Predict Sell Valus are : {pred[0]:.3f}")
