import json
import os


def saving(research):
    data = {
        "topic": research.topic,
        "created_at": str(research.created_at),
        "summary": research.summary,
        "sources": research.sources
    }

    number = 1

    while os.path.exists(f"data/reports/research_{number}.json"):
        number += 1

    filename = f"data/reports/research_{number}.json"

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_research(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                return data

        except json.JSONDecodeError:
            print("Invalid JSON format in the research report.")
            return None

    else:
        print("No saved research report found.")
        return None