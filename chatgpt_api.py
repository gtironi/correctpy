
import openai
import re
from samples_and_prompt import prompt_template, sample_response

# openai.api_key = "SUA_API_KEY"

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

def extract_python_code(text):
    pattern = r'```python(.*?)```'
    python_code = re.search(pattern, text, re.DOTALL).group(1).strip()
    return python_code
