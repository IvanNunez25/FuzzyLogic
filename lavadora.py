import tkinter as tk
from tkinter import ttk

x = 50
LAVADORA_1 = "#706E6D"
LAVADORA_2 = "#666463"
BOTONES_LAV = "#BDB7B4"
INTERIOR = "#D6D5D4"

# Función para dibujar un polígono personalizado
def dibujar_lavadora(canvas):
    # Dibujar base de la lavadora
    points = [(100 + x, 20), (500 + x, 20), (490 + x, 50), (110 + x, 50)]
    canvas.create_polygon(points, fill=LAVADORA_2)

    points = [(110 + x, 50), (490 + x, 50), (600 + x, 350), (0 + x, 350)]
    canvas.create_polygon(points, fill=LAVADORA_1)

    points = [(600 + x, 350), (0 + x, 350), (70 + x, 550), (530 + x, 550)]
    canvas.create_polygon(points, fill=LAVADORA_2)

    # Dibujar área de tina    
    canvas.create_oval(120 + x, 80, 470 + x, 250, fill=INTERIOR, outline="black")

    # Dibujar área de botones
    points = [(35 + x, 270), (565 + x, 270), (590 + x, 340), (10 + x, 340)]
    canvas.create_polygon(points, fill=BOTONES_LAV)

def inferencia():
    seleccion1 = var1.get()
    seleccion2 = var2.get()
    seleccion3 = var3.get()
    print("Selección Conjunto 1:", seleccion1)
    print("Selección Conjunto 2:", seleccion2)
    print("Selección Conjunto 3:", seleccion3)
    
# Crear ventana de Tkinter
root = tk.Tk()
root.title("Lavadora")

# Crear frame
frame = tk.Frame(root)
frame.pack(side="left", padx=10, pady=10)

# Crear radio buttons
# Crear radio buttons y empaquetarlos en columnas y filas específicas usando grid

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

label1 = tk.Label(frame, text="Tipo de tela:")
label1.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Piel", value=0, variable=var1).grid(row=1, column=0, padx=25, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Algodón", value=1, variable=var1).grid(row=2, column=0, padx=25, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Poliéster", value=2, variable=var1).grid(row=3, column=0, padx=25, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Lana", value=3, variable=var1).grid(row=4, column=0, padx=25, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Seda", value=4, variable=var1).grid(row=5, column=0, padx=25, pady=5, sticky="w")

label2 = tk.Label(frame, text="Suciedad:")
label2.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Grasa", value=5, variable=var2).grid(row=1, column=1, padx=25, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Tierra", value=6, variable=var2).grid(row=2, column=1, padx=25, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Manchas", value=7, variable=var2).grid(row=3, column=1, padx=25, pady=5, sticky="w")

label3 = tk.Label(frame, text="Carga:")
label3.grid(row=0, column=2, columnspan=3, padx=5, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Ligera", value=8, variable=var3).grid(row=1, column=2, padx=25, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Medio", value=9, variable=var3).grid(row=2, column=2, padx=25, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Pesado", value=10, variable=var3).grid(row=3, column=2, padx=25, pady=5, sticky="w")

btn_mostrar = ttk.Button(frame, text="Iniciar", command=inferencia)
btn_mostrar.grid(row=6, column=0, columnspan=3, padx=5, pady=10, sticky="ew")

canvas2 = tk.Canvas(frame, width=400, height=350, bg="blue")
canvas2.grid(row=7, column=0, columnspan=3, padx=0, pady=0)

# Crear lienzo (Canvas)
canvas = tk.Canvas(root, width=700, height=600)
canvas.pack(side="right")

# Llamar a la función para dibujar el polígono
dibujar_lavadora(canvas)

# Ejecutar la aplicación
root.mainloop()