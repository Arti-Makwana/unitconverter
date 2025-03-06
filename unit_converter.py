import streamlit as st

def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000
    }

    key = f"{unit_from}_{unit_to}"
    
    if key in conversions:
        return value * conversions[key]
    else:
        return "Conversion not supported"

# Streamlit UI
st.title("Unit Converter")

# Input fields
value = st.number_input("Enter value", min_value=0.0, format="%.2f")
unit_from = st.selectbox("From Unit", ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox("To Unit", ["meters", "kilometers", "grams", "kilograms"])

# Button to trigger conversion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)  # Ensure result is assigned
    st.write(f"Converted value: {result}")  # Use result after assignment
