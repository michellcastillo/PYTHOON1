import sys
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
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


class Login_Principal:
    db_name='Main_alumno.db'

#CREAMOS LA VENTANA
    def __init__(self, ventanalogin):
        self.ventana=ventanalogin
        self.ventana.title("LOGIN")
        self.ventana.geometry("680x500")
        self.ventana.resizable(0,0)
        self.ventana.config(bd=10, bg="azure")

        titulo= Label(ventanalogin, text="BIENVENIDO ",fg="black", bg="azure", font=("Arial", 25, "bold"),pady=15).pack()

        imagen_registro = Image.open(r"C:\Users\miche\PycharmProjects\PYCHARMich\TAREAS UNIDAD 2\Main_alumno\registro.png")
        nueva_imagen = imagen_registro.resize((120, 120))
        render = ImageTk.PhotoImage(nueva_imagen)
        label_imagen =Label(ventanalogin, image=render)
        label_imagen.image = render
        label_imagen.config(bg="azure")
        label_imagen.pack(pady=2)

        descripcion =Label(ventanalogin, text="Un gusto tenerte en este programa ingresa al registro que desees",fg="black", bg="azure", font=("Arial", 15, "bold"),pady=15).pack()


        #CREACION DE BOTONES
        frame_botones=Frame(ventanalogin)
        frame_botones.config(bg="azure" )
        frame_botones.pack()

        boton_registrar_alumno = Button(frame_botones, text="REGISTRO ALUMNO", command=self.formulario_alumno, height=2, width=20, bg="springgreen4", fg="white", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky='s', padx=10,pady=15,)
        boton_registrar_maestros =  Button(frame_botones, text="REGISTRO MAESTRO", command=self.formulario_maestro, height=2, width=20, bg="springgreen4", fg="white", font=("Arial", 12, "bold")).grid(row=1, column=1, sticky='s', padx=10,pady=15, )

    def validar_login(self,matricula,contrasena):
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            sql = f"SELECT * FROM REGISTRO WHERE matricula = {matricula} AND contraseña = '{contrasena}'"
            cursor.execute(sql)
            validacion = cursor.fetchall()  # obtener respuesta como lista
            cursor.close()
            return validacion


    def formulario_alumno(self):
        ventanalogin.destroy()
        call([sys.executable, r"C:\Users\miche\PycharmProjects\PYCHARMich\TAREAS UNIDAD 2\Main_alumno\Main_alumno_alumno.py"])

    def formulario_maestro(self):
        ventanalogin.destroy()
        call([sys.executable,r"C:\Users\miche\PycharmProjects\PYCHARMich\TAREAS UNIDAD 2\Main_alumno\Main_alumno_maestro.py"])

if __name__ == '__main__':
  ventanalogin = Tk()
  application = Login_Principal(ventanalogin)
  ventanalogin.mainloop()