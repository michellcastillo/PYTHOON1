import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
import sqlite3


def conectar_db():
    conexion = sqlite3.connect("Registro_Basedata.db")
    conexion.execute("""
                create table if not exists alumnos(
                    id integer primary key AUTOINCREMENT,
                    NOMBRE varchar, APELLIDO varchar, CARRERA varchar, MATRICULA integer)
    """)
    conexion.close()

def guardar_alumno():
    conexion = sqlite3.connect("Registro_Basedata.db")
    if NOMBRE.get() == "" or APELLIDO.get() == "" or CARRERA.get() == "" or MATRICULA.get() == "":
        messagebox.showerror("ERROR", "COM´PLETE TODOS LOS CAMPOS")
        return
    int_MATRICULA = int(MATRICULA.get())
    print(int_MATRICULA)
    print(NOMBRE.get())
    print(APELLIDO.get())
    print(CARRERA.get())
    conexion.execute("insert into alumnos(NOMBRE, APELLIDO, CARRERA, MATRICULA) values (?,?,?,?)",
                     (NOMBRE.get(), APELLIDO.get(), CARRERA.get(), int_MATRICULA))
    conexion.commit()
    conexion.close()
    ventana_nuevo.destroy()
    actualiza_listado()


def get_alumnos():
    conexion = sqlite3.connect("Registro_Basedata.db")
    cursor = conexion.cursor()
    registros_raw = cursor.execute("select * from alumnos")
    registros_fetch = registros_raw.fetchall()
    print(registros_fetch)
    global registros
    registros = registros_fetch
    cursor.close()


def actualiza_listado():
    registros_lb.delete(0, tk.END)
    get_alumnos()
    for registro in registros:
        registros_lb.insert(tk.END, registro)

def nuevo_alumno (event=None):
    ventana_nuevo_alumno = tk.Toplevel(ventana)
    ventana_nuevo_alumno.title("REGISTRO")
    ventana_nuevo_alumno.geometry("500x500")
    ventana_nuevo_alumno.configure(bg="wheat1")

    titulo = tk.Label(ventana_nuevo_alumno, text="REGISTRO DE ALUMNOS", fg="black", bg="wheat1", font=("Arial", 20, "bold"),
                   pady=15).pack()

    imagen_registro = Image.open(r"C:\Users\miche\PycharmProjects\PYCHARMich\TAREAS UNIDAD 2\registro.png")
    nueva_imagen = imagen_registro.resize((90, 90))
    render = ImageTk.PhotoImage(nueva_imagen)
    label_imagen = tk.Label(ventana_nuevo_alumno, image=render)
    label_imagen.image = render
    label_imagen.config(bg="wheat1")
    label_imagen.pack(pady=2)

    marco = tk.LabelFrame(ventana_nuevo_alumno, text="REGISTRO: ", bg="bisque2", font=("Arial", 15, "bold"), pady=10)
    marco.config(bd=2, bg="bisque2")
    marco.pack()

    # Crear la etiqueta y el campo de entrada para el nombre
    NOMBRE_label = tk.Label(marco, text="NOMBRE:", bg="bisque2", font=("Arial", 12, "bold"))
    NOMBRE_label.grid(row=0, column=0, sticky='s', padx=10,)
    NOMBRE_entry = tk.Entry(marco, width=20, font=("Arial", 12))
    NOMBRE_entry.grid(row=0, column=1,sticky='s', padx=10, pady=10)

    APELLIDO_label = tk.Label(marco, text="APELLIDO:", bg="bisque2", font=("Arial", 12, "bold"))
    APELLIDO_label.grid(row=1, column=0, sticky='s', padx=10, pady=10)
    APELLIDO_entry = tk.Entry(marco, width=20, font=("Arial", 12 ))
    APELLIDO_entry.grid(row=1, column=1, sticky='s', padx=10, pady=10)

    CARRERA_label = tk.Label(marco, text="CARRERA:", bg="bisque2", font=("Arial", 12, "bold"))
    CARRERA_label.grid(row=2, column=0, sticky='s', padx=10, pady=10)
    CARRERA_entry = tk.Entry(marco,width=20, font=("Arial", 12 ) )
    CARRERA_entry.grid(row=2, column=1, sticky='s', padx=10, pady=10)

    MATRICULA_label = tk.Label(marco, text="MATRICULA:",bg="bisque2", font=("Arial", 12, "bold"))
    MATRICULA_label.grid(row=3, column=0, sticky='s', padx=10, pady=10)
    MATRICULA_entry = tk.Entry(marco, width=20, font=("Arial", 12 ))
    MATRICULA_entry.grid(row=3, column=1, sticky='s', padx=10, pady=10)

    global NOMBRE
    NOMBRE = NOMBRE_entry
    global APELLIDO
    APELLIDO = APELLIDO_entry
    global CARRERA
    CARRERA = CARRERA_entry
    global MATRICULA
    MATRICULA = MATRICULA_entry

    global ventana_nuevo
    ventana_nuevo = marco

    # Crear el botón para enviar los datos
    submit_button = tk.Button(ventana_nuevo, text="Guardar",bg="white", font=("Arial", 12, "bold"), command=guardar_alumno)
    submit_button.grid(row=5, column=0, columnspan=2, pady=10, padx=10)


conectar_db()
get_alumnos()
ventana = tk.Tk()
ventana.title("Control de Alumnos")
ventana.config(width=400, height=300, bg="bisque2")
barra_menus = tk.Menu()
# Crear el primer menú.
menu_alumnos = tk.Menu(barra_menus, tearoff=False)
# Agregarlo a la barra.
barra_menus.add_cascade(menu=menu_alumnos, label="ALUMNOS")
menu_alumnos.add_command(label="REGISTRAR ALUMNO", accelerator="Ctrl+N", command=nuevo_alumno)
ventana.config(menu=barra_menus)

registros_lb = tk.Listbox(ventana)
for registro in registros:
    registros_lb.insert(tk.END, registro)

registros_lb.pack(pady=30, padx=30)
registros_lb.configure(width=50, height=20)
ventana.bind_all("<Control-n>", nuevo_alumno)
ventana.mainloop()

