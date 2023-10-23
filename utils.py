import os
import unicodedata

def strip_accents(string):
   """Removes accents and diacritics from a string.

   Args:
       string (str): The string to remove accents from.

   Returns:
       str: The input string with all accents and diacritics removed.
   """
   return ''.join(char for char in unicodedata.normalize('NFD', string)
                  if unicodedata.category(char) != 'Mn')

def clear_terminal():
    """
    Clears the terminal screen.

    This function checks the operating system and clears the terminal screen accordingly.
    On Windows, it uses the 'cls' command to clear the screen, while on Unix-based systems
    it uses the 'clear' command.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_exit():
    """
    Asks the user for input to either continue or exit the program.

    Returns:
    - True if the user inputs 'exit'
    - False if the user inputs anything else
    """
    text = input("\nPresiona ENTER para continuar o 'exit' para salir del modo\n");
    if text == "exit":
        return True;
    else:
        return False;