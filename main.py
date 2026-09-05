from models.research import Research
from services.ai_service import ai_agent
from utils.file_handler import saving, load_research

print("~" * 50)

print("         WELCOME TO RESEARCH ASSISTANT         ")

print("~" * 50)

while True:
    print("\n1. Start Research")
    print("2. View Saved Research")
    print("3. Exit")
    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        question = input("\nEnter Topic: ").strip()

        while question == "":
            print("Please enter a valid research topic.")
            question = input("Enter Topic: ").strip()

        r1 = Research(question) 
        result = ai_agent(question) 
        if result is None: 
            print("Research could not be generated. Please try again.") 
        else: 
            r1.summary = result["summary"] 
            r1.sources = result["sources"] 
            saving(r1) 
            print(r1.summary)

    elif choice == "2":
        report = load_research("data/reports/research_1.json")

        print("\nTopic:", report["topic"])
        print("\nSummary:")
        print(report["summary"])

        print("\nSources:")
        for source in report["sources"]:
            print(source)

    elif choice == "3":
        print("Thanks for Visiting")
        break

    else:
        print("Invalid choice")