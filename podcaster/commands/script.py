import sys

def script(filename=None):
    if filename:
        with open(filename, 'r') as file:
            input_text = file.read()
    else:
        if sys.stdin.isatty():
            print("Type or paste in some text and hit ctrl D to process")
        input_text = sys.stdin.read()

    create_script(input_text)

def create_script(text):
    print('this is my input text', text)
