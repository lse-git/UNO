global colreset
colreset = '\033[m'

def green_print(text):
    colgreen = '\033[32m'
    print(colgreen + text + colreset)
