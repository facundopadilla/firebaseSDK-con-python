# En sdk.py realizamos la consulta, en comandos_sdk.py tenemos las funciones de cada uno

import firebase_admin
from comandos_sdk import *

# operar es el menú donde recibo la conexión y puedo realizar las siguientes operaciones
def operar(conexion):
    while(True):
        print("""\n\t --- Operar con Firebase ---\n
[1] Mostrar propiedades de la conexión
[2] Obtener base de datos
[3] Editar base de datos
[4] Volver""")
        opcion = input("\n>>> Ingresar opción: ")
        if opcion == "1":
            propiedadesConexion(conexion)
        elif opcion == "2":
            obtenerBD(conexion)
        elif opcion == "3":
            editarBD(conexion)
        elif opcion == "4":
            break

