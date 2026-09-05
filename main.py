from models.research import Research
from services.ai_service import ai_agent
from utils.file_handler import saving

print("~" * 50)

print("         WELCOME TO RESEARCH ASSISTANT         ")

print("~" * 50)

question = input("\nEnter Topic: ").strip()

while question == "":
    print("Please enter a valid research topic.")
    question = input("Enter Topic: ").strip()

r1 = Research(question) 
result = ai_agent(question) 
r1.summary = result["summary"] 
r1.sources = result["sources"] 
saving(r1) 
print(r1.summary)