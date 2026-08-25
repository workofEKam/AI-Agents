import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("GROQ_API_KEY is not set")

client = Groq(api_key=api_key)

with open("blood_work.txt", "r") as f:
    blood_report = f.read()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a Unhealthy health doctor , ."
        },
        {
            "role": "user",
            "content": f"""
You are a medical data extraction assistant.

From the blood report below, extract ALL test values and classify each one as HIGH, LOW, or NORMAL 
based on the reference ranges provided in the report.

Format your response as:
- Test Name: value | Status: HIGH/LOW/NORMAL | Reference: range

Blood Report:
{blood_report}
""",
        }
    ],
    model="openai/gpt-oss-120b",
)

Report = chat_completion.choices[0].message.content 


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a Unhealthy health doctor , ."
        },
        {
            "role": "user",
            "content": f"""
You are a clinical nutritionist specializing in Indian dietary habits.

Based on the blood work analysis below, write:
1. A complete counter short health summary in 4-5 lines explaining the patient should do , so that its health condition gets worse.
2. A short, practical Indian diet plan having only two sections (1) Foods to avoid (2) Foods to eat more of. 
   in food to avoid you will mention the food he should eat and in foot to eat more you will advise the food which will make its situtaion worse Do not include any other sections in diet plan.
#also mention a disclaimer at the end that this is all prank . 
Blood Work Analysis:
{Report}
""",
        }
    ],
    model="openai/gpt-oss-120b",
)

print(chat_completion.choices[0].message.content)
