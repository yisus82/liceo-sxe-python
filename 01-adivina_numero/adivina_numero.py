from random import randint


def escribir_menu():
    print('\nADIVINA EL NÚMERO\n1. Del 1 al 10 (3 intentos)\n2. Del 1 al 50 (5 intentos)\n0. Salir')


def pedir_opcion():
    print('Escoja una opción: ', end='')


def leer_opcion():
    try:
        op = int(input())
    except ValueError:
        op = None
    finally:
        return op


def generar_numero(min, max):
    return randint(min, max)


def pedir_numero():
    try:
        num = int(input('Escriba un número: '))
    except ValueError:
        num = None
    finally:
        return num


def jugar(min, max, max_intentos):
    numero_aleatorio = generar_numero(min, max)
    # print('Número generado:', numero_aleatorio)
    intentos = 0
    while intentos < max_intentos:
        numero_usuario = pedir_numero()
        if numero_usuario is None:
            print('Introduzca un número válido')
        else:
            intentos += 1
            if numero_usuario == numero_aleatorio:
                print('Acertó el número en', intentos, 'intentos')
                break
            elif numero_usuario < numero_aleatorio:
                print('El número a adivinar es mayor')
            else:
                print('El número a adivinar es menor')
    if numero_usuario != numero_aleatorio:
        print('No ha acertado en el número máximo de intentos. El número era', numero_aleatorio)


if __name__ == '__main__':
    while True:
        escribir_menu()
        pedir_opcion()
        opcion = leer_opcion()
        if opcion == 0:
            exit(0)
        elif opcion == 1:
            jugar(1, 10, 3)
        elif opcion == 2:
            jugar(1, 50, 5)
        else:
            print('Opción no válida')
