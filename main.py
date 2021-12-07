# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from calculadora import calculadora
from numerosPrimos import numerosPrimo


def menu():
    print("Que transaccion desea realizar:")
    print("1. Calculadora")
    print("2. Numeros Primos")
    valor1 = int(input("valor:"))
    return valor1

def principal():
    valor=menu()

    if valor == 1:
        calculadora()
    if valor == 2:
        numerosPrimo()

principal()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
