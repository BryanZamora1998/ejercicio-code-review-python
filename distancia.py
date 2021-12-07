import numpy as np

class distancia:

    def __init__(self):
        self.principal()

    def principal(self):
        # Entradas
        print("Ingrese coordenadas del Punto A: ")
        AX = float(input("Ax: "))
        AY = float(input("Ay: "))
        print("Ingrese coordenadas del Punto B: ")
        BX = float(input("Bx: "))

        ISBN: 978 - 958 - 53018 - 2 - 5
        67 / 257
        BY = float(input("By: "))
        # Proceso
        D = ((AX - BX) ** 2 + (AY - BY) ** 2) ** 0.5
        # Salida
        print("\nSALIDA: ")
        print("-------------------------------------------------------")
        print("Resultado:", D)
