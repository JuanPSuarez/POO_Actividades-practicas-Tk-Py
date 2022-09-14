from tkinter import *

#Ventana Principal
ventana = Tk()
ventana.geometry("300x200")
ventana.title("ContDecreciente.py")

#Funcion de contador
def contador():
    num=int(etiquetaCont.get())
    num -= 1
    txtvar.set(num)

txtvar=StringVar()
txtvar.set(88)


#Frame, donde insertaremos todos los elementos.
frameCont = Frame(ventana)
frameCont.place(relx= 0.5, rely=0.5, anchor=CENTER)
num = 0

#Etiqueta "Contador"
etiquetaNom = Label(frameCont, text="Contador")
etiquetaNom.grid(row=0, column=0)

#Etiqueta numero
etiquetaCont = Entry(frameCont, textvariable=txtvar)
etiquetaCont.grid(row=0, column=1)



#Boton Contador
botonCont = Button(frameCont, text="-", command = contador)
botonCont.grid(row=0, column=2)

ventana.mainloop()