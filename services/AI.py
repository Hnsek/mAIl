import os
from google import genai

def get_response(prompt):
    try:
        
        client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

        response = client.models.generate_content(
            model='gemini-2.0-flash-001', contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Erro ao obter resposta: {e}"