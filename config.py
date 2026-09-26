import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

# Application name
APP_NAME = os.getenv("APP_NAME", "EduGenie")