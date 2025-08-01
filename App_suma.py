# se inporta la libreria tkinter
from tkinter import *

#--------------------
# Funciones de la app 
#---------------------



#----------------------------
# Ventana principal de la app
#----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracticas de un objeto de tipo TK()

ventana_principal= Tk() 

# titulo de la ventana
ventana_principal.title("Daniel andres villar ortiz")

# Tamaño de la ventana
ventana_principal.geometry("800x500")

# Deshabilitar boton maximizar de la ventana 

ventana_principal.resizable(0,0)

# Color de fondo de la pantalla

ventana_principal.config(bg= "black")

#---------------------------
# Frame 1 - entrada de datos
#---------------------------

frame_1 = Frame(ventana_principal)
frame_1.config(bg="ivory2", width=780, height=240)
frame_1.place(x=10,y=10)

# imagen - logo de la app
logo = PhotoImage(file="img/btn-suma.png")
label_logo = Label(frame_1, image = logo)
label_logo.place(x=10, y=10)

# Etiqueta para el titulo de la app
titulo = Label(frame_1, text="Colegio San Jose de Guanenta")
titulo.config(bg="yellow", fg="blue", font=("Arial", 16))
titulo.place(x=390, y=10)

# Etiqueta para el subtitulo 1 de la app

subtitulo1 = Label(frame_1, text="Especialidad en sistemas")
subtitulo1.config(bg="yellow", fg="blue", font=("Arial", 12))
subtitulo1.place(x=390, y=40)

#----------------------
# Frame 2 - operaciones
#----------------------

frame_2 = Frame(ventana_principal)
frame_2.config(bg="ivory2", width=780, height=120)
frame_2.place(x=10,y=260)

#---------------------
# Frame 3 - resultados
#---------------------

frame_3 = Frame(ventana_principal)
frame_3.config(bg="ivory2", width=780, height=100)
frame_3.place(x=10,y=390)


# Metodo principal que despliega la ventana en la pantalla

ventana_principal.mainloop()