#problema4

import requests
import sqlite3
from pymongo import MongoClient

# URL de la API de SUNAT
url = 'https://api.apis.net.pe/v2/sunat/tipo-cambio'

# Parámetros para obtener los datos de 2023
params = {'fecha': '2023'}

# Realizar solicitud a la API
response = requests.get(url, params=params)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
else:
    print('Error al obtener datos de la API')
    data = None

# Almacenar los datos en SQLite
if data:
    # Conexión a la base de datos SQLite
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    # Crear la tabla 'sunat_info' si no existe
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sunat_info (
        fecha TEXT PRIMARY KEY,
        compra REAL,
        venta REAL
    )
    ''')

    # Insertar los datos obtenidos desde la API en la base de datos SQLite
    for item in data:
        fecha = item['fecha']
        compra = item['compra']
        venta = item['venta']
        
        # Insertar los datos en la tabla
        cursor.execute('''
        INSERT OR REPLACE INTO sunat_info (fecha, compra, venta)
        VALUES (?, ?, ?)
        ''', (fecha, compra, venta))

    # Confirmar cambios
    conn.commit()

    # Mostrar el contenido de la tabla SQLite
    cursor.execute('SELECT * FROM sunat_info')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    
    conn.close()

# Almacenar los datos en MongoDB
if data:
    # Conexión a MongoDB
    client = MongoClient('mongodb+srv://carhuaye:L24YbryQ8UqVZbt0@dev.ongthij.mongodb.net/?retryWrites=true&w=majority&appName=Dev')
    db = client['tipo_cambio_db']
    collection = db['sunat_info']

    # Insertar los datos en MongoDB
    for item in data:
        documento = {
            'fecha': item['fecha'],
            'compra': item['compra'],
            'venta': item['venta']
        }
        collection.update_one({'fecha': item['fecha']}, {'$set': documento}, upsert=True)

    # Mostrar el contenido de MongoDB
    for doc in collection.find():
        print(doc)

    # Cerrar la conexión a MongoDB
    client.close()
