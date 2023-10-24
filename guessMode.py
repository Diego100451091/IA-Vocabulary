import sys
import random
from utils import clear_terminal, get_exit, strip_accents
from terminalPrints import print_title, print_colored_text
from IO import write_json_file
from settings import get_settings


def guess_mode(dictionary):
    settings = get_settings()

    remaining_words = dictionary.copy()
    total_dictionary_lenght = len(dictionary)
    status_vector = []
    wrong_words = []
    for i in range(total_dictionary_lenght):
        status_vector.append("clear")
    status_index = 0

    while True:
        clear_terminal()
        print_title("MODO ADIVINANZA")

        print_progress(status_vector, status_index, total_dictionary_lenght)

        if (len(remaining_words) == 0):
            print("Ya se han mostrado todas las palabras")
            break

        word = remaining_words.pop(random.randrange(len(remaining_words)))
        print("DEFINICION:  ", word["definition"])
        print("CONCEPTO:     ")
        word_concept = strip_accents(word['concept']).lower()
        trimmed_word = trim_spaces(word_concept, settings["spaces"])

        guessedWord = get_user_word(trimmed_word);

        if (guessedWord == trimmed_word):
            print_colored_text("¡Correcto!", "green")
            status_vector[status_index] = "correct"
        else:
            print_colored_text("Incorrecto", "red", "")
            print(" - La palabra era: ", word["concept"])
            status_vector[status_index] = "incorrect"
            wrong_words.append(word)

        status_index += 1

        if get_exit():
            break

    show_wrong_words(wrong_words)
    write_json_file("wrong_words.json", wrong_words)

def get_user_word(concept):
    while True:
        wordSchema = get_schema(concept)
        guessedWord = strip_accents(input(wordSchema).lower())
        if (len(guessedWord) == len(concept)):
            return guessedWord
        # Go one line up and remove the line
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        sys.stdout.flush()

def trim_spaces (word, use_spaces):
    if use_spaces == 1:
        return word
    else:
        newWord = ""
        for letter in word:
            if (letter != " "):
                newWord += letter
    return newWord

def show_wrong_words(wrong_words):
    print("\nPalabras falladas:")
    for word in wrong_words:
        print("\nCONCEPTO: ", word["concept"])
        print("DEFINICIÓN: ", word["definition"])

    get_exit()


def print_progress(status_vector, status_index, total_lenght):
    print("Progreso: ", end="")
    for status in status_vector:
        if status == "clear":
            print("■", end="")
        elif status == "correct":
            print_colored_text("■", "green", end="")
        elif status == "incorrect":
            print_colored_text("■", "red", end="")
    print(f" {status_index}/{total_lenght}\n")


def get_schema(word):
    schema = ""
    for letter in word:
        if letter in ["/", "-", "_", "(", ")", " "]:
            schema += letter
        else:
            schema += "#"
    schema += "\r"
    return schema
