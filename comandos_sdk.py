from firebase_admin import db
from validaciones import *

# propiedadesConexion me muestra las propiedades de la conexion
def propiedadesConexion(conexion):
    print(f"""
    - Nombre: {conexion.name} 
    - ID (base de datos): {conexion.project_id}
    - Servicios: {conexion._services}
    - Proyecto inicializado: {conexion._project_id_initialized}
    """)

# obtenerBD me muestra todo lo que encuentra en la raíz de la base de datos, por eso el '/', que hace referencia a la raíz 
def obtenerBD():
    print("\n--- Bases de datos ---\n")
    for i,token in enumerate(db.reference('/').get()):
        print(f"[{i}] {token}")
        for j,value in enumerate(db.reference('/'+token).get()):
            print(f"\t[{j}] {value}:{db.reference('/'+token+'/'+value).get()}")

            
# editarBD me permite añadir, eliminar y/o editar algun valor en específico de la base de datos, ref es acrónimo de "referencia".
def editarBD():
    while(True):
        print("""\n\t--- Edición de la base de datos ---
[1] Añadir 
[2] Editar
[3] Eliminar
[4] Volver""")
        opcion = input("\n>>> Selecionar una opción: ")
        if opcion == "1":
            addBD() # validaciones.py
        elif opcion == "2":
            modificarBD() # validaciones.py
        elif opcion == "3":
            eliminarBD() # validaciones.py
        elif opcion == "4":
            break