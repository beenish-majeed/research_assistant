from models.research import Research
from services.ai_service import ai_agent

print("~" * 50)

print("         WELCOME TO RESEARCH ASSISTANT         ")

print("~" * 50)

question = input("Enter Topic: ").strip()

while question == "":
    print("Please enter a valid research topic.")
    question = input("Enter Topic: ").strip()

r1 = Research(question)
r1.summary = ai_agent(question)
print(r1.summary)