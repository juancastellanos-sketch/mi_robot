from tkinter import *

#-----------------
#variables globales
#-----------------
BASE= 460
ALTURA= 220

#-----------------
#ventana principal
#-----------------
ventana_principal =Tk()
ventana_principal.title("graficas 2D")
ventana_principal.resizable(False,False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")

#----------------
#frame de graficacion
#-----------------
frame_graficacion =Frame(ventana_principal)
frame_graficacion.config(bg="green",width=480,height=240)
frame_graficacion.place(x=10, y=10)

#-----------------
# lienzo de graficacion
#-----------------
c = Canvas (frame_graficacion,width=BASE,height=ALTURA)
c.config(bg="black")
c.place(x=10, y=10)
#-----------------
#-----------------
# lineas rectas
#-----------------
linea_1 = c.create_line(BASE/2, ALTURA/2,BASE,0, fill="red", width=2)
linea_2 = c.create_line(BASE/2, ALTURA/2, 0, 0,fill="green", width=2)
linea_3 = c.create_line(BASE/2, ALTURA/2, 0, ALTURA, fill="yellow", width=2)
linea_4 = c.create_line(BASE/2, ALTURA/2, BASE, ALTURA, fill="purple", width=2)
#-----------------
# Texto
#-----------------
texto_1 = c.create_text(BASE/4,ALTURA/4, anchor="center", text="juan diego",font=("Arial",25,"bold"), fill="yellow")
#-----------------
#rectangulos
#-----------------
rectangulo_1 = c.create_rectangle(BASE/2,ALTURA/2,BASE,ALTURA, fill="pink",outline="blue")

#-----------------
#poligonos
#-----------------
poligono_1 = c.create_polygon(0,0, BASE/2, ALTURA/2, 0, ALTURA, fill="red", outline="red")
#-----------------
#circulo
#-----------------
circulo_1 = c.create_oval(BASE/2 - 50, ALTURA/2 - 50,BASE/2 + 50,ALTURA/2 + 50, fill="orange", outline="green")
#-----------------
#arcos
#-----------------
arco_1 = c.create_arc(BASE/2 - 30, ALTURA/2 - 30, BASE/2 + 30, ALTURA/2 + 30, start=30, extent=300, fill="black")
#desplegar ventana principal
#-----------------

ventana_principal.mainloop()