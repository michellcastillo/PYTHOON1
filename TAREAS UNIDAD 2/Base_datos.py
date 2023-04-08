import sqlite3

# Nos conectamos a la base de datos (si no existe la crea)
conectar = sqlite3.connect("Base_datos.db")

# Creamos (si no existe) una tabla creada alumnos con sus campos
conectar.execute("""create table if not exists alumnos(
                    id integer primary key AUTOINCREMENT,
                    Nombre varchar, Apellido varchar, Semestre varchar, Carrera varchar, Matricula integers)""")
conectar.close()
conectar = sqlite3.connect("Base_datos.db")

# Insertamos dos alumnos
conectar.execute("Insert into alumnos(Nombre, Apellido, Matricula, Semestre, Carrera) values(?,?,?,?,?)",
                 ("Michell", "Franco", "Segundo", "Sistemas", 324))
conectar.execute("Insert into alumnos(Nombre, Apellido, Matricula, Semestre, Carrera) values(?,?,?,?,?)",
                 ("Christopher", "Garcia", "Segundo", "Sistemas", 123))

# Este es necesario para que se ejecuten las consultas anteriores
conectar.commit()

# Recuperamos un elementos de la tabla alumnos y lo imprimimos
alumno = conectar.execute("select * from alumnos where Nombre= 'Michell'")

# Esto es para solamente traer el primero o bien para traer uno
fila = alumno.fetchone()

#imprimimos la fila (el alumno)
print(fila)

# Cerramos la conexión con SQLITE
conectar.close()

#CONECTAMOS OTRA TABLA:
conectar = sqlite3.connect("Base_datos.db")
conectar.execute("""create table if not exists maestros(
                    id integer primary key AUTOINCREMENT,
                    Nombre varchar, Apellido varchar, Materia varchar)""")

conectar.close()

conectar = sqlite3.connect("Base_datos.db")
# Insertamos dos maestros
conectar.execute("Insert into maestros(Nombre, Apellido, Materia) values(?,?,?)",
                 ("Ligia", "Chuc", "Programación orientado a objetos"))

conectar.execute("Insert into maestros(Nombre, Apellido, Materia) values(?,?,?)",
                 ("Alejandro", "Sagundo", "Tutorias"))
conectar.commit()

# Recuperamos un elementos de la tabla maestros y lo imprimimos
maestro = conectar.execute("select * from maestros where Nombre= 'Ligia'")

# Esto es para solamente traer el primero o bien para traer uno
fila = maestro.fetchone()
#imprimimos la fila (el alumno)
print(fila)
# Cerramos la conexión con SQLITE
conectar.close()