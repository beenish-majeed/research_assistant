from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv("API_KEY")
client = genai.Client(api_key=api_key)


def ai_agent(user_input):
    prompt = f""" You are an expert research assistant. 
    Research the user's topic and return a JSON object with exactly two fields: 

    1. "summary": A clear and informative Markdown response using headings and subheadings.
    2. "sources": A list of relevant and credible source URLs. 
    
    Do not add any text outside the JSON object. 
    User's topic: {user_input} """

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    response_text = interaction.output_text 
    try: 
        result = json.loads(response_text) 
        return result 
    except json.JSONDecodeError: 
        print("Error: Gemini returned an invalid JSON response.") 
        return None
