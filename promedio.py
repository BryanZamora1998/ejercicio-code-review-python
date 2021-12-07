import numpy as np

class promedio:

    def __init__(self):
        self.principal()

    def principal(self):
        # -*- coding: utf-8 -*-
        # Decoración: Nombre del Algoritmo
        print("-------------------------------------------------------")
        print("Ha elejido PROMEDIO DE DOS NÚMEROS..")
        print("-------------------------------------------------------")
        # Entradas
        print("Ingrese notas: ")
        N1 = int(input("N1: "))
        N2 = int(input("N2: "))
        # Proceso
        S = N1 + N2
        P = S / 2
        # Salida
        print("\nSALIDA: ")
        print("-------------------------------------------------------")
        print("Promedio:", P)