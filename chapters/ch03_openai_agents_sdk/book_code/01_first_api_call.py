import os
from openai import OpenAI
from dotenv import load_dotenv

# load_dotenv("D:/Narender/Building_LLM_Agent_Applications_ProcessIndustry/.env")
load_dotenv()

# print(os.getenv("OPENAI_API_KEY"))

client = OpenAI()

response = client.responses.create(model= "gpt-5.2", input = "What is the boiling point of water at sea level?")

print(response.output_text)
