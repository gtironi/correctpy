# correctpy


Correctpy is an AI code-writing assistant that automatically corrects some errors in your code. Correctpy is currently in its first version, so it still needs some improvements to be completely functional. 

## Demo 

Here is a video showing how to run *correctpy* using the sample_file.

https://github.com/gtironi/pyerrorhandling/assets/126670916/c21df037-70fa-4d20-9d20-1333b0c32078

## How to use

For now, to run correctpy on your code, you should download this repository, add your Python script to it, and import *correctpy* as follows:

```python
import correctpy
```

## How it works

The Python script provides a seamless solution for correcting code using ChatGPT's API. First, it reads the file being executed, capturing the code that needs correction. Leveraging prompt engineering techniques, the script crafts a structured prompt template to present the code to ChatGPT. Upon receiving the response from the model, the script extracts the corrected code. Depending on user preference, the corrected code can either be saved into a new file or overwrite the original file being executed.
