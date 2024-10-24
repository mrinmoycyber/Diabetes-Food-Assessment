import streamlit as st
from model import GeminiModel
import tempfile

# Initialize the GeminiModel class (API key is loaded automatically from .env)
model = GeminiModel()

input_prompt = """
    As an expert specializing in assessing the suitability of fruits and foods for individuals with diabetes, your task involves analyzing input images featuring various food items. Your first objective is to identify the type of fruit or food present in the image. Subsequently, determine the glycemic index of the identified item and provide recommendations on whether individuals with diabetes can include the detected food in their diet. Specify the recommended quantity for consumption if the food is deemed suitable. Additionally, perform a nutritional content analysis, breaking down the estimated macronutrients (proteins, carbohydrates, fats) in the food.
"""

# Streamlit App UI
st.title("Diabetes Food Assessment")

# File uploader in Streamlit
uploaded_file = st.file_uploader("Upload an Image of the Food", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Display the uploaded image directly in Streamlit
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Create a temporary file and write the uploaded image to it
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        image_path = temp_file.name

    # Generate response using the model
    if st.button("Analyze Image"):
        try:
            response = model.generate_gemini_response(input_prompt, image_path)
            st.write("Model Response:")
            st.write(response)
        except Exception as e:
            st.error(f"Error: {e}")
