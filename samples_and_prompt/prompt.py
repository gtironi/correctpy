### Prompt

code, e = None, None

prompt_template = f'''
I am coding. It is a Python script, and it is not running. It has one or multiple errors. I will give you the code and the traceback. You should correct all the errors that you find, not just the traceback. Correct the errors in the provided Python script without looking at the traceback first, then look at the traceback and see if you have already corrected it. 

Code: 
'{code}'

Traceback: '{e}'

You should begin your answer with the code; there should be no other word before it.

After the code, you should explain, with bullet points the correction you made, in as few words as possible, limited to 200 words.

Example of answer:
```python
print('hello word')
```

- fixed print
-added parentheses
'''