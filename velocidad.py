# Modulo de conversiones de velocidad

def kmh_a_ms(kmh):
    # Convierte kilometros por hora a metros por segundo
    try:
        ms = (kmh * 1000) / 3600
        return f"{kmh} km/h = {ms:.2f} m/s"
    except TypeError:
        return "Error: El valor debe ser un numero"


def ms_a_kmh(ms):
    # Convierte metros por segundo a kilometros por hora
    try:
        kmh = ms * 3.6
        return f"{ms} m/s = {kmh:.2f} km/h"
    except TypeError:
        return "Error: El valor debe ser un numero"


def mph_a_kmh(mph):
    # Convierte millas por hora a kilometros por hora
    try:
        kmh = mph * 1.60934
        return f"{mph} mph = {kmh:.2f} km/h"
    except TypeError:
        return "Error: El valor debe ser un numero"


def nudos_a_mph(nudos):
    # Convierte nudos a millas por hora
    try:
        mph = nudos * 1.15078
        return f"{nudos} nudos = {mph:.2f} mph"
    except TypeError:
        return "Error: El valor debe ser un numero"