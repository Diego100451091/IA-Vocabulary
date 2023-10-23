import getpass

from constants import COLORS, DICTIONARY
from utils import clear_terminal
from definitionMode import definition_mode
from guessMode import guess_mode
from IO import read_json_file, delete_file

def main():
    while True:
        clear_terminal()
        print(
            f"{COLORS['purple']}==========| MODO DE JUEGO |=========={COLORS['reset']}")
        print("Seleccione el modo de juego: ")
        print("1. Definición")
        print("2. Adivinanza")
        print("3. Modo errores")
        print("4. Eliminar registro errores")
        print("5. Salir")
        option = input("\nOpcion: ")
        if (option == "1"):
            definition_mode()
        elif (option == "2"):
            guess_mode(DICTIONARY)
        elif (option == "3"):
            wrong_dict = read_json_file("wrong_words.json")
            if (wrong_dict != None):
                guess_mode(wrong_dict)
            else:
                print("No hay registro de palabras falladas")
                getpass.getpass("Pulsa ENTER para continuar.")
        elif (option == "4"):
            delete_file("wrong_words.json")
            print("Registro de errores eliminado")
            getpass.getpass("Pulsa ENTER para continuar.")
        elif (option == "5"):
            break
        else:
            print("Opcion no valida. Intente de nuevo.")
            getpass.getpass("Pulsa ENTER para continuar.");

if __name__ == "__main__":
    main()
