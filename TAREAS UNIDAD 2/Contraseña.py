import tkinter as tk


def iniciar_sesion():
    usuario = nombre_usuario.get()
    contrasena = contrasena_usuario.get()
    if usuario == "MichellCastillo" and contrasena == "michell16":
        resultado.config(text="Tu ingreso ha sido exitoso, pulsa el boton de: siguiente, para continuar")

        # Botones que solo podran utilizarse si el inicio de sesion es exitoso (Botones de siguiente y salir)
        siguiente = tk.Button(ventana, bg="PaleTurquoise1", text="Siguiente", command=sig)
        siguiente.pack(padx=10, pady=12)
        salir = tk.Button(ventana, bg="PaleTurquoise1", text="Salir", command=ventana.quit)
        salir.pack()

    else:
        resultado.config(text="Nombre de usuario o contraseña incorrectos")


# Definir un nuevo comando para un boton de siguiente, para mostrar texto en la terminal
def sig():
    op = print("Tu inicio de sesion ha sido exitoso, has ingresado al programa")


ventana = tk.Tk()
ventana.title("Inicio de sesión")
ventana.config(bg="DarkSeaGreen1")
ventana.configure(padx=100, pady=100)

# Crear campos de entrada para el nombre de usuario y la contraseña
nombre_usuario = tk.Entry(ventana, font=(15))
label = tk.Label(text="Ingresa tu correo")
label.config(fg="Black", bg="DarkSeaGreen1", font=("tahoma", 15))
label.pack(padx=0)

nombre_usuario.pack(pady=10)
contrasena_usuario = tk.Entry(ventana, show="♥", font=(15))
label = tk.Label(text="Ingresa tu contraseña")
label.pack(pady=0)
label.config(fg="Black", bg="DarkSeaGreen1", font=("tahoma", 15))
label.pack(padx=10)
contrasena_usuario.pack(pady=10)

# Crear botones para iniciar sesión
iniciar_sesion = tk.Button(ventana, bg="PaleTurquoise1", text="Iniciar sesión", command=iniciar_sesion)
iniciar_sesion.pack(padx=10, pady=10)

# Crear un widget de etiqueta para mostrar el resultado del inicio de sesión
resultado = tk.Label(ventana, bg="DarkSeaGreen1", text="")
resultado.pack(pady=10)

ventana.mainloop()