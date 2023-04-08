import tkinter as tk


class MenuScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Ejemplo de pantalla con menú")
        self.config(bg="plum2")
        # Creamos el menú superior
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        # Creamos las opciones del menú
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Abrir", command=self.Abrir_archivo)
        self.file_menu.add_command(label="Guardar", command=self.Guardar_archivo)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)

        self.edit_menu.add_command(label="Archivo", command=self.Archivo)
        self.edit_menu.add_command(label="Imagen", command=self.Imagen)
        self.menu_bar.add_cascade(label="Insertar", menu=self.edit_menu)

        # Agregamos algunos widgets a la pantalla
        self.label = tk.Label(self, bg="plum2", text="¡BIENVENIDO!", font=30)
        self.label.pack(pady=15)
        self.button = tk.Button(self, bg="medium purple", text="Saludo", font=20, command=self.Boton)
        self.button.pack(pady=10)
        self.boton2 = tk.Button(self, bg="medium purple", text="Salir", font=20, command=self.Salir)
        self.boton2.pack()
        self.pack()

    def Abrir_archivo(self):
        print("Tu archivo ha sido abierto exitosamente")

    def Guardar_archivo(self):
        print("Tu arachivo ha sido guardado exitosamente")

    def Archivo(self):
        print("Has insertado tu archivo exitosamente")

    def Imagen(self):
        print("Has insertado la imagen exitosamente")

    def Boton(self):
        print("Hola que gusto tenerte en este programa, realiza lo que necesites")

    def Salir(self):
        print()
        self.file_menu.quit()


root = tk.Tk()
root.geometry("420x380")
app = MenuScreen(root)
root.config(bg='plum2')
app.mainloop()