import sys
import random
from constants import COLORS, DICTIONARY
from utils import clear_terminal, get_exit, strip_accents

def guess_mode():
    remaining_words = DICTIONARY.copy()
    total_dictionary_lenght = len(DICTIONARY);
    status_vector = []
    wrong_words = []
    for i in range(total_dictionary_lenght):
        status_vector.append("clear")
    status_index = 0

    while True:
        clear_terminal();
        print(
            f"{COLORS['purple']}==========| MODO ADIVINANZA |=========={COLORS['reset']}");

        print_progress(status_vector, status_index, total_dictionary_lenght);

        if (len(remaining_words) == 0):
            print("Ya se han mostrado todas las palabras");
            break;

        word = remaining_words.pop(random.randrange(len(remaining_words)));
        print("DEFINICION:  ", word["definition"]);
        print("CONCEPTO:     ");
        word_concept = strip_accents(word['concept']).lower();

        while True:
            wordSchema = get_schema(word["concept"]);
            guessedWord = strip_accents(input(wordSchema).lower());
            if (len(guessedWord) == len(word_concept)):
                break;
            # Go one line up and remove the line
            sys.stdout.write("\033[F");
            sys.stdout.write("\033[K");
            sys.stdout.flush()

        if (guessedWord == word_concept):
            print(f"{COLORS['green']}¡Correcto!{COLORS['reset']}");
            status_vector[status_index] = "correct";
        else:
            print(
                f"{COLORS['red']}Incorrecto{COLORS['reset']} - La palabra era: ", word["concept"]);
            status_vector[status_index] = "incorrect";
            wrong_words.append(word);

        status_index += 1;

        if get_exit():
            break;

    print("\nPalabras falladas:")
    for word in wrong_words:
        print("\nCONCEPTO: ", word["concept"]);
        print("DEFINICIÓN: ", word["definition"]);

    get_exit();


def print_progress(status_vector, status_index, total_lenght):
    print("Progreso: ", end="");
    for status in status_vector:
        if status == "clear":
            print("■", end="");
        elif status == "correct":
            print(f"{COLORS['green']}■{COLORS['reset']}", end="");
        elif status == "incorrect":
            print(f"{COLORS['red']}■{COLORS['reset']}", end="");
    print(f" {status_index}/{total_lenght}\n");

def get_schema(word):
    schema = "";
    for letter in word:
        if letter in ["/", "-", "_", " ", "(", ")"]:
            schema += letter;
        else:
            schema += "#";
    schema+= "\r"
    return schema;



