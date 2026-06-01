from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
from pathlib import Path
pdf_path = Path(__file__).parent / "Technical Guide Vibration Issues.pdf"

client = OpenAI()
file = client.files.create(file = open(pdf_path, "rb"), purpose="user_data")

print(f"File ID: {file.id}")