import getpass
from IO import read_json_file, write_json_file
from utils import clear_terminal
from terminalPrints import print_title, print_text_with_bg


def get_settings():
    settingsSchema = {
            "spaces": 1,
            "simbols": 1,
            "accents": 0,
            "capital": 0,
        }
    previous_settings = read_json_file("settings.json")
    if (read_json_file("settings.json") != None):
        settings = previous_settings
        for key in settingsSchema:
            if key not in previous_settings:
                settings[key] = settingsSchema[key]
    else:
        settings = settingsSchema
    return settings


def settings_mode():
    settings = get_settings();

    while True:
        clear_terminal()
        print_title("AJUSTES")
        print("1. Espacios entre palabras:", end="  ")
        printStatus(settings["spaces"] == 1)
        print("2. Reconocer acentos", end= "  ")
        printStatus(settings["accents"] == 1)
        print("3. Reconocer simbolos", end= "  ")
        printStatus(settings["simbols"] == 1)
        print("4. Reconocer mayusculas", end= "  ")
        printStatus(settings["capital"] == 1)
        print("5. Salir y guardar los cambios")
        option = input("\nOpcion: ")
        if (option == "1"):
            settings["spaces"] = abs(settings["spaces"]-1);
        elif (option == "2"):
            settings["accents"] = abs(settings["accents"]-1);
        elif (option == "3"):
            settings["simbols"] = abs(settings["simbols"]-1);
        elif (option == "4"):
            settings["capital"] = abs(settings["capital"]-1);
        elif (option == "5"):
            write_json_file("settings.json", settings)
            break;
        else:
            print("Opcion no valida. Intente de nuevo.")
            getpass.getpass("Pulsa ENTER para continuar.");


def printStatus(active):
    if (active):
        print_text_with_bg("Activado", "cyan", end="  ")
        print("Desactivado")
    else:
        print("Activado", end="  ")
        print_text_with_bg("Desactivado", "cyan")

