from firebase_admin import db

# --- validaciones ---

# validar el nombre
def ingresarNombre():
    while(True):
        try:
            nombre = input(">>> Ingresar nombre: ")
            if 3 <= len(nombre) <= 10 and nombre.isalpha():
                return nombre
            elif len(nombre) < 3 or len(nombre) > 10:
                print("\n>>> Error: Ingrese un nombre de 3 a 10 caracteres")
            elif nombre != nombre.isalpha():
                print("\n>>> Error: solo se puede ingresar letras")
        except ValueError:
            print("\n>>> Error: ingrese correctamente un nombre...")

# validar el apellido
def ingresarApellido():
    while(True):
        try:
             apellido = input(">>> Ingresar apellido: ")
             if 3 <= len(apellido) <= 10 and apellido.isalpha():
                return apellido
             elif len(apellido) < 3 or len(apellido) > 10:
                print("\n>>> Error: Ingrese un apellido de 3 a 10 caracteres")
             elif apellido != apellido.isalpha():
                print("\n>>> Error: solo se puede ingresar letras")
        except TypeError or ValueError:
            print("\n>>> Error: ingrese correctamente un apellido...")

# validar la edad
def ingresarEdad():
    while(True):
        try:
             edad = int(input(">>> Ingresar edad: "))
             if 18 <= edad <= 99:
                return edad
             elif edad < 18 or edad > 99:
                print("\n>>> Error: Ingrese una edad entre 18 a 99 años")
             elif edad != int:
                print("\n>>> Error: solo se puede ingresar números...")
        except ValueError:
            print("\n>>> Error: ingrese solamente números...")

# --- FUNCIONES DE SDK ---

# --- Añadir tokens ---

# si queremos añadir más valores a nuestra base de datos, solo creamos nuevas variables, preferiblemente para tener más control...
# ... de las mismas, creamos funcionas arriba como ingresarEdad(), ingresarApellido(), ingresarNombre(), etc...

def addBD():
    nombre = ingresarNombre()
    apellido = ingresarApellido()
    edad = ingresarEdad()
    print(f"\n>>> Estás por añadir: {nombre}, {apellido}, {edad}")
    confirmar = input("\n>>> Confirmar (s/n): ")
    if confirmar == "s" and "S":
        pushBD(nombre,apellido,edad) #validaciones.py
    elif confirmar == "n" and "N":
        print("\n>>> No se añadió nada...")

# si queremos generar un token propio, solamente tenemos que añadir dentro de pushDB:
# token = input("/n>>> Ingresar token personalizado:")
# de ahí, añadimos con un signo "+" a la reference: db.reference('/'+token)

def pushBD(nombre,apellido,edad):
    db.reference('/').push(
        {
            'nombre':nombre,
            'apellido':apellido,
            'edad':edad
        })
    print("\n>>> ¡Añadido con éxito!")

# --- fin de añadir ---

# --- modificar valores del token ----

def modificarBD():
    tokens = [i for i in db.reference('/').get()]
    while(True):
        for i,token in enumerate(tokens):
            print(f"[{i}] {token}")
        print("""
[1] Elegir un token
[2] Volver""")
        opcion = input("\n>>> Ingresar opcion: ")
        if opcion == "1":
            posicion = int(input("\n>>> Seleccionar token: "))
            originalToken = tokens[posicion]
            updateBD(originalToken) # se pasa el por parámetro el token a modificar
        elif opcion == "2":
            break
        else:
            print("\n>>> Error: selecciona una opción correcta...")

def updateBD(originalToken):
    nombre = ingresarNombre()
    apellido = ingresarApellido()
    edad = ingresarEdad()
    print(f"\n>>> Estás por editar: {originalToken}, {nombre}, {apellido}, {edad}")
    confirmar = input("\n>>> Confirmar (s/n): ")
    if confirmar == "s" and "S":
        # acá se realiza el update

        db.reference(originalToken).update({
            'nombre':nombre,
            'apellido':apellido,
            'edad':edad
        })
        print("\n>>> ¡Se ha modificado correctamente!")
    elif confirmar == "n" and "N":
        print("\n>>> No se modificó nada... ")

# --- fin de modificar ---

# --- eliminar un token específico ---

def eliminarBD():
    tokens = [i for i in db.reference('/').get()]
    while(True):
        print("\n--- Eliminación de tokens ---")
        for i,token in enumerate(tokens):
            print(f"[{i}] {token}")
        print("""
[1] Elegir un token
[2] Volver""")
        opcion = input("\n>>> Ingresar opcion: ")
        if opcion == "1":
            posicion = int(input("\n>>> Seleccionar token: "))
            originalToken = tokens[posicion]
            deleteBD(originalToken)
            tokens.pop(posicion)
        elif opcion == "2":
            break
        else:
            print("\n>>> Error: selecciona una opción correcta...")

def deleteBD(originalToken):
    print(f"\n>>> Estás por eliminar: {originalToken}")
    confirmar = input("\n>>> Confirmar (s/n): ")
    if confirmar == "s" and "S":
        # acá se realiza el delete
        db.reference(originalToken).delete()
        print("\n>>> ¡Se ha eliminado correctamente!")
    elif confirmar == "n" and "N":
        print("\n>>> No se eliminó nada... ")

# --- fin de eliminar ---