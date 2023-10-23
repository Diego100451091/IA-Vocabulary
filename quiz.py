import getpass

from constants import COLORS
from utils import clear_terminal
from definitionMode import definition_mode
from guessMode import guess_mode

def main():
    while True:
        clear_terminal()
        print(
            f"{COLORS['purple']}==========| MODO DE JUEGO |=========={COLORS['reset']}")
        print("Seleccione el modo de juego: ")
        print("1. Definición")
        print("2. Adivinanza")
        print("3. Salir")
        option = input("\nOpcion: ")
        if (option == "1"):
            definition_mode()
        elif (option == "2"):
            guess_mode()
        elif (option == "3"):
            break
        else:
            print("Opcion no valida. Intente de nuevo.")
            getpass.getpass("Pulsa ENTER para continuar.");

if __name__ == "__main__":
    main()
