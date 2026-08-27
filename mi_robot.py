import tkinter as tk

ventana = tk.Tk()
ventana.title("Robot con Tkinter")
ventana.geometry("500x500")

lienzo = tk.Canvas(ventana, width=500, height=500, bg="white")
lienzo.pack()

# Cabeza - rectángulo
lienzo.create_rectangle(150, 80, 350, 220, fill="lightgray", outline="black", width=3)

# Antena - línea recta
lienzo.create_line(250, 80, 250, 40, width=4)
lienzo.create_oval(240, 30, 260, 50, fill="red")

# Ojos - círculos
lienzo.create_oval(185, 110, 225, 150, fill="blue")
lienzo.create_oval(275, 110, 315, 150, fill="blue")

# Boca - arco
lienzo.create_arc(200, 140, 300, 200, start=0, extent=-180, width=4)

# Cuerpo - rectángulo
lienzo.create_rectangle(170, 220, 330, 370, fill="silver", outline="black", width=3)

# Brazos - líneas rectas
lienzo.create_line(170, 240, 100, 320, width=8)
lienzo.create_line(330, 240, 400, 320, width=8)

# Manos - círculos
lienzo.create_oval(80, 310, 120, 350, fill="orange")
lienzo.create_oval(380, 310, 420, 350, fill="orange")

# Piernas - rectángulos
lienzo.create_rectangle(190, 370, 240, 440, fill="gray")
lienzo.create_rectangle(260, 370, 310, 440, fill="gray")

# Pies - polígonos
lienzo.create_polygon(180, 440, 245, 440, 235, 460, 175, 460, fill="black")
lienzo.create_polygon(255, 440, 320, 440, 325, 460, 265, 460, fill="black")

ventana.mainloop()