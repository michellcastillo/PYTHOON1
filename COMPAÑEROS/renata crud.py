#Las mejoras realizaas son que, se le agregó un inicio de secion que tiene nombre de usuario,
# una vez ingresados correctamente, el boton de "iniciar" llevará a la segunda ventaana que es donde se encuentra el CRUD

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector



#SE CREA LA SEGUNDA VENTANA 2
def ventanacrud():
    root.destroy()
    Etiqueta = Tk()
    Etiqueta.title("STUDENT RECORD")
    Etiqueta.config(bg="MediumPurple4")
    Etiqueta.geometry("350x300")


    # Crear los campos de entrada para los datos del alumno
    Label(Etiqueta, text="Id:", bg="MediumPurple4").grid(row=0, column=0, padx=5, pady=5)
    entrada_id = Entry(Etiqueta)
    entrada_id.grid(row=0, column=1, padx=5, pady=5)

    Label(Etiqueta, text="Name:", bg="MediumPurple4").grid(row=1, column=0, padx=5, pady=5)
    entrada_nombre = Entry(Etiqueta)
    entrada_nombre.grid(row=1, column=1, padx=5, pady=5)

    Label(Etiqueta, text="Age:", bg="MediumPurple4").grid(row=2, column=0, padx=5, pady=5)
    entrada_edad = Entry(Etiqueta)
    entrada_edad.grid(row=2, column=1, padx=5, pady=5)

    Label(Etiqueta, text="Email:", bg="MediumPurple4").grid(row=3, column=0, padx=5, pady=5)
    entrada_email = Entry(Etiqueta)
    entrada_email.grid(row=3, column=1, padx=5, pady=5)


    # Función para agregar un nuevo alumno
    def agregar_alumno():


        # Obtener los datos del nuevo alumno
        nombre = entrada_nombre.get()
        edad = entrada_edad.get()
        email = entrada_email.get()


        # Validar que los campos no estén vacíos
        if not nombre or not edad or not email:
            messagebox.showerror("Error adding student", "Enter all student data")
            return


        # Agregar el nuevo alumno
        agregar_alumnoDB(nombre, edad, email)


        # Limpiar los campos de entrada y mostrar la lista actualizada de alumnos
        entrada_nombre.delete(0, END)
        entrada_edad.delete(0, END)
        entrada_email.delete(0, END)
        mostrar_alumnos()


    # Función para eliminar un alumno existente
    def eliminar_alumno():

        # Obtener el ID del alumno a eliminar
        id = entrada_id.get()

        # Validar que se haya ingresado un ID
        if not id:
            messagebox.showerror("Error deleting student", "Enter the ID of the student to delete")
            return


        # Preguntar al usuario si está seguro de eliminar el alumno
        confirmar = messagebox.askyesno("Confirm deletion", "¿Are you sure to delete the student?")

        if confirmar:
            # Eliminar el alumno
            eliminar_alumnoDB(id)

            # Limpiar los campos de entrada
            entrada_id.delete(0, END)
            entrada_nombre.delete(0, END)
            entrada_edad.delete(0, END)
            entrada_email.delete(0, END)

            # Mostrar la lista actualizada de alumnos
            mostrar_alumnos()



    # Función para actualizar un alumno existente
    def actualizar_alumno():
        # Obtener los datos del alumno a actualizar
        nombre = entrada_nombre.get()
        edad = entrada_edad.get()
        email = entrada_email.get()
        id = entrada_id.get()

        # Validar que los campos no estén vacíos
        if not id or not nombre or not edad or not email:
            messagebox.showerror("Error updating student", "Enter all student data")
            return

        # Actualizar el alumno
        actualizar_alumnoDB(id, nombre, edad, email)

        # Limpiar los campos de entrada
        entrada_id.delete(0, END)
        entrada_nombre.delete(0, END)
        entrada_edad.delete(0, END)
        entrada_email.delete(0, END)

        # Mostrar la lista actualizada de alumnos
        mostrar_alumnos()


    # Crear los botones para agregar, actualizar y eliminar alumnos
    Button(Etiqueta, text="Add student", command=agregar_alumno).grid(row=0, column=2, padx=5, pady=5)
    Button(Etiqueta, text="Update student", command=actualizar_alumno).grid(row=1, column=2, padx=5, pady=5)
    Button(Etiqueta, text="Eliminate student", command=eliminar_alumno).grid(row=2, column=2, padx=5, pady=5)


    # Crear la tabla para mostrar los alumnos
    tabla_alumnos = Frame(Etiqueta)
    tabla_alumnos.grid(row=4, column=0, columnspan=3, padx=5, pady=5)
    Label(tabla_alumnos, text="ID").grid(row=0, column=0)
    Label(tabla_alumnos, text="Name").grid(row=0, column=1)
    Label(tabla_alumnos, text="Age").grid(row=0, column=2)
    Label(tabla_alumnos, text="Email").grid(row=0, column=3)


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
    cursor.execute("CREATE TABLE IF NOT EXISTS alumnos (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), edad INT, email VARCHAR(255))")



    # Función para leer todos los alumnos de la base de datos
    def leer_alumnosDB():
        cursor = db.cursor()
        cursor.execute("SELECT * FROM alumnos")
        return cursor.fetchall()


    # Función para agregar un nuevo alumno a la base de datos
    def agregar_alumnoDB(nombre, edad, email):
        try:
            cursor = db.cursor()
            cursor.execute("INSERT INTO alumnos (nombre, edad, email) VALUES (%s, %s, %s)", (nombre, edad, email))
            db.commit()
        except mysql.connector.Error as error:
            messagebox.showerror("Error al agregar el alumno", f"No se pudo agregar el alumno: {error}")
        finally:
            cursor.close()


    # Función para actualizar un alumno existente en la base de datos
    def actualizar_alumnoDB(id, nombre, edad, email):
        iid = int(id)
        cursor = db.cursor()
        print("UPDATE alumnos SET nombre = %s, edad = %s, email = %s WHERE id = %s", (nombre, edad, email, iid))
        cursor.execute("UPDATE alumnos SET nombre = %s, edad = %s, email = %s WHERE id = %s",
                       (nombre, edad, email, iid))
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
            edad = alumno[2]
            email = alumno[3]

            Label(tabla_alumnos, text=id).grid(row=i, column=0, )
            Label(tabla_alumnos, text=nombre).grid(row=i, column=1)
            Label(tabla_alumnos, text=edad).grid(row=i, column=2)
            Label(tabla_alumnos, text=email).grid(row=i, column=3)
                                                             #AQUI SE CREA LA VENTANA 1

#CREAR EL INICIO DE SESION
def insesion():
    if contrasena_usuario.get() == "0622" and nombre_usuario.get() == "Renata":
            ventanacrud()
    else:
        messagebox.showerror(message="Wrong username or password", title="Ups...")





            #SE CREA LA VENTANA 1
global root
root = Tk()
root.state(newstate = "normal")
root.geometry("300x300")
root.resizable(5, 5)
root.title("LOGIN")
root.config(bg="MediumPurple1")
miEtiqueta1 = Label(root, text="Welcome to register students", bg="purple4", font=("Times New Roman", 13), fg="gray1")
miEtiqueta1.pack()



#SE CREAN LOS COMPOS PARA EL USUARIO Y LA CONTRASEÑA
global nombre_usuario
global contrasena_usuario

nombre_usuario = tk.Entry(root)
label= tk.Label (text="User")
label.config (fg= "Black", bg="MediumPurple1", font=("Times New Roman", 13))
label.pack (padx=0)
nombre_usuario.pack(pady=10)

contrasena_usuario = tk.Entry(root, show="★")
label= tk.Label ( text= "Password")
label.config (fg= "Black", bg="MediumPurple1",font=("Times New Roman", 13) )
label.pack (pady=0)
contrasena_usuario.pack(pady=10)


iniciar_sesion = Button(root, text="Log in", bg="white", font= ("Times New Roman", 11), fg="Black", command=insesion )
iniciar_sesion.place(x=160, y=350)
iniciar_sesion.pack()
salir = tk.Button(root, text="Leave",  font= ("Times New Roman", 11), command=root.quit)
salir.pack()
salir.place(x=125, y=200)










root.mainloop()





