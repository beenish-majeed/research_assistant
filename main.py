print("~" * 50)

print("         WELCOME TO RESEARCH ASSISTANT         ")

print("~" * 50)

question = input("Enter Topic: ").strip()

while question == "":
    print("Please enter a valid research topic.")
    question = input("Enter Topic: ").strip()
