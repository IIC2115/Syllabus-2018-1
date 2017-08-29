from json import load


def obtener_informacion():
    try:
        with open("Estaciones.json") as file:
            return load(file)
    except FileNotFoundError:
        print("El archivo Estaciones.json no está en la carpeta junto a utils.py")
        return None


def obtener_modelo(modelo):
    if isinstance(modelo, int):
        if modelo in [1, 2, 3]:
            try:
                with open("Modelo {}.json".format(modelo)) as file:
                    return load(file)
            except FileNotFoundError:
                print("El archivo Modelo {}.json no está en la carpeta junto a utils.py".format(modelo))
                return None
        else:
            print("El número debe ser 1, 2 o 3")
            return None
    else:
        print("Esta funcion recibe solo un número en forma de integer")
        return None
