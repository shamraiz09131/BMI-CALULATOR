import streamlit as st

def calculate_bmi(weight, height):
    """Calculate BMI given weight in kg and height in meters."""
    return weight / (height ** 2)

st.title("BMI Calculator")

weight = st.number_input("Enter your weight in kg", min_value=0.0, format="%.2f")
height = st.number_input("Enter your height in meters", min_value=0.0, format="%.2f")

if st.button("Calculate BMI"):
    if height > 0:
        bmi = calculate_bmi(weight, height)
        st.write(f"Your BMI is: {bmi:.2f}")
    else:
        st.write("Please enter a valid height.")