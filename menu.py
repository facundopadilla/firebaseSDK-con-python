from autenticar.firebase import *
from sdk import operar

# éste es el menú principal
def menu():
    while(True):
        print("""\n--- Menú de Firebase --- 
[1] Autenticar con Firebase
[2] Operar con base de datos
[3] Salir""")
        opcion = input("\n>>> Ingresar opción: ")
        if opcion == "1":
            conexion = autenticar()
        elif opcion == "2":
            try:
                operar(conexion)
            except UnboundLocalError:
                print("\n>>> Error: ingrese el archivo .json desde la opción 1")
        elif opcion == "3":
            print("\n>>> Finalizando la ejecución del programa...")
            break
        else:
            print("\n>>> Error: ingrese una opción correcta...")
