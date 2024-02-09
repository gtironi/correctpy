import inspect
import sys
import re

def read_file_executed():
    file = open(sys.argv[0], mode='r') #open the file
    content = file.read() #read all the file
    file.close() #close the file

    return content