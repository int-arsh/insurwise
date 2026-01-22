import requests
import streamlit as st

# Use environment variable for API URL, with fallback to localhost for local development
import os

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/predict")

st.title("Insurance Premium Category Predictor")
st.markdown("Enter your details below:")

# Input fields
age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("Are you a smoker?", options=[True, False])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox(
    "Occupation",
    [
        "retired",
        "freelancer",
        "student",
        "government_job",
        "business_owner",
        "unemployed",
        "private_job",
    ],
)

if st.button("Predict Premium Category"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation,
    }

    try:
        response = requests.post(API_URL, json=input_data, timeout=10)
        result = response.json()

        if response.status_code == 200 and "predicted_category" in result:
            prediction = result["predicted_category"]
            st.success(
                f"Predicted Insurance Premium Category: **{prediction['predicted_category']}**"
            )
            st.write("Confidence:", prediction["confidence"])
            st.write("Class Probabilities:")
            st.json(prediction["class_probabilities"])

        else:
            st.error(f"API Error: {response.status_code}")
            st.write(result)

    except requests.exceptions.Timeout:
        st.error("Request timed out. The API server is taking too long to respond.")
    except requests.exceptions.ConnectionError:
        st.error(f"Could not connect to the API server at {API_URL}. Make sure it's running and accessible.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")