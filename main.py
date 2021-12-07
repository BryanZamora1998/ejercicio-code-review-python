# This is a sample Python script.
from calculadora import calculadora
from distancia import distancia
from gasolinera import gasolinera
from numerosPrimos import numerosPrimo
from promedio import promedio
from rectangulo import rectangulo

def menu():
    print("QUE TRANSACCION DESEA REALIZAR:")
    print("1. CALCULADORA")
    print("2. NUMEROS PRIMOS")
    print("3. DISTANCIA ENTRE 2 PUNTOS A y B, en 2D.")
    print("4. PROMEDIO DE DOS NÚMEROS.")
    print("5. CALCULAR PERÍMETRO Y SUPERFICIE DEL RECTÁNGULO")
    print("6. GASOLINERA")
    valor = int(input("VALOR:"))
    return valor

def principal():
    valor=menu()

    if valor == 1:
        calculadora()
    if valor == 2:
        numerosPrimo()
    if valor == 3:
        distancia()
    if valor == 4:
        promedio()
    if valor==5:
        rectangulo()
    if valor==6:
        gasolinera()

principal()
