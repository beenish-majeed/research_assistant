from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv("API_KEY")
client = genai.Client(api_key=api_key)


def ai_agent(user_input):
    prompt = f"""
    You are an expert research assistant. Research the user's topic and provide a clear, concise, and informative response.

    Requirements:
    - Use clear headings and subheadings.
    - Explain important points briefly.
    - Include relevant and credible sources.
    - Format the response in Markdown.
    - End with a "Sources" section containing the source URLs.

    User's topic:
    {user_input}
    """

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    response_text = interaction.output_text 
    return json.loads(response_text)
