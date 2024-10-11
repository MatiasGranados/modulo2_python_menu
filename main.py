def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for mostrar in sorted(opciones):
        print(f' {mostrar}) {opciones[mostrar][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

def menu_principal():
    opciones = {
        '1': ('SUMAR', suma),
        '2': ('RESTAR', resta),
        '3': ('MULTIPLICAR', multiplicacion),
        '4': ('DIVIDIR', division),
        '5': ('Salir', salir)
    }
    generar_menu(opciones, '5')

#LISTA para el historial
historial = []

def suma():
    print('ELEGISTE LA OPCIÓN DE SUMA')
    num1 = float(input("INGRESE NUMERO 1:"))
    num2 = float(input("INGRESE NUMERO 2:"))
    suma = num1+num2
    print("LA SUMA ES DE:", suma)
    historial.append(suma)

def resta():
    print('ELEGISTE LA OPCIÓN DE RESTA')
    num3 = float(input("INGRESE NUMERO 1:"))
    num4 = float(input("INGRESE NUMERO 2:"))
    resta = num3-num4
    print("LA RESTA ES DE:", resta)
    historial.append(resta)

def multiplicacion():
    print('ELEGISTE LA OPCIÓN DE MULTIPLICACIÓN')
    num5 = float(input("INGRESE NUMERO 1:"))
    num6 = float(input("INGRESE NUMERO 2:"))
    multiplicacion = num5*num6
    print("LA MULTIPLICACIÓN ES DE:", multiplicacion)
    historial.append(multiplicacion)

def division():
    print('ELEGISTE LA OPCIÓN DE DIVISIÓN')
    num7 = float(input("INGRESE NUMERO 1:"))
    num8 = float(input("INGRESE NUMERO 2:"))
    division = num7/num8
    print("LA DIVISIÓN ES DE:", division)
    historial.append(division)

def salir():
    print("EL HISTORIAL DE CALCULOS:", historial)
    print('SALISTE DE LA CALCULAD0RA')

if __name__ == '__main__':
    menu_principal()