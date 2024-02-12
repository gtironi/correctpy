
import openai
import sys
import os
import re
from samples_and_prompt import prompt_template, sample_response

OPENAI_API = "YOUR_API_KEY"

client = openai.OpenAI(api_key= OPENAI_API)

def generate_response(code, error):
    prompt = prompt_from_template(code, error)
    try:
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",  
        messages=[{"role": "system", "content": prompt}],
        max_tokens=2000,  
        temperature=0.2).choices[0].message.content
    except:
        if sys.argv[0] == f'{os.getcwd()}/sample_file.py':
            response = sample_response
        else:
            print('You must defined your API KEY')
            sys.exit(0)

    return response

def extract_python_code(text):
    pattern = r'```python(.*?)```'
    python_code = re.search(pattern, text, re.DOTALL).group(1).strip()
    return python_code

def prompt_from_template(code, error):
     return f'''{prompt_template[0]} {code}

Traceback: {error}

{prompt_template[1]}
'''