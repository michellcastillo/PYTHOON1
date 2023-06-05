from tkinter import *
from tkinter import ttk
from tkinter import messagebox, Tk
import mysql.connector
import tkinter as tk
from PIL import ImageTk, Image
from subprocess import call
import sys

#VENTANA DEL CRUD
def ventanaingresar():
   ventanaprincipal.destroy()

   # CONECTAR LA BASE DE DATOS
   try:
      db = mysql.connector.connect(
         host="localhost",
         user="root",
         password="",
         database="escuela"
      )
   except mysql.connector.Error as e:
      messagebox.showerror("ERROR", f"NO SE PUDO CONECTAR LA BASE DE DATOS: {e}")
      exit()

   # CREAR LA TABLA ALUMNO SI NO EXISTE
   cursor = db.cursor()
   cursor.execute(
      "CREATE TABLE IF NOT EXISTS alumnos (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), apellido VARCHAR(250), edad INT, carrera VARCHAR(250), semestre VARCHAR(250), email VARCHAR(255))")

   # FUNCIÓN PARA LEER TODOS LOS ALUMNOS EN LA BASE DE DATOS
   def leer_alumnosDB():
      cursor = db.cursor()
      cursor.execute("SELECT * FROM alumnos")
      return cursor.fetchall()

   # FUNCIÓN PARA AGREGAR UN NUEVO ALUMNO A ALA BASE DE DATOS
   def agregar_alumnoDB(nombre, apellido, edad, carrera, semestre, email):
      try:
         cursor = db.cursor()
         cursor.execute(
            "INSERT INTO alumnos (nombre, apellido,edad,carrera, semestre, email) VALUES (%s, %s, %s, %s, %s, %s)",
            (nombre, apellido, edad, carrera, semestre, email))
         db.commit()
      except mysql.connector.Error as error:
         messagebox.showerror("ERROR AL AGREGAR AL ALUMNO", f"NO SE PUEDE AGREGAR AL ALUMNO: {error}")
      finally:
         cursor.close()

   # FUNCIÓN PARA ACTUALIZAR A UN ALUMNO EXISTENTE EN LA BASE DE DATOS
   def actualizar_alumnoDB(id, nombre, apellido, edad, carrera, semestre, email):
      iid = int(id)
      cursor = db.cursor()
      print(
         "UPDATE alumnos SET nombre = %s, apellido = %s,  edad = %s, carrera = %s, semestre = %s, email = %s WHERE id = %s",
         (nombre, apellido, edad, carrera, semestre, email, iid))
      cursor.execute(
         "UPDATE alumnos SET nombre = %s, apellido = %s, edad = %s, carrera = %s, semestre =%s, email = %s WHERE id = %s",
         (nombre, apellido, edad, carrera, semestre, email, iid))
      db.commit()

   # FUNCIÓN PARA ELIMINAR UN ALUMNO EXISTENTE DE LA BASE DE DATOS
   def eliminar_alumnoDB(id):
      cursor = db.cursor()
      cursor.execute("DELETE FROM alumnos WHERE id = %s", (id,))
      db.commit()

   # FUNCIÓN PARA MOSTRAR LA LISTA DE TODOS LOS ALUMNOS
   def mostrar_alumnos():
      # Limpiar la tabla
      for widget in tabla_alumnos.winfo_children():
         widget.destroy()

      # OBTENER A LOS ALUMNOS
      alumnos = leer_alumnosDB()

      # MOSTRAR A LOS ALUMNOS EN LA TABLA
      for i, alumno in enumerate(alumnos):
         id = alumno[0]
         nombre = alumno[1]
         apellido = alumno[2]
         edad = alumno[3]
         carrera = alumno[4]
         semestre = alumno[5]
         email = alumno[6]

         Label(tabla_alumnos, text=id).grid(row=i, column=0)
         Label(tabla_alumnos, text=nombre).grid(row=i, column=1)
         Label(tabla_alumnos, text=apellido).grid(row=i, column=2)
         Label(tabla_alumnos, text=edad).grid(row=i, column=3)
         Label(tabla_alumnos, text=carrera).grid(row=i, column=4)
         Label(tabla_alumnos, text=semestre).grid(row=i, column=5)
         Label(tabla_alumnos, text=email).grid(row=i, column=6)

   # FUNCIÓN PARA AGREGAR UN NUEVO ALUMNO
   def agregar_alumno():
      # OBTENCIÓN DE DATOS DEL ALUMNO
      nombre = entrada_nombre.get()
      apellido = entrada_apellido.get()
      edad = entrada_edad.get()
      carrera = entrada_carrera.get()
      semestre = entrada_semestre.get()
      email = entrada_email.get()

      # VALIDAR CADA CAMPO QUE NO SE ENCUENTRE VACIO Y QUE SEAN LOS CARACTERES CORRESPONDIENTES
      if not nombre or not apellido or not edad or not carrera or not semestre or not email:
         messagebox.showerror("ERROR AL AGREGAR AL ALUMNO", "POR FAVOR INGRESE TODOS LOS DATOS DEL ALUMNO")

      elif not nombre.replace('', "").isalpha():
         messagebox.showerror("ERROR", "SOLO SE PERMITEN LETRAS EN EL NOMBRE, INTENTALO DE NUEVO")

      elif not apellido.replace('', "").isalpha():
         messagebox.showerror("ERROR", "SOLO SE PERMITEN LETRAS EN EL APELLIDO, INTENTALO DE NUEVO")

      elif not edad.isdigit():
         messagebox.showerror("ERROR", "SOLO SE PERMITEN NÚMEROS EN LA EDAD, INTENTALO DE NUEVO")
         return
      elif not carrera.replace('', "").isalpha():
         messagebox.showerror("ERROR", "SOLO SE PERMITEN LETRAS EN LA CARRERA, INTENTALO DE NUEVO")
         return
      elif not semestre.replace('', "").isalpha():
         messagebox.showerror("ERROR", "SOLO SE PERMITEN LETRAS EN EL SEMESTRE, INTENTALO DE NUEVO")
         return
      elif email == "":
         messagebox.showerror("ERROR", "NO SE A INGRESADO UN EMAIL, INTENTALO DE NUEVO")
         return
      else:


      # AGREGAR UN NUEVO ALUMNO
       agregar_alumnoDB(nombre, apellido, edad, carrera, semestre, email)

      # LIMPIAR LOS CAMPOS DE ENTRADA
      entrada_nombre.delete(0, END)
      entrada_apellido.delete(0, END)
      entrada_edad.delete(0, END)
      entrada_carrera.delete(0, END)
      entrada_semestre.delete(0, END)
      entrada_email.delete(0, END)

      # MOSTRAR LA LISTA DE ACTUALIZACIÓN DE LOS ALUMNOS
      mostrar_alumnos()

   # FUNCIÓN PARA ACTUALIZAR A UN ALUMNO EXISTENTE
   def actualizar_alumno():
      # OBTENER LOS DATOS DEL ALUMNO A ACTUALIZAR
      nombre = entrada_nombre.get()
      apellido = entrada_apellido.get()
      edad = entrada_edad.get()
      carrera = entrada_carrera.get()
      semestre = entrada_semestre.get()
      email = entrada_email.get()
      id = entrada_id.get()

      # VALIDAR QUE LOS CAMPOS NO ESTEN VACIOS
      if not id or not nombre or not apellido or not edad or not carrera or not semestre or not email:
         messagebox.showerror("ERROR AL ACTUALIZAR AL ALUMNO", "POR FAVOR INGRESE TODOS LOS DATOS DE ALUMNO")
         return

      # ACTUALIZAR AL ALUMNO
      actualizar_alumnoDB(id, nombre, apellido, edad, carrera, semestre, email)

      # LIMPIAR LOS CAMPOS DE ENTRADA
      entrada_id.delete(0, END)
      entrada_nombre.delete(0, END)
      entrada_apellido.delete(0, END)
      entrada_edad.delete(0, END)
      entrada_carrera.delete(0, END)
      entrada_semestre.delete(0, END)
      entrada_email.delete(0, END)

      # MOSTRAR LA LISTA DE ACTUALIZACIÓN DE ALUMNOS
      mostrar_alumnos()

   # FUNCIÓN PARA ELIMINAR UN ALUMNO EXISTENTE
   def eliminar_alumno():
      # OBTENER EL ID DEL ALUMNO A ELIMINAR
      id = entrada_id.get()

      # VALIDAR QUE HAYA INGRESADO EL ID
      if not id:
         messagebox.showerror("ERROR AL ELIMINAR EL ALUMNO", "PORFAVOR INGRESE EL ID DEL ALUMNO A ELIMINAR")
         return

      # PREGUNTAR AL USUARIO SI QUIERE ELIMINAR AL ALUMNO
      confirmar = messagebox.askyesno("CONFIRMAR ELIMINACIÓN", "¿ESTÁS SEGURO QUE DESEA ELIMINAR ESTÉ ALUMNO?")

      if confirmar:
         # ELIMINAR ALUMNO
         eliminar_alumnoDB(id)

         # LIMPIAR LOS CAMPOS DE ENTRADA
         entrada_id.delete(0, END)
         entrada_nombre.delete(0, END)
         entrada_apellido.delete(0, END)
         entrada_edad.delete(0, END)
         entrada_carrera.delete(0, END)
         entrada_semestre.delete(0, END)
         entrada_email.delete(0, END)

         # MOSTRAR LA LISTA DE ACTUALIZACIÓN DE ALUMNOS
         mostrar_alumnos()

      # VALIDACIÓN
   def validate_id(new_text):
      if not new_text:
         return True
      try:
         if int(new_text) >= 0 and len(new_text) <= 2:
            return True
         else:
            return False
      except ValueError:
         return False

   def validate_nombre(text):
      return text.isalpha() and len(text) <= 10

   def validate_apellido(text):
      return text.isalpha() and len(text) <= 10

   def validate_edad (new_text):
      if not new_text:
         return True
      try:
         if int(new_text) >= 0 and len(new_text) <= 2:
            return True
         else:
            return False
      except ValueError:
         return False


   def salir():
      ventana.destroy()
      call([sys.executable,r"C:\Users\miche\PycharmProjects\PYCHARMich\TAREAS UNIDAD 3\CRUD_MEJORADO.py"])
      # Crear la ventana principal

   ventana = Tk()
   ventana.title("CRUD")
   ventana.geometry("700x500")
   ventana.config(bg="thistle")

   # CREE UN MARCO PARA QUE SE VEA MEJOR ESTETICAMENTE Y MAS ORGANIZADO
   marco = LabelFrame(ventana, text=" INGRESA TUS DATOS", bg="azure", font=("Arial", 15, "bold"), pady=10)
   marco.config(bd=2)
   marco.pack()



   # Crear los campos de entrada para los datos del alumno
   Label(marco, text="ID:", bg="azure").grid(row=0, column=0, padx=5, pady=5)
   vcmd = (marco.register(validate_id), '%P')
   entrada_id = Entry(marco, validate="key", validatecommand=vcmd)
   entrada_id.grid(row=0, column=1, padx=5, pady=5)

   Label(marco, text="NOMBRE:", bg="azure").grid(row=1, column=0, padx=5, pady=5)
   entrada_nombre = Entry(marco, validate="key", validatecommand=(marco.register(validate_nombre), '%P'))
   entrada_nombre.grid(row=1, column=1, padx=5, pady=5)

   Label(marco, text="APELLIDO:", bg="azure").grid(row=2, column=0, padx=5, pady=5)
   entrada_apellido = Entry(marco, validate="key", validatecommand=(marco.register(validate_apellido), '%P'))
   entrada_apellido.grid(row=2, column=1, padx=5, pady=5)

   Label(marco, text="EDAD:", bg="azure").grid(row=3, column=0, padx=5, pady=5)
   vcmd4 = (marco.register(validate_edad), '%P')
   entrada_edad = Entry(marco, validate="key", validatecommand=vcmd4)
   entrada_edad.grid(row=3, column=1, padx=5, pady=5)

   Label(marco, text="CARRERA:", bg="azure").grid(row=4, column=0, padx=5, pady=5)
   entrada_carrera = ttk.Combobox(marco,values=["Sistemas", "Electromecanica", "Administracion", "Renovables","Animacion"],width=18, state="readonly")
   entrada_carrera.current(0)
   entrada_carrera.grid(row=4, column=1, padx=5, pady=5)

   Label(marco, text="SEMESTRE:", bg="azure").grid(row=5, column=0, padx=5, pady=5)
   entrada_semestre = ttk.Combobox(marco, values=["Segundo", "Cuarto", "Sexto", "Octavo", "Alumno Irregular"],width=18, state="readonly")
   entrada_semestre.current(0)
   entrada_semestre.grid(row=5, column=1, padx=5, pady=5)

   Label(marco, text="EMAIL:", bg="azure").grid(row=6, column=0, padx=5, pady=5)
   entrada_email = Entry(marco)
   entrada_email.grid(row=6, column=1, padx=7, pady=5)

   # Crear los botones para agregar, actualizar y eliminar alumnos
   Button(marco, text="AGREGAR ALUMNO", bg="thistle", command=agregar_alumno).grid(row=8, column=0, padx=5, pady=5)
   Button(marco, text="ACTUALIZAR ALUMNO", bg="thistle", command=actualizar_alumno).grid(row=8, column=1, padx=5,pady=5)
   Button(marco, text="ELIMINAR ALUMNO", bg="thistle", command=eliminar_alumno).grid(row=8, column=2, padx=5, pady=5)

   marcofalso = LabelFrame(ventana, text="", )
   marcofalso.config(bd=0, bg="thistle")
   marcofalso.pack()
   Button(marcofalso, text="SALIR", bg="azure", command=salir).grid(row=9, pady=5)

   marco2 = LabelFrame(ventana, text="DATOS DEL ALUMNO", bg="azure", font=("Arial", 15, "bold"), pady=5)
   marco2.config(bd=2, bg="azure")
   marco2.pack()

   # Crear la tabla para mostrar los alumnos
   tabla_alumnos = Frame(marco2)
   tabla_alumnos.config(bg="azure")
   tabla_alumnos.grid(row=1, column=0, columnspan=100, padx=5, pady=5)

   Label(marco2, text="NOMBRE  APELLIDO  EDAD  CARRERA  SEMESTRE    EMAIL                                  ID",
         bg="azure").grid(row=0, column=0)

   Label(tabla_alumnos, text="ID").grid(row=1, column=0)
   Label(tabla_alumnos, text="Nombre").grid(row=1, column=1)
   Label(tabla_alumnos, text="Apellido").grid(row=1, column=2)
   Label(tabla_alumnos, text="Edad").grid(row=1, column=3)
   Label(tabla_alumnos, text="Carrera").grid(row=1, column=4)
   Label(tabla_alumnos, text="Semestre").grid(row=1, column=5)
   Label(tabla_alumnos, text="Email").grid(row=1, column=6)

   mostrar_alumnos()

   # Iniciar el loop de la ventana
   ventana.mainloop()

def llam():
   global ventana2
   ventana2=tk.Toplevel(ventanaprincipal)
   ventana2.title("")
   ventana2.mainloop()

ventanaprincipal= tk.Tk()
ventanaprincipal.title("INICIO")
ventanaprincipal.config(bg="thistle")
ventanaprincipal.geometry("500x500")

titulo = Label(ventanaprincipal, text=" BIENVENIDOS", bg="thistle", font=("Arial", 25, "bold"), pady=10).pack()

imagen = Image.open(r"C:\Users\miche\PycharmProjects\PYCHARMich\TAREAS UNIDAD 3\yoshis.jpeg")
nueva_imagen = imagen.resize((200, 200))
render = ImageTk.PhotoImage(nueva_imagen)
label_imagen = Label(ventanaprincipal, image=render)
label_imagen.image = render
label_imagen.config(bg="azure")
label_imagen.pack(pady=10, padx=0, ipadx=0)

descripcion = Label(ventanaprincipal, text="PARA INGRESAR, PRESIONE EL BOTON", bg="thistle", font=("Arial", 9, "bold"), pady=12).pack()
Boton_ingresar=Button(ventanaprincipal,text="INGRESAR", bg="azure",  command=ventanaingresar, font=("Arial", 10, "bold"), pady="15")
Boton_ingresar.place(x=200,y=330, height=100, width=100)

ventanaprincipal.mainloop()




