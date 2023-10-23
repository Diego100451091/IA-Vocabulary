import os
import unicodedata

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_exit():
    text = input("\nPresiona ENTER para continuar o 'exit' para salir del modo\n");
    if text == "exit":
        return True;
    else:
        return False;