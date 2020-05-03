# firebaseSDK-con-python

LIBRERIAS UTILIZADAS: requests, firebase-admin, Path

- main.py: es el script principal para ejecutar el programa.

- menu.py: es el script que le sigue a main, tiene un menú donde la primera opción es cargar el archivo .JSON (que es la llave de autenticación) e inicializar la app. La llave .JSON tiene que estar dentro de la carpeta "firebase" y dentro de firebase.py hay que modificar 'databaseURL' por el link de la base de datos (https://nombre de tu base de datos.firebaseio.com/).

- sdk.py: una vez que hayamos hecho correctamente la conexión, podemos empezar a operar con Firebase. 

- comandos_sdk.py: cualquier operación que hagamos en sdk.py se ejecutan dentro de comandos_sdk.py (dentro del mismo está comentado)

- validaciones.py: a la hora de añadir elementos a nuestra base de datos, podemos modificar éstos métodos a nuestro gusto para mayor seguridad y robustez del programa, así evitamos añadir valores erróneos a nuestra BD

- carpeta "autenticacion": ahí tienen que añadir su archivo .JSON para poder utilizar el programa
