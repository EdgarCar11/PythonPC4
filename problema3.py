#PROBLEMA3

import os

def contar_lineas_codigo(ruta_archivo):
    try:
        # Verificamos si el archivo tiene la extensión .py
        if not ruta_archivo.endswith('.py'):
            print('El archivo no tiene extensión \'.py\'.')
            return

        # lee el archivo
        with open(ruta_archivo, 'r') as f:
            lineas = f.readlines()
        
        # Contador de líneas de código
        lineas_codigo = 0
        
        for linea in lineas:
            # Eliminamos los espacios en blanco al inicio y final
            linea = linea.strip()
            
            # Verificamos que la línea no sea vacía ni un comentario
            if linea and not linea.startswith('#'):
                lineas_codigo += 1
        
        print(f'El archivo: {ruta_archivo} tiene {lineas_codigo} lineas')

    except FileNotFoundError:
        print('El archivo no existe. Verifique la ruta y nombre.')
    except Exception as e:
        print(f'Ocurrió un error: {e}')

# Solicitamos la ruta del archivo al usuario
ruta_archivo = input('Ingrese la ruta del archivo .py(nombre y ruta): ')

# Llamamos a la función para contar las líneas de código
contar_lineas_codigo(ruta_archivo)
