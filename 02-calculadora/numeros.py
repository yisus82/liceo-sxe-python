class Numero:
    def suma(self, operando):
        pass

    def resta(self, operando):
        pass

    def producto(self, operando):
        pass

    def division(self, operando):
        pass

    def mostrar(self):
        pass

    def __str__(self):
        return self.mostrar()


class Entero(Numero):
    def __init__(self, valor):
        self.valor = valor

    def suma(self, operando):
        if isinstance(operando, Entero):
            return Entero(self.valor + operando.valor)
        else:
            print('El operando tiene que ser de clase Entero')
            return None

    def resta(self, operando):
        if isinstance(operando, Entero):
            return Entero(self.valor - operando.valor)
        else:
            print('El operando tiene que ser de clase Entero')
            return None

    def producto(self, operando):
        if isinstance(operando, Entero):
            return Entero(self.valor * operando.valor)
        else:
            print('El operando tiene que ser de clase Entero')
            return None

    def division(self, operando):
        if isinstance(operando, Entero):
            if operando.valor == 0:
                print('División entre 0')
                return None
            return Entero(self.valor / operando.valor)
        else:
            print('El operando tiene que ser de clase Entero')
            return None

    def mostrar(self):
        return str(self.valor)


class Racional(Numero):
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def suma(self, operando):
        if isinstance(operando, Racional):
            a = self.numerador
            b = self.denominador
            c = operando.numerador
            d = operando.denominador
            num = a * d + b * c
            den = b * d
            return Racional(num, den)
        else:
            print('El operando tiene que ser de clase Racional')
            return None

    def resta(self, operando):
        if isinstance(operando, Racional):
            a = self.numerador
            b = self.denominador
            c = operando.numerador
            d = operando.denominador
            num = a * d - b * c
            den = b * d
            return Racional(num, den)
        else:
            print('El operando tiene que ser de clase Racional')
            return None

    def producto(self, operando):
        if isinstance(operando, Racional):
            a = self.numerador
            b = self.denominador
            c = operando.numerador
            d = operando.denominador
            num = a * c
            den = b * d
            return Racional(num, den)
        else:
            print('El operando tiene que ser de clase Racional')
            return None

    def division(self, operando):
        if isinstance(operando, Racional):
            a = self.numerador
            b = self.denominador
            c = operando.numerador
            d = operando.denominador
            num = a * d
            den = b * c
            return Racional(num, den)
        else:
            print('El operando tiene que ser de clase Racional')
            return None

    def mostrar(self):
        return str(self.numerador) + " / " + str(self.denominador)
