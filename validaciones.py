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

            