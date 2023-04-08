import mysql.connector
import tkinter as tk
from tkinter import ttk

try:
    conexion= mysql.connector.connect (host='localhost', user='root', passwd='', database='XAMPP')

except Exception as err:
    print ('ERROR CONECTANDO A LA BASE')
else:
    print('CONECTADO A MYSQL')
try:
    cursor = conexion.cursor()
    insertar="insert into mascotas values('Lucky', 'Gato', 'Siames', 'Michell')"
    cursor.execute(insertar)
    conexion.commit()
except Exception as err:
    print('ERROR AL INSERTAR LOS DATOS', err)
else:
    print('DATOS INGRESADOS CORRECTAMENTE')

#---------------------------------------------------------------------------------------------------
# Crear una consulta SQL para obtener los datos de la tabla
cursor = conexion.cursor()
cursor.execute("SELECT * FROM mascotas")

# Obtener los datos de la tabla y mostrarlos en la consola de PyCharm
for row in cursor.fetchall():
    print(row)

# Cerrar la conexión a la base de datos
conexion.close()
