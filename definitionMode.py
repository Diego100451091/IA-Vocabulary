import random
from utils import clear_terminal, get_exit
from terminalPrints import print_title, print_colored_text

def definition_mode(dictionary):
    remaining_words = dictionary.copy()
    while True:
        clear_terminal()
        print_title("MODO DEFINICIÓN")
        
        if (len(remaining_words) == 0):
            print("Ya se han mostrado todas las palabras")
            break

        word = remaining_words.pop(random.randrange(len(remaining_words)))
        print("CONCEPTO:    ", word["concept"])
        print("DEFINICION:  ", word["definition"])

        if get_exit():
            break

