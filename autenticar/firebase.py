# Configuración de conexión y autenticación

import firebase_admin
from firebase_admin import credentials
from pathlib import Path

def autenticar():
    try:
        archivo = buscar()
        print(">>> Archivo elegido:", archivo)
        credencial = credentials.Certificate(f'autenticar/{archivo}')
        return(firebase_admin.initialize_app(credencial,{
            'databaseURL': 'LA URL DE TU BASE DE DATOS'
            }
        ))
    except IndexError:
        print("\n>>> Error: ingrese un archivo correcto...")   
    except ValueError:
        print("\n>>> Error: ya cargó el archivo .json")

def buscar():
    try:
        lista_de_archivos = [obj.name for obj in Path('autenticar/').iterdir() if obj.is_file()]
        print("") #salto de línea
        for i,j in enumerate(lista_de_archivos):
            print(f"[{i}] {j}")
        opcion = int(input("\n>>> Ingresa el número del archivo (.json): "))
        return lista_de_archivos[opcion]
    except FileNotFoundError:
        print("\n>>> Error: no se encuentra la carpeta 'autenticar' dentro del mismo directorio...") 
