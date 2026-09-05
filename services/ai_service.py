from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
client = genai.Client(api_key=api_key)


def ai_agent(user_input):
    prompt = f"""
You are an expert research assistant. Provide a clear, informative answer about the user's topic.
Organize the response with meaningful headings and subheadings, and explain each section concisely.

User's topic:
{user_input}
"""

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    return interaction.output_text