import json

def saving(research):
    data = {
        "topic": research.topic,
        "created_at": research.created_at,
        "summary": research.summary,
        "sources": research.sources
    }

    with open("data/reports/research.json", "w") as file:
        json.dump(data, file)
        print(data)