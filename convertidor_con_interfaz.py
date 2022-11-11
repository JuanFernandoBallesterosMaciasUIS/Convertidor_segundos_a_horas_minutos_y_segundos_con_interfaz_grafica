from tkinter import *
from tkinter import messagebox


def convertir():
    h = int(x.get())/3600

    h1 = int(h)
    m1 = (h-h1)*60

    m2 = int(m1)
    s1 = int((m1-m2)*60)
    if h1 == 1:
        t_resultados.insert(INSERT, "De los " + x.get() + " segundos, serian:\n"+ str(h1) + " hora con " + str(m2) + " minutos y " + str(s1) + " segundos.")
    else:
        t_resultados.insert(INSERT, "De los " + x.get() + " segundos, serian:\n"+ str(h1) + " horas con " + str(m2) + " minutos y " + str(s1) + " segundos.")
        
def borrar():
    x.set("")
    t_resultados.delete("1.0","end")
    
def salir():
    messagebox.showinfo("Conversión 1.0", "La app se cerrará...")
    ventana_principal.destroy()

    

ventana_principal = Tk()
ventana_principal.title("Convertidor")
ventana_principal.geometry("400x450")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="snow")




x = StringVar()

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "light grey", width = 380 , height = 240)
frame_entrada.place(x = 10, y = 10)

#frame_entrada1 = Frame(ventana_principal)
#frame_entrada1.config(bg = "slategray4", width = 380 , height = 180)
#frame_entrada1.place(x = 10, y = 260)


titulo = Label(frame_entrada, text = "Convertidor de tiempo")
titulo.config(bg = "light grey", fg = "gray21", font = ("Rubik",18))
titulo.place(x = 70, y = 20)

titulo2 = Label(frame_entrada, text = "Ingresa la cantidad en segundos")
titulo2.config(bg = "light grey", fg = "gray21", font = ("Rubik",14))
titulo2.place(x = 50, y = 150)

# Entry para segundos

entry_s = Entry(ventana_principal, textvariable=x)
entry_s.config(font=("Rubik",20), justify=LEFT, fg="gray21")
entry_s.focus_set()
entry_s.place(x=150, y=120, width=115, height=30)


# Boton para convertir
bt_convertir = Button(ventana_principal, text="Convertir",bg="slategray4", fg="light grey", command= convertir)
bt_convertir.place(x=150, y=205, width=100, height=30)

#Boton borrar
bt_borrar = Button(ventana_principal, text="Borrar",bg="slategray4", fg="light grey",command= borrar)
bt_borrar.place(x=25, y=205, width=100, height=30)

# Boton salir
bt_salir = Button(ventana_principal, text="Salir",bg="slategray4", fg="light grey", command= salir)
bt_salir.place(x=275, y=205, width=100, height=30)


#area de texto para resultados
t_resultados = Text(ventana_principal)
t_resultados.config(bg = "slategray4", width = 25 , height = 6, fg="white", font=("Rubik",17))
t_resultados.place(x = 10, y = 260)

ventana_principal.mainloop()