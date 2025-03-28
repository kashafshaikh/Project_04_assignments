import streamlit as st

# BMI calculation function
def calculate_bmi(weight, height):
    if height > 0:
        bmi = weight / ((height / 100) ** 2)  # Height ko cm se meter mein convert karna
        return round(bmi, 2)
    return None

# BMI category function
def bmi_category(bmi):
    if bmi is None:
        return "Invalid Input"
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Streamlit UI
st.title("💪 BMI Calculator")

# User input
weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1, format="%.1f")
height = st.number_input("Enter your height (cm):", min_value=1.0, step=0.1, format="%.1f")

if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    
    if bmi is not None:
        st.success(f"Your BMI is: {bmi}")
        st.info(f"Category: {category}")
    else:
        st.error("Invalid height input! Please enter a valid height.")

