#PROBLEMA 2

import os

#tabla de multiplicar
def guardar_tabla_multiplicar(n):
    #número esté entre 1 y 10
    if n < 1 or n > 10:
        print('El número debe estar entre 1 y 10')
        return
    #ruta del archivo
    ruta_archivo = f'tabla-{n}.txt'
    
    #informacion dentro de archivo texto
    with open(ruta_archivo, 'w') as f:
        for i in range(1, 11):
            f.write(f'{n} x {i} = {n * i}\n')
    
# Función para leer y mostrar la tabla de multiplicar desde un archivo
def mostrar_tabla_multiplicar(n):
    # Ruta del archivo
    ruta_archivo = f'tabla-{n}.txt'
    
    # Intentamos abrir el archivo y mostrar su contenido
    try:
        with open(ruta_archivo, 'r') as f:
            print(f'\nTabla de multiplicar del {n}:')
            print(f.read())
    except FileNotFoundError:
        print(f'El archivo {ruta_archivo} no existe.')

# Función para leer una línea específica (m) de la tabla de multiplicar
def mostrar_linea_tabla(n, m):
    # Ruta del archivo
    ruta_archivo = f'tabla-{n}.txt'
    
    # Intentamos abrir el archivo y leer la línea m
    try:
        with open(ruta_archivo, 'r') as f:
            lineas = f.readlines()
            
            # Verificamos que la línea m exista en el archivo
            if m < 1 or m > 10:
                print('El número de la línea debe estar entre 1 y 10.')
                return
            
            # Mostramos la línea m (restamos 1 porque las listas comienzan en 0)
            print(f'\nLínea {m} de la tabla del {n}: {lineas[m-1].strip()}')
    except FileNotFoundError:
        print(f'El archivo {ruta_archivo} no existe.')

#función principal
def opciones():
    while True:
        print('\n ELIGA UNA OPCION ')
        print('1. Guardar la tabla de multiplicar de un número')
        print('2. Mostrar la tabla de multiplicar de un número')
        print('3. Mostrar una línea específica de la tabla')
        print('4. Salir')

        try:
            opcion = int(input('Seleccione una opción: '))
            
            if opcion == 1:
                # Opción 1: Guardar la tabla
                n = int(input('Ingrese un número entre 1 y 10: '))
                guardar_tabla_multiplicar(n)
            
            elif opcion == 2:
                # Opción 2: Mostrar la tabla
                n = int(input('Ingrese un número entre 1 y 10 para mostrar la tabla: '))
                mostrar_tabla_multiplicar(n)
            
            elif opcion == 3:
                # Opción 3: Mostrar una línea específica de la tabla
                n = int(input('Ingrese un número entre 1 y 10 para la tabla: '))
                m = int(input('Ingrese el número de la línea entre 1 y 10: '))
                mostrar_linea_tabla(n, m)
            
            elif opcion == 4:
                #salir del programa
                print('FIN')
                break
            
            else:
                print('Opción no válida, intente de nuevo.')
        
        except ValueError:
            print('Por favor, ingrese un número válido.')

#ejecutamos
opciones()
