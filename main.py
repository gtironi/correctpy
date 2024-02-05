import sys

def teste():
    with open(sys.argv[0], mode='r') as file:
        content = file.read()
        file.close()
    return content # Imprime o caminho do arquivo atual