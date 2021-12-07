import numpy as np

class gasolinera:

    def __init__(self):
        self.principal()

    def principal(self):
        # Decoración: Nombre del Algoritmo
        # Constantes
        LITXG = 3.785
        PRECIOXL = 4.50
        # Entradas
        consu = float(input("Ingresar consumo: "))
        # Proceso
        total = consu * LITXG * PRECIOXL
        # Salida
        print("\nSALIDA: ")
        print("-------------------------------------------------------")
        print("Total:", total)
