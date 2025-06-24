import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title("This is the housing prediction model")

with open("best_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

area = st.number_input("Enter the area", min_value=50, step = 1)
bedrooms = st.slider("Enter the number of bedrooms", min_value = 1, max_value = 6 ,step = 1)
furnishingstatus = st.selectbox("Enter the furnitutre status", ["furnished", "unfurnished","semi-furnished"])
bathrooms = st.number_input("Number of Bathrooms", min_value=1, step = 1)
stories = st.number_input("Number of Stories", min_value=1, step = 1)
mainroad = st.selectbox("Main Road Access", ["Yes", "No"])
guestroom = st.selectbox("Guest Room", ["Yes", "No"])
basement = st.selectbox("Basement", ["Yes", "No"])
hotwaterheating = st.selectbox("Hot Water Heating", ["Yes", "No"])
airconditioning = st.selectbox("Air Conditioning", ["Yes", "No"])
parking = st.number_input("Parking Spaces", min_value=0, step = 1)
prefarea = st.selectbox("Preferred Area", ["Yes", "No"])

mainroad = 1 if mainroad == "Yes" else 0
guestroom = 1 if guestroom =="Yes" else 0
basement = 1 if basement =="Yes" else 0
hotwaterheating = 1 if hotwaterheating == "Yes" else 0
airconditioning = 1 if airconditioning == "Yes" else 0
prefarea = 1 if prefarea == "Yes" else 0

map_dict = {"furnished":2, "semi-furnished":1, "unfurnished":0}
furnishingstatus = map_dict[furnishingstatus]

input_array = np.array([[area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnishingstatus]])

input_scaled = scaler.transform(input_array)

if st.button("Predict Price"):
    predicted_price = model.predict(input_scaled)[0]
    st.write(f"The predicted price is: {predicted_price}")


