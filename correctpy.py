import sys
from io import StringIO
import inspect
from contextlib import redirect_stdout
import time
from correctpy_modules import read_file_executed, remove_func_from_code, extract_python_code, generate_response

f = StringIO()

def correctpy(slow_mode = True):
    original_code = read_file_executed() #read the file being executed

    function_name = inspect.currentframe().f_code.co_name #see the name of the function
    code_without_function = remove_func_from_code(original_code, function_name) #remove the function from the code, prevent loop

    try:
        with redirect_stdout(f): #redirect the outputs. they are not printed in the terminal
            exec(code_without_function) #execute the code
        print('Your code is correct')
        print('I am running it now...')
        if slow_mode: #delay
            time.sleep(2)
    except Exception as e:
        print(f"Error during execution: {e}")
        print('Trying to autocorrect the code...')
        if slow_mode: #delay
            time.sleep(2)
        answer = generate_response(original_code, e) #use chatgpt to correct the code
        corrected_code = extract_python_code(answer) #extract the code from response
        try:
            with redirect_stdout(f):
                exec(corrected_code) #check it the code is valid

            options = ['overwrite my file', 'create a new file'] #ask you where write the corrected code

            input_message = "Where should I put your corrected code:\n"

            for index, item in enumerate(options):
                input_message += f'{index+1}) {item}\n'

            input_message += 'Your choice: '

            user_input = ''

            while user_input.lower() not in ['1','2']:
                user_input = input(input_message)
            
            if user_input == '1': #overwrite the file with the corrected code
                with open(sys.argv[0], 'w') as file:
                    file.write(corrected_code)

            if user_input == '2':#write a new file with the corrected code
                file_name = input('What should be the file name (without .py)? ')
                with open(f'{file_name}.py', 'w') as file:
                    file.write(corrected_code)

            print('Sucessifuly corrected the code')
        except:
            print('Correctpy:: Automatically correcting the code was not feasible.')
        finally:
            sys.exit()
    pass

correctpy()