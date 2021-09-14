from numeros import *

def escribir_menu():
    print('\r\nCALCULADORA\r\n1. Suma\r\n2. Resta\r\n3. Producto\r\n4. División\r\n0. Salir')


def pedir_int(mensaje):
    try:
        op = int(input(mensaje))
    except ValueError:
        op = None
    finally:
        return op


def escribir_submenu():
    print('\r\nTipo de números\r\n1. Números enteros\r\n2. Números racionales\r\n0. Cancelar')


if __name__ == '__main__':
    while True:
        escribir_menu()
        opcion = pedir_int('Escoja una opción: ')
        if opcion == 0:
            exit(0)
        elif opcion in range(1, 4):
            escribir_submenu()
            opcion_submenu = pedir_int('Escoja una opción: ')
            operando1 = None
            operando2 = None
            resultado = None
            if opcion_submenu == 1:
                valor1 = pedir_int('Escriba el valor del primer operando: ')
                if valor1 is None:
                    print('El valor tiene que ser un número entero')
                    continue
                valor2 = pedir_int('Escriba el valor del segundo operando: ')
                if valor2 is None:
                    print('El valor tiene que ser un número entero')
                    continue
                operando1 = Entero(valor1)
                operando2 = Entero(valor2)
                if opcion == 1:
                    resultado = operando1.suma(operando2)
                elif opcion == 2:
                    resultado = operando1.resta(operando2)
                elif opcion == 3:
                    resultado = operando1.producto(operando2)
                elif opcion == 4:
                    resultado = operando1.division(operando2)
                print('El resultado es:', resultado)
            elif opcion_submenu == 2:
                numerador1 = pedir_int('Escriba el numerador del primer operando: ')
                if numerador1 is None:
                    print('El numerador tiene que ser un número entero')
                    continue
                denominador1 = pedir_int('Escriba el denominador del primer operando: ')
                if denominador1 is None:
                    print('El denominador tiene que ser un número entero')
                    continue
                numerador2 = pedir_int('Escriba el numerador del segundo operando: ')
                if numerador2 is None:
                    print('El numerador tiene que ser un número entero')
                    continue
                denominador2 = pedir_int('Escriba el denominador del segundo operando: ')
                if denominador2 is None:
                    print('El denominador tiene que ser un número entero')
                    continue
                operando1 = Racional(numerador1, denominador1)
                operando2 = Racional(numerador2, denominador2)
                if opcion == 1:
                    resultado = operando1.suma(operando2)
                elif opcion == 2:
                    resultado = operando1.resta(operando2)
                elif opcion == 3:
                    resultado = operando1.producto(operando2)
                elif opcion == 4:
                    resultado = operando1.division(operando2)
                print('El resultado es:', resultado)
            elif opcion_submenu == 0:
                continue
            else:
                print('Opción no válida')
        else:
            print('Opción no válida')
