from models.research import Research
from services.ai_service import ai_agent
from utils.file_handler import saving, load_research, get_saved_reports


print("~" * 50)
print("         WELCOME TO RESEARCH ASSISTANT         ")
print("~" * 50)


def display_report(report):
    print("\n" + "~" * 100)
    print("Topic:", report["topic"])

    print("\nSummary:")
    print(report["summary"])

    print("\nSources:")
    for source in report["sources"]:
        print(source)


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
        reports = get_saved_reports()

        if not reports:
            print("\nNo saved research reports found.")
        else:
            print("\nSaved Research Reports:")

            for number, report_name in enumerate(reports, start=1):
                print(f"{number}. {report_name}")

            ch = input(
                "\nEnter report number or type 'all': "
            ).strip().lower()

            if ch == "all":
                for report_name in reports:
                    report = load_research(
                        f"data/reports/{report_name}"
                    )

                    if report is not None:
                        display_report(report)

            elif ch.isdigit():
                number = int(ch)

                if 1 <= number <= len(reports):
                    report = load_research(
                        f"data/reports/{reports[number - 1]}"
                    )

                    if report is not None:
                        display_report(report)
                else:
                    print("\nInvalid report number.")

            else:
                print("\nInvalid choice.")

    elif choice == "3":
        print("Thanks for Visiting!\n")
        break

    else:
        print("Invalid choice")