# Modulo de conversiones de longitud

def kilometros_a_millas(kilometros):
    # Convierte kilometros a millas
    try:
        millas = kilometros * 0.621371
        return f"{kilometros} kilometros = {millas:.2f} millas"
    except TypeError:
        return "Error: El valor debe ser un numero"


def millas_a_kilometros(millas):
    # Convierte millas a kilometros
    try:
        kilometros = millas / 0.621371
        return f"{millas} millas = {kilometros:.2f} kilometros"
    except TypeError:
        return "Error: El valor debe ser un numero"


def metros_a_pies(metros):
    # Convierte metros a pies
    try:
        pies = metros * 3.28084
        return f"{metros} metros = {pies:.2f} pies"
    except TypeError:
        return "Error: El valor debe ser un numero"


def pulgadas_a_centimetros(pulgadas):
    # Convierte pulgadas a centimetros
    try:
        centimetros = pulgadas * 2.54
        return f"{pulgadas} pulgadas = {centimetros:.2f} centimetros"
    except TypeError:
        return "Error: El valor debe ser un numero"