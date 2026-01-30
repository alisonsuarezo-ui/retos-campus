# Modulo de conversiones de volumen

def litros_a_galones(litros):
    # Convierte litros a galones estadounidenses
    try:
        galones = litros * 0.264172
        return f"{litros} litros = {galones:.2f} galones"
    except TypeError:
        return "Error: El valor debe ser un numero"


def galones_a_litros(galones):
    # Convierte galones estadounidenses a litros
    try:
        litros = galones / 0.264172
        return f"{galones} galones = {litros:.2f} litros"
    except TypeError:
        return "Error: El valor debe ser un numero"


def mililitros_a_onzas_fluidas(mililitros):
    # Convierte mililitros a onzas fluidas estadounidenses
    try:
        onzas_fluidas = mililitros * 0.033814
        return f"{mililitros} mililitros = {onzas_fluidas:.2f} onzas fluidas"
    except TypeError:
        return "Error: El valor debe ser un numero"


def tazas_a_litros(tazas):
    # Convierte tazas estadounidenses a litros
    try:
        litros = tazas * 0.236588
        return f"{tazas} tazas = {litros:.2f} litros"
    except TypeError:
        return "Error: El valor debe ser un numero"