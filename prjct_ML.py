import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Solar Power Prediction")

st.write("Enter input values to predict")

# ---- INPUT FIELDS (change names if needed) ----
doy=st.number_input("doy", value=1.0)
hour=st.number_input("hour",value=0.25)
is_day=st.number_input("is_day",value=0.0)
ghi_W_m2=st.number_input("ghi_W_m2",value=6.0)
clear_sky_ghi_W_m2=st.number_input("clear_sky_ghi_W_m2",value=0.0)
rain_flag=st.number_input("rain_flag",value=0.0)
temperature = st.number_input("Temperature (°C)", value=30.0)
humidity = st.number_input("Humidity (%)", value=50.0)
wind_speed = st.number_input("Wind Speed (m/s)", value=3.0)
solar_irradiance = st.number_input("Solar Irradiance (W/m²)", value=800.0)
cloud_cover = st.number_input("Cloud Cover (%)", value=20.0)

# Create input DataFrame
input_data = pd.DataFrame({
    "doy": [doy],
    "hour": [hour],
    "is_day": [is_day],
    "ghi_W_m2": [ghi_W_m2],
    "clear_sky_ghi_W_m2": [clear_sky_ghi_W_m2],
    "rain_flag": [rain_flag],
    "temperature": [temperature],
    "humidity": [humidity],
    "wind_speed": [wind_speed],
    "solar_irradiance": [solar_irradiance],
    "cloud_cover": [cloud_cover]
})

st.subheader("Input Data")
st.write(input_data)

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Power Output: {prediction[0]}")

