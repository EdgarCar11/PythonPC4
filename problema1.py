""""
Tienes un fichero temperaturas.txt que contiene registros de temperaturas diarias en formato 
CSV. Cada línea del fichero tiene la siguiente estructura: fecha,temperatura. Debes leer el 
fichero, calcular la temperatura promedio, la temperatura máxima y la mínima. Finalmente, 
debes escribir los resultados en un nuevo fichero resumen_temperaturas.txt. 

"""

ruta_archivo = '/workspaces/PythonPC4/temperaturas.txt'

with open(ruta_archivo, 'r') as f:
    lineas_archivo = f.readlines() 

#Inicializamos las variables
temperaturas = []  

#Procesamos cada línea del archivo
for linea in lineas_archivo:
    linea = linea.strip()  # Eliminar saltos de línea y espacios extra
    fecha, temperatura = linea.split(',')  # Separar la fecha y la temperatura
    temperaturas.append(float(temperatura))  # Convertir la temperatura a flotante y agregarla a la lista

#Cálculos de estadísticas
temp_prom = sum(temperaturas) / len(temperaturas)  # Temperatura promedio
temp_max = max(temperaturas)  # Temperatura máxima
temp_min = min(temperaturas)  # Temperatura mínima

#Ruta del archivo de salida
ruta_salida = '/workspaces/PythonPC4/resumen_temperaturas.txt'

#Escribir los resultados en un nuevo archivo
with open(ruta_salida, 'w') as f:
    f.write(f'Temperatura Promedio: {temp_prom:.2f} °C\n')
    f.write(f'Temperatura Máxima: {temp_max:.2f} °C\n')
    f.write(f'Temperatura Mínima: {temp_min:.2f} °C\n')



  

