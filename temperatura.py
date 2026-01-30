# Modulo de conversiones de temperatura

def celsius_a_fahrenheit(celsius):
    # Convierte celsius a fahrenheit
    try:
        fahrenheit = (celsius * 9/5) + 32
        return f"{celsius} grados Celsius = {fahrenheit:.2f} grados Fahrenheit"
    except TypeError:
        return "Error: El valor debe ser un numero"


def fahrenheit_a_celsius(fahrenheit):
    # Convierte fahrenheit a celsius
    try:
        celsius = (fahrenheit - 32) * 5/9
        return f"{fahrenheit} grados Fahrenheit = {celsius:.2f} grados Celsius"
    except TypeError:
        return "Error: El valor debe ser un numero"


def celsius_a_kelvin(celsius):
    # Convierte celsius a kelvin
    try:
        kelvin = celsius + 273.15
        return f"{celsius} grados Celsius = {kelvin:.2f} Kelvin"
    except TypeError:
        return "Error: El valor debe ser un numero"


def kelvin_a_celsius(kelvin):
    # Convierte kelvin a celsius
    try:
        celsius = kelvin - 273.15
        return f"{kelvin} Kelvin = {celsius:.2f} grados Celsius"
    except TypeError:
        return "Error: El valor debe ser un numero"