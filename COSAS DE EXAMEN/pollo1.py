import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

#se crea la interfaz
ventana = tk.Tk()
ventana.title ("ERROR")
ventana.geometry('500x500')
ventana.config(bg="azure")
ventana.iconbitmap(r"C:\Users\miche\PycharmProjects\PYCHARMich\COSAS DE EXAMEN\error.ico")

img = Image.open(r'C:\Users\miche\PycharmProjects\PYCHARMich\COSAS DE EXAMEN\pollo1.jpg')
new_img = img.resize ((300,250))
render = ImageTk.PhotoImage(new_img)
img1 = Label(ventana, image= render)
img1.image = render
img1.place(x=100, y=108)

espacio=Label(ventana, text=" ",bg="azure", font=("Arial", 12), fg="gray1")
espacio.config(pady="15")
espacio.pack()
miEtiqueta1 = Label(ventana, text="¡ALGO ESTA MAL, INTENTALO DE NUEVO!",bg="azure", font=("Arial", 12), fg="gray1")
miEtiqueta1.config(pady="10")
miEtiqueta1.pack()

#se crean los botones
boton = tk.Button(ventana,command=ventana.quit, text='ACEPTAR',bg="red",fg="white",font=("Arial",12,"bold"), height=2, width=10)
boton.place(x="200", y="400")

ventana.mainloop()