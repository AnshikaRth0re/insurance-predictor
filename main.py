
import streamlit as st
import pickle
import pandas as pd

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

st.title("Insurance Premium Predictor")

# Inputs
age = st.number_input("Age", min_value=1, max_value=120)
weight = st.number_input("Weight (kg)", min_value=1.0)
height = st.number_input("Height (meters)", min_value=0.5, max_value=2.5)
income_lpa = st.number_input("Income (LPA)", min_value=0.0)
smoker = st.checkbox("Smoker")
city = st.text_input("City")
occupation = st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job',
     'business_owner', 'unemployed', 'private_job']
)

# Feature engineering
if st.button("Predict"):

    bmi = weight / (height ** 2)

    if smoker and bmi > 30:
        lifestyle_risk = "high"
    elif smoker or bmi > 27:
        lifestyle_risk = "medium"
    else:
        lifestyle_risk = "low"

    if age < 25:
        age_group = "young"
    elif age < 45:
        age_group = "adult"
    elif age < 60:
        age_group = "middle_aged"
    else:
        age_group = "senior"

    if city in tier_1_cities:
        city_tier = 1
    elif city in tier_2_cities:
        city_tier = 2
    else:
        city_tier = 3

    input_df = pd.DataFrame([{
        'bmi': bmi,
        'age_group': age_group,
        'lifestyle_risk': lifestyle_risk,
        'city_tier': city_tier,
        'income_lpa': income_lpa,
        'occupation': occupation
    }])

    prediction = model.predict(input_df)[0]

    st.success(f"Predicted Category: {prediction}")