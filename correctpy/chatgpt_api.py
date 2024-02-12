
import openai
import re
import os
import sys
sys.path.append(f'{os.getcwd()}')

from samples_and_prompt import prompt_template, sample_response

OPENAI_API = "YOUR_API_KEY" #define your API KEY here

client = openai.OpenAI(api_key= OPENAI_API) 

def generate_response(code, error): #use the ChatGPT API to produce the response
    prompt = prompt_from_template(code, error) #define the prompt from template
    try: 
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",  
        messages=[{"role": "system", "content": prompt}],
        max_tokens=2000,  
        temperature=0.2).choices[0].message.content #interact with the API
    except:
        if sys.argv[0] == f'{os.getcwd()}/sample_file.py': #check if the file executed is the sample_file
            response = sample_response #return the sample_response
        else:
            print('You must defined your API KEY')
            sys.exit(0) #stop the execution

    return response

def extract_python_code(text): #use regex to extract the python code from chatgpt response
    pattern = r'```python(.*?)```' #set the pattern to be searched
    python_code = re.search(pattern, text, re.DOTALL).group(1).strip() #search in multiple lines
    return python_code

def prompt_from_template(code, error): #create the prompt from template
     return f'''{prompt_template[0]} {code}

Traceback: {error}

{prompt_template[1]}
'''