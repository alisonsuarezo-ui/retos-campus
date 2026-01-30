# Modulo de conversiones de peso

def kilogramos_a_libras(kilogramos):
    # Convierte kilogramos a libras
    try:
        libras = kilogramos * 2.20462
        return f"{kilogramos} kilogramos = {libras:.2f} libras"
    except TypeError:
        return "Error: El valor debe ser un numero"


def libras_a_kilogramos(libras):
    # Convierte libras a kilogramos
    try:
        kilogramos = libras / 2.20462
        return f"{libras} libras = {kilogramos:.2f} kilogramos"
    except TypeError:
        return "Error: El valor debe ser un numero"


def gramos_a_onzas(gramos):
    # Convierte gramos a onzas
    try:
        onzas = gramos * 0.035274
        return f"{gramos} gramos = {onzas:.2f} onzas"
    except TypeError:
        return "Error: El valor debe ser un numero"


def onzas_a_gramos(onzas):
    # Convierte onzas a gramos
    try:
        gramos = onzas / 0.035274
        return f"{onzas} onzas = {gramos:.2f} gramos"
    except TypeError:
        return "Error: El valor debe ser un numero"