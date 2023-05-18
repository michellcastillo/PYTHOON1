from tkinter import *
import tkinter as tk
from tkinter import messagebox, Entry
import sqlite3
import mysql.connector


# se crea la base de datos
def conectar_db():
    conexion = sqlite3.connect("Servicio2.db")
    conexion.execute("""
                create table if not exists clientes(
                    id integer primary key AUTOINCREMENT,
                    nombre varchar,
                    apellido varchar,
                    edad integer,
                    correo varchar,
                    contraseña varchar
                    direccion varchar,
                    raza varchar,
                    masc varchar,
                    ubi varchar,
                    servi varchar)
                    """)
    conexion.close()


# Funcion para la ventana de eleccion del usuario
def eleccion_usuario():
    ventana1 = tk.Tk()
    ventana1.configure(bg="beige")
    ventana1.resizable(width=False, height=False)
    # ventana1.iconbitmap("pet.ico")
    ventana1.title("Login cliente", )
    ventana1.configure(padx=100)
    mi_label5 = tk.Label(ventana1,
                         text="  Bienvenido a Pet World  ",
                         bg="beige", font=("Bahnschrift", 15))
    mi_label5.pack()
    mi_label6 = tk.Label(ventana1,
                         text=""" El objetivo principal de Pet World es brindar una atención médica
    de calidad y un servicio excepcional a las mascotas y sus dueños,
    nos esforzamos por crear un ambiente tranquilo y relajado para que
    las mascotas se sientan seguras y cómodas durante su visita  """,
                         bg="beige")
    mi_label6.pack()
    mi_label7 = tk.Label(ventana1,
                         text="""Pet World ofrece un servicio estetico de primera el cual incluye:
    baño y secado, corte de pelo, corte de garras, peinado y perfumado,
    etc, tambien ofrecemos un servicio medico muy completo
    como exámenes de salud regulares, vacunas, cirugía, análisis de laboratorio, 
    radiografías, pruebas de diagnóstico y tratamientos especializados para
    una amplia variedad de enfermedades y dolencias.  """,
                         bg="beige")
    mi_label7.pack()
    tk.Label(ventana1, text="  ", bg="beige",
             fg="black", width="20", height="1", font=("Bahnschrift", 15)).pack()
    mi_label8 = tk.Label(ventana1,
                         text="Registrar usuario",
                         bg="beige", font=("Bahnschrift", 15))
    mi_label8.pack()
    iniciar_Cliente = tk.Button(ventana1, text="Registrar", command=ubicaciones)
    iniciar_Cliente.pack(padx=40, pady=40)
    regresar = tk.Button(ventana1, text="Regresar", command=ventana1.destroy)
    regresar.pack(padx=40, pady=40)


conectar_db()


def tabla_admin():
    str_nameadmin = str(name.get())
    int_age = int(age.get())
    str_serv = str(serv.get())
    int_str_age = str(age.get())
    str_name = str(name.get())
    str_raza = str(raza.get())
    str_calle = str(calle.get())
    str_namemasc = str(namemasc.get())
    ventana24 = tk.Tk()
    ventana24.configure(bg="beige")
    ventana24.resizable(width=False, height=False)
    # ventana3.iconbitmap("pet.ico")
    ventana24.title("Ficha de cita", )
    ventana24.configure(padx=200)
    ventana24.configure(pady=50)
    marco = LabelFrame(ventana24, text="Datos de la cita agendada", font=("Comic Sans", 10, "bold"), bg="white")
    marco.config(bd=9, pady=9)
    marco.pack()
    # Crear la etiqueta y el campo de entrada de los datos
    persona = tk.Label(marco,
                       text="______________________________________________________________________________________________________",
                       bg="white", font=("Comic Sans", 10, "bold"))
    persona.grid(row=0, column=0, padx=(10, 0))
    persona2 = tk.Label(marco,
                        text="Nombre""          ""          ""Nombre de la mascota""          ""Raza         ""          ""Servicio""                  ""          Ubicacion""    ",
                        bg="white", font=("Comic Sans", 10, "bold"))
    persona2.grid(row=1, column=0, padx=(10, 0))
    persona6 = tk.Label(marco,
                        text="-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
                        bg="white", font=("Comic Sans", 10, "bold"))
    persona6.grid(row=2, column=0, padx=(10, 0))
    persona3 = tk.Label(marco,
                        text=str_name + "          ""          "        "     " + str_namemasc + "             " + str_raza + "                  " + str_serv + "                       " + str_calle + "    ",
                        bg="white", font=("Comic Sans", 10, "bold"))
    persona3.grid(row=3, column=0, padx=(10, 0))
    persona4 = tk.Label(marco,
                        text="                         ""        ""               ""      ""          ""          ""                    ""        ""                      ""  ",
                        bg="white", font=("Comic Sans", 10, "bold"))
    persona4.grid(row=4, column=0, padx=(10, 0))

    ventana24.mainloop()


def elec_serv():
    servx = str(serv.get())
    servicio1 = "corte de pelo"
    servicio2 = "Baño y secado"
    servicio3 = "corte de garras"
    servicio4 = "peinado y perfumado"
    servicio5 = "analisis"
    servicio6 = "esterilizacion"
    servicio7 = "interventiva"
    servicio8 = "vacunas"
    servicio9 = "radiografias"
    servicio10 = "prueba diagnostica"
    if servx != servicio1 and servx != servicio2 and servx != servicio3 and servx != servicio4 and servx != servicio5 and servx != servicio6 and servx != servicio7 and servx != servicio8 and servx != servicio9 and servx != servicio10:
        messagebox.showerror("Dato erroneo", "El servicio ingresado no es válido")
    else:
        conexion = sqlite3.connect("Servicio2.db")
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            db="Servicio2"
        )

        base = "INSERT INTO clientes (Nombre, Nombremasc, Ubi, Edad, Servicio, Raza) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
            name.get(), namemasc.get(), calle.get(), age.get(), serv.get(), raza.get())

        fcursor = db.cursor()
        consulta = "SELECT * FROM clientes"
        fcursor.execute(consulta)
        datos = fcursor.fetchall()
        print(datos)

        fcursor.execute(base)
        db.commit()
        db.close

        str_nameadmin = str(name.get())
        int_age = int(age.get())
        str_serv = str(serv.get())
        int_str_age = str(age.get())
        str_name = str(name.get())
        str_raza = str(raza.get())
        str_calle = str(calle.get())
        str_namemasc = str(namemasc.get())
        conexion.execute("insert into clientes(nombre,edad,raza,masc,ubi,servi) val1ues (?,?,?,?,?,?)",
                         (name.get(), int_age, raza.get(), namemasc.get(), calle.get(), serv.get()))
        conexion.commit()
        conexion.close()
        ventana_nuevo.destroy()
        "----------------------------------------------------------"
        ventana4 = tk.Tk()
        ventana4.configure(bg="beige")
        ventana4.resizable(width=False, height=False)
        # ventana3.iconbitmap("pet.ico")
        ventana4.title("Ficha de cita", )
        ventana4.configure(padx=200)
        ventana4.configure(pady=50)
        marco = LabelFrame(ventana4, text="Datos de la cita agendada", font=("Comic Sans", 10, "bold"), bg="white")
        marco.config(bd=9, pady=9)
        marco.pack()
        # Crear la etiqueta y el campo de entrada de los datos
        persona = tk.Label(marco,
                           text="______________________________________________________________________________________________________",
                           bg="white", font=("Comic Sans", 10, "bold"))
        persona.grid(row=0, column=0, padx=(10, 0))
        persona2 = tk.Label(marco,
                            text="Nombre""          ""          ""Nombre de la mascota""          ""Raza         ""          ""Servicio""                  ""          Ubicacion""    ",
                            bg="white", font=("Comic Sans", 10, "bold"))
        persona2.grid(row=1, column=0, padx=(10, 0))
        persona6 = tk.Label(marco,
                            text="-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
                            bg="white", font=("Comic Sans", 10, "bold"))
        persona6.grid(row=2, column=0, padx=(10, 0))
        persona3 = tk.Label(marco,
                            text=str_name + "          ""          "        "     " + str_namemasc + "             " + str_raza + "                  " + str_serv + "                       " + str_calle + "    ",
                            bg="white", font=("Comic Sans", 10, "bold"))
        persona3.grid(row=3, column=0, padx=(10, 0))
        persona4 = tk.Label(marco,
                            text="                         ""        ""               ""      ""          ""          ""                    ""        ""                      ""  ",
                            bg="white", font=("Comic Sans", 10, "bold"))
        persona4.grid(row=4, column=0, padx=(10, 0))

        global variable
        variable = str_nameadmin

        ventana4.mainloop()


def servicios():
    # creacion de la ventana de eleccion de servicio
    ventana10 = tk.Tk()
    ventana10.title("Eleccion de servicios")
    ventana10.geometry("500x400")
    ventana10.config(bg="beige")
    ventana10.resizable(width=False, height=False)

    tk.Label(ventana10, text="                   Servicios                  ", bg="navajo white", fg="black",
             width="50", height="2", font=("Bahnschrift", 15)).pack()
    tk.Label(ventana10, text="""Bienvenido a la pestaña de servicios,
    por favor de las siguientes opciones ingrese el servicio que desea para su mascota
    Respetando mayusculas y espacios""", bg="beige", fg="black", width="100", height="3",
             font=("Bahnschrift", 10)).pack()

    tk.Label(ventana10, text="""Servicio Estetico: 
         corte de pelo,  Baño y secado,
         corte de garras o  peinado y perfumado""", bg="beige", fg="black", width="100", height="4",
             font=("Bahnschrift", 10)).pack()

    tk.Label(ventana10, text="""Servicio Medico: 
         analisis,  esterilizacion,  interventiva 
         vacunas,  radiografias o  prueba diagnostica """, bg="beige", fg="black", width="100", height="4",
             font=("Bahnschrift", 10)).pack()

    # Crear campos de entrada
    marco2 = LabelFrame(ventana10, text="", font=("Comic Sans", 10, "bold"), bg="beige")
    marco2.config(bd=2, pady=5)
    marco2.pack()
    persona = tk.Label(marco2, text="", bg="beige", font=("Comic Sans", 10, "bold"))
    persona.grid(row=0, column=0, padx=(10, 0))
    servi_entry = tk.Entry(marco2)
    servi_entry.grid(row=0, column=1, sticky='s', padx=(0, 10), pady=(10, 0))
    iniciar_sesion = tk.Button(ventana10, text="Siguiente", command=elec_serv)
    iniciar_sesion.pack(padx=20, pady=20)
    salir = tk.Button(ventana10, text="Regresar", command=ventana10.destroy)
    salir.pack()

    global serv
    serv = servi_entry

    ventana10.mainloop()


def ubicaciones():
    def compro():
        callex = str(calle.get())
        calle1 = "C. 74 x 23 y 45"
        calle2 = "C. 32 x 96 y 98"
        calle3 = "C. 96 x 114 y 116"
        calle4 = "C. 14 x 18 y 20"
        calle5 = "C. 104 x 176 y 178"
        calle6 = "C. 77 x 56 y 58"
        if callex != calle1 and callex != calle2 and callex != calle3 and callex != calle4 and callex != calle5 and callex != calle6:
            messagebox.showerror("Dato erroneo", "La direccion ingresada no es válida")
        else:
            conexion = sqlite3.connect("Servicio2.db")
            ventana3 = tk.Tk()
            ventana3.configure(bg="beige")
            ventana3.resizable(width=False, height=False)
            # ventana3.iconbitmap("pet.ico")
            ventana3.title("Registro", )
            ventana3.configure(padx=200)
            ventana3.configure(pady=50)
            marco = LabelFrame(ventana3, text="Datos Generales", font=("Comic Sans", 10, "bold"), bg="beige")
            marco.config(bd=2, pady=5)
            marco.pack()
            # Crear la etiqueta y el campo de entrada de los datos
            persona = tk.Label(marco, text="datos del ciente", bg="beige", font=("Comic Sans", 10, "bold"))
            persona.grid(row=0, column=0, padx=(10, 0))
            "---------------edad-------------"
            age_label = tk.Label(marco, text="Edad:", bg="beige", font=("Comic Sans", 10, "bold"))
            age_label.grid(row=1, column=0, padx=(10, 0))
            age_entry = tk.Entry(marco)
            age_entry.grid(row=1, column=1, sticky='s', padx=(0, 10), pady=(10, 0))
            "-------------nombre-------------"
            name_label = tk.Label(marco, text="Nombre y apellido :", bg="beige", font=("Comic Sans", 10, "bold"))
            name_label.grid(row=2, column=0, padx=(10, 0))
            name_entry = tk.Entry(marco)
            name_entry.grid(row=2, column=1, sticky='s', padx=(0, 10), pady=(10, 0))
            "------------separacion--------------"
            mascota = tk.Label(marco, text="datos de la mascota", bg="beige", font=("Comic Sans", 10, "bold"))
            mascota.grid(row=4, column=0, padx=(10, 0))
            "-------------nombre_masc-------------"
            namemasc_label = tk.Label(marco, text="Nombre:", bg="beige", font=("Comic Sans", 10, "bold"))
            namemasc_label.grid(row=5, column=0, padx=(10, 0))
            namemasc_entry = tk.Entry(marco)
            namemasc_entry.grid(row=5, column=1, sticky='s', padx=(0, 10), pady=(10, 0))
            "---------------raza-------------"
            raza_label = tk.Label(marco, text="Raza:", bg="beige", font=("Comic Sans", 10, "bold"))
            raza_label.grid(row=6, column=0, padx=(10, 0))
            raza_entry = tk.Entry(marco)
            raza_entry.grid(row=6, column=1, sticky='s', padx=(0, 10), pady=(10, 0))
            "------------boton------------"
            submit_button = tk.Button(marco, text="Guardar e iniciar sesión", bg="Light cyan", command=servicios)
            submit_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10)
            submit_button2 = tk.Button(marco, text="Regresar", bg="Light cyan", command=ventana3.destroy)
            submit_button2.grid(row=9, column=0, columnspan=2, pady=10, padx=10)
            # creamos las variables globales

            global name
            name = name_entry
            global age
            age = age_entry
            global namemasc
            namemasc = namemasc_entry
            global raza
            raza = raza_entry
            global ventana_nuevo
            ventana_nuevo = ventana3

            ventana3.mainloop

    # creacion de la ventana de eleccion de servicio
    ventana5 = tk.Tk()
    ventana5.title("Selección de ubicación")
    ventana5.geometry("500x300")
    ventana5.resizable(width=False, height=False)
    ventana5.config(bg="beige")

    tk.Label(ventana5, text="Por favor, escoja y escriba una ubicacion de las siguientes", bg="navajo white",
             fg="black", width="70", height="2", font=("Bahnschrift", 13)).pack()
    tk.Label(ventana5, text="C. 74 x 23 y 45  |  C. 32 x 96 y 98     |  C. 96 x 114 y 116 ", bg="navajo white",
             fg="black", width="50", height="0", font=("Bahnschrift", 8)).pack()
    tk.Label(ventana5, text="C. 14 x 18 y 20  |C. 104 x 176 y 178    |  C. 77 x 56 y 58   ", bg="navajo white",
             fg="black", width="50", height="0", font=("Bahnschrift", 8)).pack()

    mi_label4 = tk.Label(ventana5,
                         text="",
                         bg="beige")
    mi_label4.pack()
    marco2 = LabelFrame(ventana5, text="", font=("Comic Sans", 10, "bold"), bg="beige")
    marco2.config(bd=2, pady=5)
    marco2.pack()
    # Crear la etiqueta y el campo de entrada de los datos
    persona = tk.Label(marco2, text="", bg="beige", font=("Comic Sans", 10, "bold"))
    persona.grid(row=0, column=0, padx=(10, 0))
    calle_entry = tk.Entry(marco2)
    calle_entry.grid(row=1, column=1, sticky='s', padx=(0, 10), pady=(10, 0))
    # calle_entry = tk.Entry(ventana5)
    # calle_entry.ggrid(row=1, column=1, padx=(0, 10), pady=(10, 0))
    iniciar_sesion = tk.Button(ventana5, text="Siguiente", command=compro)
    iniciar_sesion.pack(padx=20, pady=20)
    salir = tk.Button(ventana5, text="Regresar", command=ventana5.destroy)
    salir.pack()

    global calle
    calle = calle_entry

    ventana5.mainloop()


# Funcion para la ventana del login del admin.
def login_admin():
    def comprobacion():
        admin = nombre_usuario.get()
        admin_fijo = "Veter"
        contrasenna = contrasena_usuario.get()
        contrasena = "Eugenio"
        if contrasenna != contrasena or admin_fijo != admin:
            messagebox.showerror("Dato erroneo", "Alguno de los datos no es correcto")
        else:
            conexion = sqlite3.connect("Servicio2.db")
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                db="Servicio2"
            )
            ventana24 = tk.Tk()
            ventana24.configure(bg="beige")
            ventana24.resizable(width=False, height=False)
            # ventana3.iconbitmap("pet.ico")
            ventana24.title("Ficha de cita", )
            ventana24.configure(padx=200)
            ventana24.configure(pady=100)
            fcursor = db.cursor()
            consulta = "SELECT * from clientes "
            fcursor.execute(consulta)
            datos = fcursor.fetchall()
            str_datos = str(datos)
            print(datos)
            # for i in datos:
            #    print(datos)
            marco = LabelFrame(ventana24, text="Datos de la cita agendada", font=("Comic Sans", 10, "bold"), bg="white")
            marco.config(bd=9, pady=9)
            marco.pack()
            citas = tk.Label(marco, text=str_datos,
                             bg="white", font=("Comic Sans", 10, "bold"))
            citas.grid(row=1, column=1, padx=(10, 0))

            ventana24.mainloop()

    # se crea la ventana donde el admin ingresa sus datos
    ventana2 = tk.Tk()
    ventana2.resizable(width=False, height=False)
    ventana2.configure(background="beige")
    # ventana2.iconbitmap("pet.ico")
    ventana2.title("Login administrador")
    ventana2.configure(padx=165)
    ventana2.configure(pady=20)
    # Entrada para la contraseña
    mi_label3 = tk.Label(ventana2,
                         text="  BIENVENIDO ADMINISTRADOR  ",
                         bg="beige")
    mi_label3.pack()
    tk.Label(ventana2, text="  ", bg="beige",
             fg="black", width="20", height="1", font=("Bahnschrift", 15)).pack()
    mi_label4 = tk.Label(ventana2,
                         text="Ingrese su usuario",
                         bg="beige")
    mi_label4.pack()
    nombre_usuario = tk.Entry(ventana2)
    nombre_usuario.pack(pady=20)
    mi_label5 = tk.Label(ventana2,
                         text="Ingrese su contraseña",
                         bg="beige")
    mi_label5.pack()
    contrasena_usuario = tk.Entry(ventana2, show="*")
    contrasena_usuario.pack()
    # Botones
    iniciar_sesion = tk.Button(ventana2, text="Iniciar sesión", command=comprobacion)
    iniciar_sesion.pack(padx=40, pady=40)
    salir = tk.Button(ventana2, text="Regresar", command=ventana2.destroy)
    salir.pack()
    # Widgets
    resultado = tk.Label(ventana2, text="")
    resultado.pack(pady=90)
    ventana2.mainloop()


# ventana de elección de usuario
ventana = Tk()
ventana.configure(bg="beige")
ventana.resizable(width=False, height=False)
# ventana.iconbitmap("pet.ico")
ventana.title("Elección de usuario", )
ventana.configure(padx=200)
tk.Label(ventana, text=" Seleccione un perfil ", bg="beige",
         fg="black", width="20", height="1", font=("Bahnschrift", 15)).pack()
tk.Label(ventana, text=" ", bg="beige",
         fg="black", width="3", height="3", font=("Bahnschrift", 15)).pack()
iniciar_cuenta = Tk = Button(ventana, text="Administrador", command=login_admin)
iniciar_cuenta.pack(padx=20, pady=20)
iniciar_usuario = Tk = Button(ventana, text="       Cliente      ", command=eleccion_usuario)
iniciar_usuario.pack(padx=20, pady=20)
# Botones
salir = Tk = Button(ventana, text="Cerrar", command=ventana.quit)
salir.pack()
# Widgets
resultado = Tk = Label(ventana, text="")
resultado.pack(pady=90)
ventana.mainloop()