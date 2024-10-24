# Diabetes Food Assessment

## Project Goal
The Diabetes Food Assessment project aims to provide individuals with diabetes an interactive tool to analyze the suitability of various food items. By uploading images of food, users can receive insights on the glycemic index, recommended dietary quantities, and detailed nutritional analysis, helping them make informed dietary choices.

## Features
- **Image Upload**: Users can upload images of food items in JPG or PNG format.
- **Food Analysis**: The application identifies food items and assesses their suitability for individuals with diabetes.
- **Nutritional Insights**: Provides information on the glycemic index and macronutrient breakdown (proteins, carbohydrates, fats).
- **Streamlit UI**: An interactive web interface built with Streamlit for user-friendly interaction.
- **Response Generation**: Utilizes the Gemini model to generate expert recommendations based on uploaded images.

## Project Structure
├── app.py               # Main application file
├── model.py             # Model and logic for processing
├── requirements.txt     # List of dependencies 
├── .gitignore           # Specify files/folders to ignore
├── LICENSE              # License information        
└── README.md            # Project documentation

## Video Output
Watch the project demo here:

## Requirements
To run this project, ensure you have the following dependencies installed:

- `streamlit`
- `google-generativeai`
- `python-dotenv`

You can install the required packages using pip:

```bash
pip install streamlit google-generativeai python-dotenv
```
## Usage 
Clone the repository:
```bash
git clone https://github.com/mrinmoycyber/Diabetes-Food-Assessment.git
```
Navigate to the project directory:
```bash
cd Diabetes-Food-Assessment
```
Create a .env file and add your Gemini API key:
```bash
GEMINI_API_KEY=your_api_key_here
```
Run the Streamlit app:
```bash
streamlit run app.py
```


