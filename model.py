
import google.generativeai as genai
from dotenv import load_dotenv
from pathlib import Path
import os

# Load environment variables from .env file
load_dotenv()

class GeminiModel:
    def __init__(self):
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("API key not found. Make sure it's set in the .env file.")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config={
                "temperature": 0.4,
                "top_p": 1,
                "top_k": 32,
                "max_output_tokens": 4096,
            },
            safety_settings=[
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            ]
        )

    def input_image_setup(self, file_loc):
        if not (img := Path(file_loc)).exists():
            raise FileNotFoundError(f"Could not find image: {img}")

        image_parts = [{
            "mime_type": "image/jpeg",
            "data": Path(file_loc).read_bytes()
        }]
        return image_parts

    def clean_output(self, response_text):
        return response_text.replace("*", "").strip()

    def generate_gemini_response(self, input_prompt, image_loc):
        image_prompt = self.input_image_setup(image_loc)
        prompt_parts = [input_prompt, image_prompt[0]]
        response = self.model.generate_content(prompt_parts)
        cleaned_response = self.clean_output(response.text)
        return cleaned_response
