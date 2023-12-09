import random
from utils import clear_terminal, get_exit
from terminalPrints import print_title, print_progress

def definition_mode(dictionary):
    remaining_words = dictionary.copy()

    status_vector = []
    total_dictionary_lenght = len(dictionary)
    for i in range(total_dictionary_lenght):
        status_vector.append("clear")
    status_index = 0

    while True:
        clear_terminal()
        print_title("MODO DEFINICIÓN")

        print_progress(status_vector)

        
        if (len(remaining_words) == 0):
            print("Ya se han mostrado todas las palabras")
            break

        word = remaining_words.pop(random.randrange(len(remaining_words)))
        print("CONCEPTO:    ", word["concept"])
        print("DEFINICION:  ", word["definition"])

        status_vector[status_index] = "correct"
        status_index += 1
        
        if get_exit():
            break

