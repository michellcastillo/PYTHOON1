
import customtkinter
from customtkinter import CTk, CTkLabel, CTkButton, CTkEntry, CTkComboBox
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

lg=customtkinter.CTk()
lg.geometry('700x500')
lg.config(bg="black")
lg.title("INICIO")
lg.resizable(False,False)
lg.iconbitmap(r"C:\Users\miche\PycharmProjects\PYCHARMich\Contabilidad/tecnologia-financiera.ico")

img = Image.open(r"C:\Users\miche\PycharmProjects\PYCHARMich\Contabilidad/FUTURE.png")
render = ImageTk.PhotoImage(img)
label_imagen = tk.Label(lg, image=render)
label_imagen.image = render
label_imagen.config(bg="black")
label_imagen.place(y=0, x=0)

#Insertamos una imagen que no es porque le queda una marca de agua horrible
#img = PhotoImage(file=r"C:\Users\miche\PycharmProjects\PYCHARMich\Contabilidad\FUTURE.png")
#label_img = customtkinter.CTkLabel(master=lg, image=img,text="")
#label_img.place(y=0, x=0)

#Creamos un frame
frame = customtkinter.CTkFrame(master=lg, fg_color="DeepSkyBlue4", border_color="DeepSkyBlue4",width=327, height=550)
frame.pack(side=tk.RIGHT, fill=tk.BOTH)

#Dentro del frame
label = customtkinter.CTkLabel(master=frame, text="BIENVENIDO",bg_color="DeepSkyBlue4",text_color="black", font=('Arial', 30, 'bold', ))
label.pack(padx=60,pady=10)

imagen_registro = Image.open(r"C:\Users\miche\PycharmProjects\PYCHARMich\Contabilidad\LOGO.png")
nueva_imagen = imagen_registro.resize((200, 200))
render = ImageTk.PhotoImage(nueva_imagen)
label_imagen = Label(master=frame, image=render)
label_imagen.image = render
label_imagen.config(bg="DeepSkyBlue4")
label_imagen.pack(pady=10, padx=0, ipadx=0)

marco = LabelFrame(master=frame, text="INICIA SESIÓN", bg="DeepSkyBlue4",font=("Comic Sans", 15, "bold"))
marco.config(padx=30, pady=10, bd=5)
marco.pack()

matricula_label = tk.Label(marco, text="No.EMPLEADO:",bg="DeepSkyBlue4", font=("Arial", 12, "bold"))
matricula_label.grid(row=1, column=1, padx=5, pady=8)
#vcmd = (marco.register(validate_matricula), '%P') validatecommand=vcmd
matricula_entry = tk.Entry(marco, validate="key",width=20, font=("Arial", 12))
matricula_entry.grid(row=1, column=2, padx=5, pady=8)

password_label = tk.Label(marco, text="CONTRASEÑA:", bg="DeepSkyBlue4", font=("Arial", 12, "bold"))
password_label.grid(row=2, column=1, padx=5, pady=8)
#vcmd2 = (marco.register(validate_password), '%P') validatecommand=vcmd2
password_entry = tk.Entry(marco, show="★", validate="key", width=20, font=("Arial", 12))
password_entry.grid(row=2, column=2, padx=5, pady=8)

frame_botones = Frame(master=frame)
frame_botones.config(bg="DeepSkyBlue4")
frame_botones.pack(pady=10)

#command=self.login

login_button = tk.Button(frame_botones, text="INICIAR SESIÓN", height=2, width=15,bg="cyan3", fg="black", font=("Arial", 12, "bold"))
login_button.grid(row=3, column=1, padx=5, pady=8)

#command=self.register

register_button = tk.Button(frame_botones, text="REGISTRARSE", height=2, width=15,bg="cyan3", fg="black", font=("Arial", 12, "bold"))
register_button.grid(row=3, column=2, padx=5, pady=8)

#NumEmp =customtkinter

lg.mainloop()

