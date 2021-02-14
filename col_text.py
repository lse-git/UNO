global colreset
colreset = '\033[m'

def green_print(text):
    colgreen = '\033[32m'
    print(colgreen + text + colreset)

def red_print(text):
    colred = '\033[31m'
    print(colred + text + colreset)

def yellow_print(text):
    colyellow = '\033[33m'
    print(colyellow + text + colreset)
