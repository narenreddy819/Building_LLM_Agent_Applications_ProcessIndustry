import os
from openai import OpenAI
from dotenv import load_dotenv

# load_dotenv("D:/Narender/Building_LLM_Agent_Applications_ProcessIndustry/.env")
# load_dotenv()

# # print(os.getenv("OPENAI_API_KEY"))

# client = OpenAI()

# response = client.responses.create(model= "gpt-5.2", input = "What is the boiling point of water at sea level?")

# print(response.output_text)

# from ollama import chat

# response = chat(
#     model="mistral",
#     messages=[
#         {"role": "user", "content": "What is the boiling point of water at sea level?"}
#     ]
# )

# print(response["message"]["content"])

from ollama import chat

response = chat(
    model="mistral",
    messages=[
        {
            "role": "system",
            "content": "You are a senior process engineer specializing in distillation and NGL recovery. You answer questions in a concise manner."
        },
        {
            "role": "user",
            "content": "What is the primary function of a de-ethanizer column in an NGL plant, and how does it impact downstream propane purity?"
        }
    ]
)

print(response["message"]["content"])
print("Model:", response["model"])
print("Done:", response["done"])
print("Prompt tokens:", response["prompt_eval_count"])
print("Response tokens:", response["eval_count"])
print("Answer:")
