
import openai
import re
from samples_and_prompt import prompt_template, sample_response

def generate_response(code, error):
    code = code
    e = error
    prompt = prompt_template
    if openai.api_key is not None:
        response = openai.Completion.create(
        engine="davinci-codex",  
        prompt=prompt,
        max_tokens=150,  
        temperature=0.2,
        stop=None).choices[0].text.split()
    else:
        response = sample_response

    return response

