#Project 8: Build a BMI Calculator with Python & Streamlit in Under 6 Minutes!

import streamlit as st

st.title("💪 BMI Calculator")

# Input fields
st.sidebar.header("Enter Your Details:")
height = st.sidebar.number_input("Height (in cm)", min_value=50.0, max_value=300.0, value=170.0)
weight = st.sidebar.number_input("Weight (in kg)", min_value=10.0, max_value=300.0, value=70.0)

# BMI calculation
height_m = height / 100  # convert cm to meters
bmi = weight / (height_m ** 2)

# Display BMI
st.subheader("📊 Your BMI is:")
st.success(f"{bmi:.2f}")

# BMI Category
if bmi < 18.5:
    st.warning("You're underweight.")
elif 18.5 <= bmi < 24.9:
    st.info("You have a normal weight.")
elif 25 <= bmi < 29.9:
    st.warning("You're overweight.")
else:
    st.error("You are obese.")
