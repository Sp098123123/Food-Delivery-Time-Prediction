
import streamlit as st
import pandas as pd
import pickle

with open("food_delivery_model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(
    page_title="Food Delivery Prediction",
    page_icon="🍔"
)

st.title("🍔 Food Delivery Time Prediction")
st.write("Predict estimated food delivery time using Machine Learning.")

st.divider()

st.subheader("Enter Delivery Details")

distance = st.number_input("Distance (km)", min_value=0.1, value=10.0)

weather = st.selectbox(
    "Weather", ["Clear", "Rainy", "Foggy", "Windy", "Snowy"]
)

traffic = st.selectbox(
    "Traffic Level", ["Low", "Medium", "High"]
)

time_of_day = st.selectbox(
    "Time of Day", ["Morning", "Afternoon", "Evening", "Night"]
)

vehicle = st.selectbox(
    "Vehicle Type", ["Bike", "Scooter", "Car"]
)

preparation = st.number_input(
    "Preparation Time (minutes)", min_value=1, value=15
)

experience = st.number_input(
    "Courier Experience (years)", min_value=0, value=3
)

if st.button("Predict Delivery Time"):

    input_data = pd.DataFrame({
        "Distance_km": [distance],
        "Weather": [weather],
        "Traffic_Level": [traffic],
        "Time_of_Day": [time_of_day],
        "Vehicle_Type": [vehicle],
        "Preparation_Time_min": [preparation],
        "Courier_Experience_yrs": [experience]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated Delivery Time: {prediction:.2f} minutes"
    )

    st.caption("This is an estimated delivery time, not a guarantee.")
