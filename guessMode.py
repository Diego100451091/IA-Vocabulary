import sys
import random
from utils import clear_terminal, get_exit, strip_accents
from terminalPrints import print_title, print_colored_text, print_progress
from IO import write_json_file
from settings import get_settings


def guess_mode(dictionary):
    settings = get_settings()

    remaining_words = dictionary.copy()
    wrong_words = []
    
    status_vector = []
    total_dictionary_lenght = len(dictionary)
    for i in range(total_dictionary_lenght):
        status_vector.append("clear")
    status_index = 0

    while True:
        clear_terminal()
        print_title("MODO ADIVINANZA")

        print_progress(status_vector)

        if (len(remaining_words) == 0):
            print("Ya se han mostrado todas las palabras")
            break

        word = remaining_words.pop(random.randrange(len(remaining_words)))
        print("DEFINICION:  ", word["definition"])
        print("CONCEPTO:     ")
        word_concept = word['concept']
        word_concept = trim_spaces(word_concept, settings["spaces"] == 1)
        word_concept = skip_simbols(word_concept, settings["simbols"] == 1)

        guessedWord = get_user_word(word_concept)

        if settings["accents"] == 0:
            guessedWord = strip_accents(guessedWord)
            word_concept = strip_accents(word_concept)
        
        if settings["capital"] == 0:
            guessedWord = guessedWord.lower()
            word_concept = word_concept.lower()

        if (guessedWord == word_concept):
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

        guessedWord = input(wordSchema)
        if (len(guessedWord) == len(concept)):
            return guessedWord
        # Go one line up and remove the line
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        sys.stdout.flush()

def trim_spaces (word, use_spaces):
    if use_spaces:
        return word

    newWord = ""
    for letter in word:
        if (letter != " "):
            newWord += letter
    return newWord

def skip_simbols (word, use_simbols):
    if use_simbols:
        return word
    
    newWord = ""
    for letter in word:
        if letter not in ["-", "_", "(", ")"]:
            newWord += letter
    return newWord

def show_wrong_words(wrong_words):
    print("\nPalabras falladas:")
    for word in wrong_words:
        print("\nCONCEPTO: ", word["concept"])
        print("DEFINICIÓN: ", word["definition"])

    get_exit()

def get_schema(word):
    schema = ""
    for letter in word:
        if letter in ["/", "-", "_", "(", ")", " "]:
            schema += letter
        else:
            schema += "#"
    schema += "\r"
    return schema
