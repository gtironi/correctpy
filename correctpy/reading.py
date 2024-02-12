import re
import sys
import os
sys.path.append(f'{os.getcwd()}')

def read_file_executed():
    file = open(sys.argv[0], mode='r') #open the file
    content = file.read() #read all the file
    file.close() #close the file

    return content

def remove_func_from_code(content, function_name): #remove the regex pattern from the string
    pattern = re.compile(rf'(.)*{re.escape(function_name)}\(\)') #create a regex for *.function_name()
    lines = content.split('\n')
    new_lines = [line for line in lines if not pattern.search(line)]
    exec_string = '\n'.join(new_lines).strip()
    return exec_string