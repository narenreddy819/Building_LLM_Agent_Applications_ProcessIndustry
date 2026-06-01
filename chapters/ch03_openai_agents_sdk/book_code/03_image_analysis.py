from dotenv import load_dotenv
import os
load_dotenv()
from openai import OpenAI
from base64 import b64encode


from pathlib import Path

image_path = Path(__file__).parent / "plant_inspection.png"

with open(image_path, "rb") as image_file:
    base64_image = b64encode(image_file.read()).decode("utf-8")

client = OpenAI()

response = client.responses.create(model = "gpt-4.1", input=[{"role":"user", "content":[{"type":"input_text", "text":"Is there any indication of pipe leakage in this image?" }, {"type":"input_image","image_url":f"data:image/png;base64,{base64_image}"}]}])

print(response.output_text)
