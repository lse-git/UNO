global colreset
colreset = '\033[m'

def green_print(text):
    colgreen = '\033[32m'
    print(colgreen + text + colreset)

def green_input(text):
    colgreen = '\033[32m'
    return input(colgreen + text + colreset)

def red_print(text):
    colred = '\033[31m'
    print(colred + text + colreset)

def red_input(text):
    colred = '\033[31m'
    return input(colred + text + colreset)

def yellow_print(text):
    colyellow = '\033[33m'
    print(colyellow + text + colreset)

def yellow_input(text):
    colyellow = '\033[33m'
    return input(colyellow + text + colreset)