from pathlib import Path
import streamlit as st
import pandas as pd
import pickle
st.set_page_config(
    page_title="Food Delivery Prediction",
    page_icon="🍔"
)

BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / "food_delivery_model.pkl", "rb") as file:
    model = pickle.load(file)
st.markdown("""
<style>
.stApp {
    background:
        linear-gradient(
            rgba(20, 20, 20, 0.35),
            rgba(20, 20, 20, 0.45)
        ),
        url("https://raw.githubusercontent.com/Sp098123123/Food-Delivery-Time-Prediction/main/Food_Delivery_Prediction/delivery_bg.jpg");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    background-repeat: no-repeat;
}
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

h1, h2, h3 {
    color: #392719;
}

p, label {
    color: #594638;
}

.stButton > button {
    background-color: #F07836;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #D95D20;
    color: white;
}

div[data-testid="stMetric"] {
    background-color: white;
    border: 1px solid #F0DFD0;
    border-radius: 14px;
    padding: 18px;
}

section[data-testid="stSidebar"] {
    background-color: #FCEBDD;
}
div[data-testid="stAlert"] {
    background-color: #14532D !important;
    color: white !important;
    border: 2px solid #86EFAC !important;
    border-radius: 12px !important;
}

div[data-testid="stAlert"] p {
    color: white !important;
    font-size: 20px !important;
    font-weight: 700 !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<h1 style="text-align:center; color:#E66B2E;">
🍔 Food Delivery Time Predictor
</h1>
<p style="text-align:center; font-size:17px; color:#755B48;">
Smart delivery time estimation powered by Machine Learning
</p>
""", unsafe_allow_html=True)
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
