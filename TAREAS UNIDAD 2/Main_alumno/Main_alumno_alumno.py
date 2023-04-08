import sys
from subprocess import call
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from subprocess import call

import sqlite3

def conectar_db():
    conexion = sqlite3.connect("Main_alumno.db")
    conexion.execute("""
                create table if not exists alumnos(
                    id integer primary key AUTOINCREMENT,
                    NOMBRE varchar, APELLIDO varchar, CARRERA varchar, MATRICULA integer)
    """)
    conexion.close()

class Tareas:
    db_name = 'Main_alumno.db'

    def __init__(self, ventana_tarea):
        self.window = ventana_tarea
        self.window.title("MIS TAREAS")
        self.window.geometry("900x670")
        self.window.resizable(0, 0)
        self.window.config(bd=10, bg="pink")


        titulo = Label(ventana_tarea, text="REGISTRATE", fg="black", bg="pink", font=("Arial", 20, "bold"), pady=10).pack()

        marco = LabelFrame(ventana_tarea, text="DATOS DEL ALUMNO", bg="pink", font=("Arial", 15, "bold"), pady=5)
        marco.config(bd=2, bg="pink")
        marco.pack()


        label_asignatura= Label(marco, text="NOMBRE: ", bg="pink", font=("Ariual", 12, "bold")).grid(row=0, column=0,sticky='s', padx=5,pady=9)
        self.combo_asignatura = Entry(marco, width=25, font=("Arial", 12, "bold"))
        self.combo_asignatura.grid(row=0, column=1, padx=5, pady=0)

        label_fecha = Label(marco, text="APELLIDO: ", bg="pink", font=("Arial", 12, "bold")).grid(row=1,column=0,sticky='s',padx=5,pady=8)
        self.fecha = Entry(marco, width=25, font=("Arial", 12, "bold"))
        self.fecha.grid(row=1, column=1, padx=5, pady=8)

        label_puntaje = Label(marco, text="CARRERA: ", bg="pink", font=("Arial", 12, "bold")).grid(row=2, column=0,sticky='s', padx=5,pady=8)
        self.puntaje = Entry(marco, width=25, font=("Arial", 12, "bold"))
        self.puntaje.grid(row=2, column=1, padx=5, pady=8)

        label_descripcion = Label(marco, text="MATRICULA: ", bg="pink", font=("Arial", 12, "bold")).grid(row=3, column=0,sticky='s',padx=5, pady=8)
        self.descripcion = Entry(marco, width=25, font=("Arial", 12, "bold"))
        self.descripcion.grid(row=3, column=1, padx=5, pady=8)

        frame_botones = Frame(ventana_tarea)
        frame_botones.config(bg="pink")
        frame_botones.pack()

        boton_registrar = Button(frame_botones, text="REGISTRAR",command=self.agregar_tareas, height=2, width=10,bg="mediumpurple1", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10,pady=15)
        boton_eliminar = Button(frame_botones, text="ELIMINAR", command=self.eliminar_asignatura,height=2, width=10,bg="mediumpurple1", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=10,pady=15)
        boton_eliminar = Button(frame_botones, text="REGRESAR", command=self.llamar_login, height=2, width=10,bg="mediumpurple1", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=4, padx=10,pady=15)

        "--------------- Tabla --------------------"
        self.tree = ttk.Treeview(height=15, columns=("columna1", "columna2", "columna3"))
        self.tree.heading("#0", text="NOMBRE", anchor=CENTER)
        self.tree.column("#0", width=90, minwidth=75, stretch=NO)

        self.tree.heading("columna1", text='APELLIDO', anchor=CENTER)
        self.tree.column("columna1", width=150, minwidth=75, stretch=NO)

        self.tree.heading("columna2", text='CARRERA', anchor=CENTER)
        self.tree.column("columna2", width=150, minwidth=75, stretch=NO)

        self.tree.heading("columna3", text='MATRICULA', anchor=CENTER)
        self.tree.column("columna3", width=150, minwidth=75, stretch=NO)

        self.tree.pack()
        self.Obtener_tareas()



    def Ejecutar_consulta(self, query, parameters=()):
            with sqlite3.connect(self.db_name) as conexion:
                cursor = conexion.cursor()
                result = cursor.execute(query, parameters)
                conexion.commit()
            return result

    def Validar_formulario_completo(self):
            if len(self.combo_asignatura.get()) != 0 and len(self.fecha.get()) != 0 and len(self.puntaje.get()) != 0 and  len(self.descripcion.get()) != 0:
                return True
            else:
                messagebox.showerror("ERROR", "COMPLETE TODOS LOS CAMPOS DEL FORMULARIUO")

    def Limpiar_formulario(self):
            self.combo_asignatura.delete(0, END)
            self.fecha.delete(0, END)
            self.puntaje.delete(0, END)
            self.descripcion.delete(0, END)

    def Obtener_tareas(self):
            records = self.tree.get_children()
            for element in records:
                self.tree.delete(element)
            query = 'SELECT * FROM alumnos ORDER BY NOMBRE desc'
            db_rows = self.Ejecutar_consulta(query)
            for row in db_rows:
                self.tree.insert("", 0, text=row[1], values=(row[2], row[3], row[4]))

    def agregar_tareas(self):
            if self.Validar_formulario_completo():
                query = 'INSERT INTO alumnos VALUES(NULL, ?, ?, ?, ?)'
                parameters = (self.combo_asignatura.get(), self.fecha.get(),self.puntaje.get(),self.descripcion.get())
                self.Ejecutar_consulta(query, parameters)
                messagebox.showinfo("REGISTRO EXITOSO", f'TAREA REGISTRADA DE LA MATERIA: {self.combo_asignatura.get()}')
                print('REGISTRADO')
            self.Limpiar_formulario()
            self.Obtener_tareas()

    def eliminar_asignatura(self):
            try:
                self.tree.item(self.tree.selection())['values'][0]
            except IndexError as e:
                messagebox.showerror("ERROR", "Porfavor selecciona un elemento")
                return
            dato = self.tree.item(self.tree.selection())['text']
            nombre = self.tree.item(self.tree.selection())['values'][0]
            query = "DELETE FROM alumnos WHERE NOMBRE = ?"
            respuesta = messagebox.askquestion("ADVERTENCIA", f"¿SEGURO QUE QUIERES ELIMINAR ESTÁ TAREA:?")
            if respuesta == 'yes':
                self.Ejecutar_consulta(query, (dato,))
                self.Obtener_tareas()
                messagebox.showinfo('ÉXITO', '¡FELICIDADES HAS COMPLETADO ESTÁ TAREA! :3')
            else:
                messagebox.showerror('ERROR', f'Error al eliminar la tarea')

    def llamar_login(self):
        ventana_tarea.destroy()
        call([sys.executable, r"C:\Users\miche\PycharmProjects\PYCHARMich\TAREAS UNIDAD 2\Main_alumno\Main_alumno.py"])




if __name__ == '__main__':
    ventana_tarea = Tk()
    application = Tareas(ventana_tarea)
    ventana_tarea.mainloop()