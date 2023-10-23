import random
from constants import COLORS, DICTIONARY
from utils import clear_terminal, get_exit

def definition_mode():
    remaining_words = DICTIONARY.copy()
    while True:
        clear_terminal()
        print(
            f"{COLORS['purple']}==========| MODO DEFINICIÓN |=========={COLORS['reset']}");

        if (len(remaining_words) == 0):
            print("Ya se han mostrado todas las palabras");
            break;

        word = remaining_words.pop(random.randrange(len(remaining_words)));
        print("CONCEPTO:    ", word["concept"]);
        print("DEFINICION:  ", word["definition"]);

        if get_exit():
            break;

