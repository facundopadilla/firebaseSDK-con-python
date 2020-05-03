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
def obtenerBD(conexion):
    print("\n--- Bases de datos ---\n")
    bases = [i for i in db.reference('/').get()]
    for i,base in enumerate(bases):
        print(f"[{i}] {base}")
        for j,dato in enumerate(db.reference('/'+str(base)+'/').get()):
            print(f"\t[{j}] {dato}")

             #TODO---

# editarBD me permite añadir, eliminar y/o editar algun valor en específico de la base de datos, ref es acrónimo de "referencia".
def editarBD(conexion):
    while(True):
        print("""\n\t--- Edición de la base de datos ---
[1] Añadir 
[2] Editar
[3] Eliminar
[4] Volver""")
        opcion = input("\n>>> Selecionar una opción: ")
        if opcion == "1":
            nombre = ingresarNombre()
            apellido = ingresarApellido()
            edad = ingresarEdad()
        elif opcion == "2":
            break
            #TODO
        elif opcion == "3":
            pass
            #TODO
        elif opcion == "4":
            pass
            #TODO