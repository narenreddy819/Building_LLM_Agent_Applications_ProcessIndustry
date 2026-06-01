from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-5.2",
    input=[
        {
            "role": "developer",
            "content": (
                "You are a senior process engineer specializing in "
                "distillation and NGL recovery. "
                "You answer questions in a concise manner."
            )
        },
        {
            "role": "user",
            "content": (
                "What is the primary function of a de-ethanizer column "
                "in an NGL plant, and how does it impact downstream "
                "propane purity?"
            )
        }
    ],
    stream=True
)

for event in response:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)

print()