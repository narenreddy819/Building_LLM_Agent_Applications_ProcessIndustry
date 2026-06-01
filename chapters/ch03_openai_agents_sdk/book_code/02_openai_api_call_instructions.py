import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(model= "gpt-5.2", input = [{"role": "developer", "content":"You are a senior process engineer specializing in distillation and NGL recovery. You answer questions in a concise manner."}, {"role": "user",
"content": "What is the primary function of a de-ethanizer column in an NGL plant, and how does it impact downstream propane purity?"}],max_output_tokens=20, reasoning={"effort":"low"})

print(response.output_text)


##################

# from pprint import pprint # display complex data structures like dictionaries in a well-formatted way
# pprint(response.model_dump())

#####################################
# obtain specific items from the response object
print("Status:", response.status)
print("Reason for incompleteness:", response.incomplete_details.reason)
print("Total tokens used:", response.usage.total_tokens)
print("Output text:", response.output[0].content[0].text) # same as response.output_text here