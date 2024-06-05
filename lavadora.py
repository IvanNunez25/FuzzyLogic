import tkinter as tk
from tkinter import ttk
import numpy as np

import funciones_membresia
import inferencia
import defuzzification

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

def calcular():
    # Pasar las selecciones de los radio buttons a las variables de entrada
    tipo_tela_input = var1.get()
    tipo_suciedad_input = var2.get()
    nivel_carga_input = var3.get()
    
    arr_tipo_tela = []
    arr_tipo_tela.append( funciones_membresia.pi_shaped( np.arange(0, 101, 1), 0, 0, 5, 15 )[tipo_tela_input - 1] )
    arr_tipo_tela.append( funciones_membresia.pi_shaped( np.arange(0, 101, 1), 5, 15, 30, 45 )[tipo_tela_input - 1] )
    arr_tipo_tela.append( funciones_membresia.pi_shaped( np.arange(0, 101, 1), 30, 40, 55, 70 )[tipo_tela_input - 1] )
    arr_tipo_tela.append( funciones_membresia.pi_shaped( np.arange(0, 101, 1), 55, 65, 80, 95 )[tipo_tela_input - 1] )
    arr_tipo_tela.append( funciones_membresia.pi_shaped( np.arange(0, 101, 1), 80, 95, 100, 100 )[tipo_tela_input - 1] )
    
    arr_suciedad = []
    arr_suciedad.append( funciones_membresia.generalized_bell( np.arange(0, 101, 1), 20, 4, 4 )[tipo_suciedad_input - 1] )
    arr_suciedad.append( funciones_membresia.pi_shaped( np.arange(0, 101, 1), 12.5, 35, 50, 87.5 )[tipo_suciedad_input - 1] )
    arr_suciedad.append( funciones_membresia.trapezoidal( tipo_suciedad_input, 60, 85, 100, 100 ) )
    
    arr_carga = []
    arr_carga.append( funciones_membresia.trapezoidal( nivel_carga_input, 0, 0, 10, 40 ) )
    arr_carga.append( funciones_membresia.pi_shaped( np.arange(0, 101, 1), 10, 40, 60, 90 )[nivel_carga_input - 1] )
    arr_carga.append( funciones_membresia.trapezoidal( nivel_carga_input, 60, 90, 100, 100 ) )
    
    inf_tiempo, inf_temperatura, inf_secado, inf_velocidad, inf_agua = inferencia.inferencia( arr_tipo_tela, arr_suciedad, arr_carga )
    
    reglas = inferencia.getRules()
    
    inferencia.clear()
    
    print(inf_tiempo, inf_temperatura, inf_secado, inf_velocidad, inf_agua)
    
    tiempo_lavado_output = defuzzification.centroide( inf_tiempo, list(range(101)) )
    temperatura_output = defuzzification.centroide( inf_temperatura, list(range(101)) )
    tiempo_secado_output = defuzzification.centroide( inf_secado, list(range(101)) )
    velocidad_lavado_output = defuzzification.centroide( inf_velocidad, list(range(101)) )
    nivel_agua_output = defuzzification.centroide( inf_agua, list(range(101)) )
    
    canvas2.delete("texto_anterior")
    canvas2.create_text(10, 10, text=f"Tiempo de lavado: {round((tiempo_lavado_output * 100 / 95 )* 60, 2)} min", anchor="nw", tags="texto_anterior")
    canvas2.create_text(10, 25, text=f"Tiempo de secado: {round((tiempo_secado_output * 100 / 200) * 60, 2)} min", anchor="nw", tags="texto_anterior")
    canvas2.create_text(10, 40, text=f"Temperatura: {round(temperatura_output * 100 / 3.8, 2) } °C", anchor="nw", tags="texto_anterior")
    canvas2.create_text(10, 55, text=f"Velocidad: {round(velocidad_lavado_output * 100 / 1.2, 2)} RPM", anchor="nw", tags="texto_anterior")
    canvas2.create_text(10, 70, text=f"Nivel de agua: {round(nivel_agua_output * 100 / 1.6, 2)} %", anchor="nw", tags="texto_anterior")
    
    # Imprimir los resultados (puedes hacer lo que desees con ellos)
    print("Tiempo de lavado:", tiempo_lavado_output)
    print("Temperatura:", temperatura_output)
    print("Tiempo de secado:", tiempo_secado_output)
    print("Velocidad de lavado:", velocidad_lavado_output)
    print("Nivel de agua:", nivel_agua_output)
    
    y = 10
    canvas3.delete("reglas")
    for regla in reglas:
        canvas3.create_text(10, y, text=regla, anchor="nw", tags="reglas")
        y += 30
        

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
ttk.Radiobutton(frame, text="Piel", value=5, variable=var1).grid(row=1, column=0, padx=25, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Seda", value=15, variable=var1).grid(row=2, column=0, padx=25, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Lana", value=50, variable=var1).grid(row=3, column=0, padx=25, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Algodón", value=70, variable=var1).grid(row=4, column=0, padx=25, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Poliéster", value=95, variable=var1).grid(row=5, column=0, padx=25, pady=5, sticky="w")
# Añade los otros radio buttons para tipo de tela

label2 = tk.Label(frame, text="Suciedad:")
label2.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Manchas", value=5, variable=var2).grid(row=1, column=1, padx=25, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Grasa", value=50, variable=var2).grid(row=2, column=1, padx=25, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Tierra", value=95, variable=var2).grid(row=3, column=1, padx=25, pady=5, sticky="w")

label3 = tk.Label(frame, text="Carga:")
label3.grid(row=0, column=2, columnspan=3, padx=5, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Ligera", value=5, variable=var3).grid(row=1, column=2, padx=25, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Medio", value=50, variable=var3).grid(row=2, column=2, padx=25, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Pesado", value=95, variable=var3).grid(row=3, column=2, padx=25, pady=5, sticky="w")

btn_mostrar = ttk.Button(frame, text="Iniciar", command=calcular)
btn_mostrar.grid(row=6, column=0, columnspan=3, padx=5, pady=10, sticky="ew")



canvas2 = tk.Canvas(frame, width=600, height=150, bg="white")
canvas2.grid(row=7, column=0, columnspan=3, padx=0, pady=0)

canvas3 = tk.Canvas(frame, width=600, height=150, bg="white")
canvas3.grid(row=8, column=0, columnspan=3, padx=0, pady=0)

# Crear lienzo (Canvas)
canvas = tk.Canvas(root, width=700, height=600)
canvas.pack(side="right")

# Llamar a la función para dibujar el polígono
dibujar_lavadora(canvas)

root.mainloop()
