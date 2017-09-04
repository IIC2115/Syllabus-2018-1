from json import load


def obtener_informacion():
    try:
        with open("Personas.json") as file:
            return load(file)
    except FileNotFoundError:
        print("El archivo Personas.json no esta en la carpeta junto a utils.py")
        return None


def obtener_relaciones():
    try:
        with open("Familia.json") as file:
            return load(file)
    except FileNotFoundError:
        print("El archivo Familia.json no esta en la carpeta junto a utils.py")
        return None
