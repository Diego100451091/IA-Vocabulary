import getpass
from IO import read_json_file, write_json_file
from utils import clear_terminal
from terminalPrints import print_title, print_text_with_bg

def get_settings():
    previous_settings = read_json_file("settings.json") 
    if (read_json_file("settings.json") != None):
        settings = previous_settings
    else:
        settings = {
            "spaces": 1,
        }
    return settings

def settings_mode() :
    settings = get_settings();

    while True:
        clear_terminal()
        print_title("AJUSTES")
        print("1. Espacios entre palabras:", end="  ")
        if (settings["spaces"] == 1):
            print_text_with_bg("Activado", "cyan", end="  ")
            print("Desactivado")
        else:
            print("Activado", end="  ")
            print_text_with_bg("Desactivado", "cyan")
        print("2. Salir y guardar los cambios")
        option = input("\nOpcion: ")
        if (option == "1"): 
            settings["spaces"] = abs(settings["spaces"]-1); 
        elif (option == "2"):
            write_json_file("settings.json", settings)
            break;
        else:
            print("Opcion no valida. Intente de nuevo.")
            getpass.getpass("Pulsa ENTER para continuar.");



