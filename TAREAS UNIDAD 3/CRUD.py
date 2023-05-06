from tkinter import *
from tkinter import messagebox
import mysql.connector

# Conectar a la base de datos
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="escuela"
    )
except mysql.connector.Error as e:
    messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")
    exit()


# Crear la tabla de alumnos si no existe
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS alumnos (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), apellido VARCHAR(250), edad INT, carrera VARCHAR(250), semestre VARCHAR(250), email VARCHAR(255))")

# Función para leer todos los alumnos de la base de datos
def leer_alumnosDB():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM alumnos")
    return cursor.fetchall()

# Función para agregar un nuevo alumno a la base de datos
def agregar_alumnoDB(nombre, apellido, edad, carrera, semestre, email):
    try:
        cursor = db.cursor()
        cursor.execute("INSERT INTO alumnos (nombre, apellido,edad,carrera, semestre, email) VALUES (%s, %s, %s, %s, %s, %s)", (nombre, apellido, edad, carrera, semestre, email))
        db.commit()
    except mysql.connector.Error as error:
        messagebox.showerror("Error al agregar el alumno", f"No se pudo agregar el alumno: {error}")
    finally:
        cursor.close()


# Función para actualizar un alumno existente en la base de datos
def actualizar_alumnoDB(id, nombre, apellido, edad, carrera, semestre, email):
    iid = int(id)
    cursor = db.cursor()
    print("UPDATE alumnos SET nombre = %s, apellido = %s,  edad = %s, carrera = %s, semestre = %s, email = %s WHERE id = %s", (nombre, apellido, edad, carrera, semestre, email, iid))
    cursor.execute("UPDATE alumnos SET nombre = %s, apellido = %s, edad = %s, carrera = %s, semestre =%s, email = %s WHERE id = %s", (nombre, apellido, edad, carrera, semestre, email, iid))
    db.commit()

# Función para eliminar un alumno existente de la base de datos
def eliminar_alumnoDB(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM alumnos WHERE id = %s", (id,))
    db.commit()

# Función para mostrar una lista de todos los alumnos
def mostrar_alumnos():
    # Limpiar la tabla
    for widget in tabla_alumnos.winfo_children():
        widget.destroy()

    # Obtener todos los alumnos
    alumnos = leer_alumnosDB()

    # Mostrar los alumnos en la tabla
    for i, alumno in enumerate(alumnos):
        id = alumno[0]
        nombre = alumno[1]
        apellido =alumno[2]
        edad = alumno[3]
        carrera= alumno[4]
        semestre = alumno[5]
        email = alumno[6]

        Label(tabla_alumnos, text=id).grid(row=i, column=0)
        Label(tabla_alumnos, text=nombre).grid(row=i, column=1)
        Label(tabla_alumnos, text=apellido).grid(row=i, column=2)
        Label(tabla_alumnos, text=edad).grid(row=i, column=3)
        Label(tabla_alumnos, text=carrera).grid(row=i, column=4)
        Label(tabla_alumnos, text=semestre).grid(row=i, column=5)
        Label(tabla_alumnos, text=email).grid(row=i, column=6)

# Función para agregar un nuevo alumno
def agregar_alumno():
    # Obtener los datos del nuevo alumno
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    edad = entrada_edad.get()
    carrera = entrada_carrera.get ()
    semestre = entrada_semestre.get()
    email = entrada_email.get()

    # Validar que los campos no estén vacíos
    if not nombre or not apellido or not edad or not carrera or not semestre or not email:
        messagebox.showerror("Error al agregar el alumno", "Por favor ingrese todos los datos del alumno")

    elif not nombre.replace('',"").isalpha():
        messagebox.showerror("ERROR","SOLO LETRAS NO NUMEROS")

    elif not apellido.replace('',"").isalpha():
        messagebox.showerror("ERROR","SOLO LETRAS NO NUMEROS")

    elif not edad.isdigit():
        messagebox.showerror("ERROR","SOLO NUMEROS NO LETRAS")
        return
    elif not carrera.replace('',"").isalpha():
        messagebox.showerror("ERROR","SOLO LETRAS NO NUMEROS")
        return
    elif not semestre.replace('',"").isalpha():
        messagebox.showerror("ERROR","SOLO LETRAS NO NUMEROS")
        return
    elif not email.replace('',"").isalpha():
        messagebox.showerror("ERROR","SOLO LETRAS NO NUMEROS")
        return



    # Agregar el nuevo alumno
    agregar_alumnoDB(nombre, apellido, edad, carrera, semestre, email)

    # Limpiar los campos de entrada
    entrada_nombre.delete(0, END)
    entrada_apellido.delete(0, END)
    entrada_edad.delete(0, END)
    entrada_carrera.delete(0, END)
    entrada_semestre.delete(0,END)
    entrada_email.delete(0, END)

    # Mostrar la lista actualizada de alumnos
    mostrar_alumnos()

# Función para actualizar un alumno existente
def actualizar_alumno():
    # Obtener los datos del alumno a actualizar
    nombre = entrada_nombre.get()
    apellido =entrada_apellido.get()
    edad = entrada_edad.get()
    carrera = entrada_carrera.get()
    semestre = entrada_semestre.get()
    email = entrada_email.get()
    id = entrada_id.get()

    # Validar que los campos no estén vacíos
    if not id or not nombre or not apellido or not edad or not carrera or not semestre or not email:
        messagebox.showerror("Error al actualizar el alumno", "Por favor ingrese todos los datos del alumno")
        return

    # Actualizar el alumno
    actualizar_alumnoDB(id, nombre, apellido, edad, carrera, semestre, email)

    # Limpiar los campos de entrada
    entrada_id.delete(0, END)
    entrada_nombre.delete(0, END)
    entrada_apellido.delete(0,END)
    entrada_edad.delete(0, END)
    entrada_carrera.delete(0,END)
    entrada_semestre.delete(0,END)
    entrada_email.delete(0, END)

    # Mostrar la lista actualizada de alumnos
    mostrar_alumnos()


# Función para eliminar un alumno existente
def eliminar_alumno():
    # Obtener el ID del alumno a eliminar
    id = entrada_id.get()

    # Validar que se haya ingresado un ID
    if not id:
        messagebox.showerror("Error al eliminar el alumno", "Por favor ingrese el ID del alumno a eliminar")
        return

    # Preguntar al usuario si está seguro de eliminar el alumno
    confirmar = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de eliminar este alumno?")

    if confirmar:
        # Eliminar el alumno
        eliminar_alumnoDB(id)

        # Limpiar los campos de entrada
        entrada_id.delete(0, END)
        entrada_nombre.delete(0, END)
        entrada_apellido.delete(0, END)
        entrada_edad.delete(0, END)
        entrada_carrera.delete(0,END)
        entrada_semestre.delete(0,END)
        entrada_email.delete(0, END)

        # Mostrar la lista actualizada de alumnos
        mostrar_alumnos()


# Crear la ventana principal
ventana = Tk()
ventana.title("SQL")
ventana.geometry("700x500")
ventana.config(bg="thistle")

#CREE UN MARCO PARA QUE SE VEA MEJOR ESTETICAMENTE Y MAS ORGANIZADO
marco = LabelFrame(ventana, text=" INGRESA TUS DATOS", bg="azure", font=("Arial", 15, "bold"), pady=10)
marco.config(bd=2)
marco.pack()

# Crear los campos de entrada para los datos del alumno
Label(marco, text="Id:", bg="azure").grid(row=0, column=0, padx=5, pady=5)
entrada_id = Entry(marco)
entrada_id.grid(row=0, column=1, padx=5, pady=5)

Label(marco, text="Nombre:", bg="azure").grid(row=1, column=0, padx=5, pady=5)
entrada_nombre = Entry(marco)
entrada_nombre.grid(row=1, column=1, padx=5, pady=5)

Label(marco, text="Apellido:", bg="azure").grid(row=2, column=0, padx=5, pady=5)
entrada_apellido = Entry(marco)
entrada_apellido.grid(row=2, column=1, padx=5, pady=5)

Label(marco, text="Edad:", bg="azure").grid(row=3, column=0, padx=5, pady=5)
entrada_edad = Entry(marco)
entrada_edad.grid(row=3, column=1, padx=5, pady=5)

Label(marco, text="Carrera:", bg="azure").grid(row=4, column=0, padx=5, pady=5)
entrada_carrera = Entry(marco)
entrada_carrera.grid(row=4, column=1, padx=5, pady=5)

Label(marco, text="Semestre:", bg="azure").grid(row=5, column=0, padx=5, pady=5)
entrada_semestre = Entry(marco)
entrada_semestre.grid(row=5, column=1, padx=5, pady=5)

Label(marco, text="Email:", bg="azure").grid(row=6, column=0, padx=5, pady=5)
entrada_email = Entry(marco)
entrada_email.grid(row=6, column=1, padx=7, pady=5)

# Crear los botones para agregar, actualizar y eliminar alumnos
Button(marco, text="Agregar alumno",bg="thistle", command=agregar_alumno).grid(row=8, column=0, padx=5, pady=5)
Button(marco, text="Actualizar alumno", bg="thistle", command=actualizar_alumno).grid(row=8, column=1, padx=5, pady=5)
Button(marco, text="Eliminar alumno", bg="thistle", command=eliminar_alumno).grid(row=8, column=2, padx=5, pady=5)

marcofalso = LabelFrame(ventana, text="",)
marcofalso.config(bd=0,bg="thistle")
marcofalso.pack()
Label(marcofalso, text="", bg="thistle").grid(row=9, pady=5)


marco2 = LabelFrame(ventana, text="DATOS DEL ALUMNO", bg="azure", font=("Arial", 15, "bold"), pady=5)
marco2.config(bd=2, bg="azure")
marco2.pack()

# Crear la tabla para mostrar los alumnos
tabla_alumnos = Frame(marco2)
tabla_alumnos.config(bg="azure")
tabla_alumnos.grid(row=1, column=0, columnspan=100, padx=5, pady=5)

Label(marco2, text="Nombre  Apellido  Edad  Carrera  Semestre   Email                              ID", bg="azure").grid(row=0, column=0)

Label(tabla_alumnos, text="ID").grid(row=1, column=0)
Label(tabla_alumnos, text="Nombre").grid(row=1, column=1)
Label(tabla_alumnos, text="Apellido").grid(row=1, column=2)
Label(tabla_alumnos, text="Edad").grid(row=1, column=3)
Label(tabla_alumnos, text="Carrera").grid(row=1, column=4)
Label(tabla_alumnos, text="Semestre").grid(row=1, column=5)
Label(tabla_alumnos, text="Email").grid(row=1, column=6)

# Mostrar la lista de alumnos en la tabla
mostrar_alumnos()

# Iniciar el loop de la ventana
ventana.mainloop()