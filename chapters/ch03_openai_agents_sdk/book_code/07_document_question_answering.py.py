from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# Step 1: Upload PDF
file = client.files.create(
    file=open("Technical Guide Vibration Issues.pdf", "rb"),
    purpose="user_data"
)

print(f"Uploaded File ID: {file.id}")

# Step 2: Ask a question about the document
response = client.responses.create(
    model="gpt-5-nano",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_file",
                    "file_id": "CghNu3zFRNTtNdP1v5Wak4"
                },
                {
                    "type": "input_text",
                    "text": "Tell concisely: What are the main topics covered in this document?"
                }
            ]
        }
    ]
)

# Step 3: Print answer
print("\nDocument Summary:")
print(response.output_text)