import longitud
import temperatura
import peso
import volumen
import velocidad

def menu_principal():
    # Menu principal de conversiones
    while True:
        print("\n" + "="*50)
        print("      SISTEMA DE CONVERSION DE UNIDADES")
        print("="*50)
        print("\nSeleccione una categoria:\n")
        print("1. Conversiones de Longitud")
        print("2. Conversiones de Temperatura")
        print("3. Conversiones de Peso")
        print("4. Conversiones de Volumen")
        print("5. Conversiones de Velocidad")
        print("6. Salir")
        print("="*50)
        
        try:
            opcion = input("\nSeleccione una opcion: ")
            
            if opcion == "1":
                menu_longitud()
            elif opcion == "2":
                menu_temperatura()
            elif opcion == "3":
                menu_peso()
            elif opcion == "4":
                menu_volumen()
            elif opcion == "5":
                menu_velocidad()
            elif opcion == "6":
                print("\nGracias por usar el sistema de conversiones")
                print("Hasta pronto\n")
                break
            else:
                print("\nOpcion no valida")
        
        except Exception as e:
            print(f"\nOcurrio un error: {e}")


def menu_longitud():
    # Menu de conversiones de longitud
    while True:
        print("\n" + "="*50)
        print("         CONVERSIONES DE LONGITUD")
        print("="*50)
        print("\n1. Kilometros a Millas")
        print("2. Millas a Kilometros")
        print("3. Metros a Pies")
        print("4. Pulgadas a Centimetros")
        print("5. Regresar al menu principal")
        print("="*50)
        
        opcion = input("\nSeleccione una opcion: ")
        
        if opcion == "1":
            valor = float(input("\nIngrese los kilometros: "))
            print("\n" + longitud.kilometros_a_millas(valor))
        elif opcion == "2":
            valor = float(input("\nIngrese las millas: "))
            print("\n" + longitud.millas_a_kilometros(valor))
        elif opcion == "3":
            valor = float(input("\nIngrese los metros: "))
            print("\n" + longitud.metros_a_pies(valor))
        elif opcion == "4":
            valor = float(input("\nIngrese las pulgadas: "))
            print("\n" + longitud.pulgadas_a_centimetros(valor))
        elif opcion == "5":
            break
        else:
            print("\nOpcion no valida")
        
        input("\nPresione ENTER para continuar...")


def menu_temperatura():
    # Menu de conversiones de temperatura
    while True:
        print("\n" + "="*50)
        print("        CONVERSIONES DE TEMPERATURA")
        print("="*50)
        print("\n1. Celsius a Fahrenheit")
        print("2. Fahrenheit a Celsius")
        print("3. Celsius a Kelvin")
        print("4. Kelvin a Celsius")
        print("5. Regresar al menu principal")
        print("="*50)
        
        opcion = input("\nSeleccione una opcion: ")
        
        if opcion == "1":
            valor = float(input("\nIngrese los grados Celsius: "))
            print("\n" + temperatura.celsius_a_fahrenheit(valor))
        elif opcion == "2":
            valor = float(input("\nIngrese los grados Fahrenheit: "))
            print("\n" + temperatura.fahrenheit_a_celsius(valor))
        elif opcion == "3":
            valor = float(input("\nIngrese los grados Celsius: "))
            print("\n" + temperatura.celsius_a_kelvin(valor))
        elif opcion == "4":
            valor = float(input("\nIngrese los Kelvin: "))
            print("\n" + temperatura.kelvin_a_celsius(valor))
        elif opcion == "5":
            break
        else:
            print("\nOpcion no valida")
        
        input("\nPresione ENTER para continuar...")


def menu_peso():
    # Menu de conversiones de peso
    while True:
        print("\n" + "="*50)
        print("           CONVERSIONES DE PESO")
        print("="*50)
        print("\n1. Kilogramos a Libras")
        print("2. Libras a Kilogramos")
        print("3. Gramos a Onzas")
        print("4. Onzas a Gramos")
        print("5. Regresar al menu principal")
        print("="*50)
        
        opcion = input("\nSeleccione una opcion: ")
        
        if opcion == "1":
            valor = float(input("\nIngrese los kilogramos: "))
            print("\n" + peso.kilogramos_a_libras(valor))
        elif opcion == "2":
            valor = float(input("\nIngrese las libras: "))
            print("\n" + peso.libras_a_kilogramos(valor))
        elif opcion == "3":
            valor = float(input("\nIngrese los gramos: "))
            print("\n" + peso.gramos_a_onzas(valor))
        elif opcion == "4":
            valor = float(input("\nIngrese las onzas: "))
            print("\n" + peso.onzas_a_gramos(valor))
        elif opcion == "5":
            break
        else:
            print("\nOpcion no valida")
        
        input("\nPresione ENTER para continuar...")


def menu_volumen():
    # Menu de conversiones de volumen
    while True:
        print("\n" + "="*50)
        print("          CONVERSIONES DE VOLUMEN")
        print("="*50)
        print("\n1. Litros a Galones")
        print("2. Galones a Litros")
        print("3. Mililitros a Onzas Fluidas")
        print("4. Tazas a Litros")
        print("5. Regresar al menu principal")
        print("="*50)
        
        opcion = input("\nSeleccione una opcion: ")
        
        if opcion == "1":
            valor = float(input("\nIngrese los litros: "))
            print("\n" + volumen.litros_a_galones(valor))
        elif opcion == "2":
            valor = float(input("\nIngrese los galones: "))
            print("\n" + volumen.galones_a_litros(valor))
        elif opcion == "3":
            valor = float(input("\nIngrese los mililitros: "))
            print("\n" + volumen.mililitros_a_onzas_fluidas(valor))
        elif opcion == "4":
            valor = float(input("\nIngrese las tazas: "))
            print("\n" + volumen.tazas_a_litros(valor))
        elif opcion == "5":
            break
        else:
            print("\nOpcion no valida")
        
        input("\nPresione ENTER para continuar...")


def menu_velocidad():
    # Menu de conversiones de velocidad
    while True:
        print("\n" + "="*50)
        print("         CONVERSIONES DE VELOCIDAD")
        print("="*50)
        print("\n1. Kilometros por hora a Metros por segundo")
        print("2. Metros por segundo a Kilometros por hora")
        print("3. Millas por hora a Kilometros por hora")
        print("4. Nudos a Millas por hora")
        print("5. Regresar al menu principal")
        print("="*50)
        
        opcion = input("\nSeleccione una opcion: ")
        
        if opcion == "1":
            valor = float(input("\nIngrese los km/h: "))
            print("\n" + velocidad.kmh_a_ms(valor))
        elif opcion == "2":
            valor = float(input("\nIngrese los m/s: "))
            print("\n" + velocidad.ms_a_kmh(valor))
        elif opcion == "3":
            valor = float(input("\nIngrese las mph: "))
            print("\n" + velocidad.mph_a_kmh(valor))
        elif opcion == "4":
            valor = float(input("\nIngrese los nudos: "))
            print("\n" + velocidad.nudos_a_mph(valor))
        elif opcion == "5":
            break
        else:
            print("\nOpcion no valida")
        
        input("\nPresione ENTER para continuar...")


# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()