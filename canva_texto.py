from tkinter import *

# variables globales
base = 460
altura = 380

# ventana principal
ventana_principal = Tk()
ventana_principal.title("Graficas 2D - texto")
ventana_principal.resizable(False,False)
ventana_principal.config(bg="green")


#frame de graficacion
frame_graficacion =Frame(ventana_principal)
frame_graficacion.config(bg="white", width=480, height=400)
frame_graficacion.pack(fill=BOTH, padx=10,pady=10)


#creacion canvas
c= Canvas(frame_graficacion, width=base, height=altura)
c.place(x=10, y=10)


#texto
texto = c.create_text(base/2, altura/2, anchor="center", text="sistemas guanenta", font=("Arial", "30", "bold"), fill="blue", activefill="red")


ventana_principal.mainloop()