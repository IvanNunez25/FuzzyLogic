import tkinter as tk
from tkinter import ttk
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

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
    # Pasar las selecciones de los radio buttons a las variables de entrada
    tipo_tela_input = var1.get()
    tipo_suciedad_input = var2.get()
    nivel_carga_input = var3.get()
    
    # Computar las salidas utilizando lógica difusa
    lavadora_sim.input['tipo_tela'] = tipo_tela_input
    lavadora_sim.input['tipo_suciedad'] = tipo_suciedad_input
    lavadora_sim.input['nivel_carga'] = nivel_carga_input
    lavadora_sim.compute()
    
    # Obtener los resultados de las salidas
    tiempo_lavado_output = lavadora_sim.output['tiempo_lavado']
    temperatura_output = lavadora_sim.output['temperatura']
    tiempo_secado_output = lavadora_sim.output['tiempo_secado']
    velocidad_lavado_output = lavadora_sim.output['velocidad_lavado']
    nivel_agua_output = lavadora_sim.output['nivel_agua']
    # Imprimir los resultados (puedes hacer lo que desees con ellos)
    canvas2.delete("texto_anterior")
    canvas2.create_text(10, 10, text=f"Tiempo de lavado: {tiempo_lavado_output}", anchor="nw", tags="texto_anterior")
    canvas2.create_text(10, 25, text=f"Tiempo de secado: {tiempo_secado_output}", anchor="nw", tags="texto_anterior")
    canvas2.create_text(10, 40, text=f"Temperatura: {temperatura_output}", anchor="nw", tags="texto_anterior")
    canvas2.create_text(10, 55, text=f"Velocidad: {velocidad_lavado_output}", anchor="nw", tags="texto_anterior")
    canvas2.create_text(10, 70, text=f"Nivel de agua: {nivel_agua_output}", anchor="nw", tags="texto_anterior")
    # Imprimir los resultados (puedes hacer lo que desees con ellos)
    print("Tiempo de lavado:", tiempo_lavado_output)
    print("Temperatura:", temperatura_output)
    print("Tiempo de secado:", tiempo_secado_output)
    print("Velocidad de lavado:", velocidad_lavado_output)
    print("Nivel de agua:", nivel_agua_output)

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
ttk.Radiobutton(frame, text="Manchas", value=1, variable=var2).grid(row=1, column=1, padx=25, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Grasa", value=40, variable=var2).grid(row=2, column=1, padx=25, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Tierra", value=90, variable=var2).grid(row=3, column=1, padx=25, pady=5, sticky="w")

label3 = tk.Label(frame, text="Carga:")
label3.grid(row=0, column=2, columnspan=3, padx=5, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Ligera", value=0, variable=var3).grid(row=1, column=2, padx=25, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Medio", value=50, variable=var3).grid(row=2, column=2, padx=25, pady=5, sticky="w")
ttk.Radiobutton(frame, text="Pesado", value=95, variable=var3).grid(row=3, column=2, padx=25, pady=5, sticky="w")

btn_mostrar = ttk.Button(frame, text="Iniciar", command=inferencia)
btn_mostrar.grid(row=6, column=0, columnspan=3, padx=5, pady=10, sticky="ew")



canvas2 = tk.Canvas(frame, width=400, height=350, bg="blue")
canvas2.grid(row=7, column=0, columnspan=3, padx=0, pady=0)

# Crear lienzo (Canvas)
canvas = tk.Canvas(root, width=700, height=600)
canvas.pack(side="right")

# Llamar a la función para dibujar el polígono
dibujar_lavadora(canvas)

# Definir los universos y las funciones de membresía para las entradas y salidas
# Definiciones de las funciones de membresía para las entradas y salidas
tipo_tela = ctrl.Antecedent(np.arange(0, 101, 1), 'tipo_tela')
tipo_tela['piel'] = fuzz.pimf(tipo_tela.universe, 0, 0, 5, 15)
tipo_tela['seda'] = fuzz.pimf(tipo_tela.universe, 5, 15, 30, 45)
tipo_tela['lana'] = fuzz.pimf(tipo_tela.universe, 30, 40, 55, 70)
tipo_tela['algodon'] = fuzz.pimf(tipo_tela.universe, 55, 65, 80, 95)
tipo_tela['poliester'] = fuzz.pimf(tipo_tela.universe, 80, 95, 100, 100)

tipo_suciedad = ctrl.Antecedent(np.arange(0, 101, 1), 'tipo_suciedad')
tipo_suciedad['manchas_comida'] = fuzz.gbellmf(tipo_suciedad.universe, 20, 4, 4)
tipo_suciedad['grasa'] = fuzz.pimf(tipo_suciedad.universe, 12.5, 35, 50, 87.5)
tipo_suciedad['tierra'] = fuzz.trapmf(tipo_suciedad.universe, (60, 85, 100, 100))

nivel_carga = ctrl.Antecedent(np.arange(0, 101, 1), 'nivel_carga')
nivel_carga['ligero'] = fuzz.trapmf(nivel_carga.universe, (0, 0, 10, 40))
nivel_carga['medio'] = fuzz.pimf(nivel_carga.universe, 10, 40, 60, 90)
nivel_carga['pesado'] = fuzz.trapmf(nivel_carga.universe, (60, 90, 100, 100))


#output
tiempo_lavado = ctrl.Consequent(np.arange(0, 101, 1), 'tiempo_lavado')
tiempo_lavado['corto'] = fuzz.trapmf(tiempo_lavado.universe, (0, 0, 10, 35))
tiempo_lavado['medio'] = fuzz.pimf(tiempo_lavado.universe, 10, 45, 55, 90)
tiempo_lavado['largo'] = fuzz.trapmf(tiempo_lavado.universe, (62.5, 90, 100, 100))

temperatura = ctrl.Consequent(np.arange(0, 101, 1), 'temperatura')
temperatura['fria'] = fuzz.trapmf(temperatura.universe,( 0, 0, 5, 35))
temperatura['templada'] = fuzz.gaussmf(temperatura.universe, 30, 50)
temperatura['caliente'] = fuzz.trapmf(temperatura.universe, (65, 95, 100, 100))

tiempo_secado = ctrl.Consequent(np.arange(0, 101, 1), 'tiempo_secado')
tiempo_secado['corto'] = fuzz.trapmf(tiempo_secado.universe, (0, 0, 5, 35))
tiempo_secado['medio'] = fuzz.gaussmf(tiempo_secado.universe, 30, 50)
tiempo_secado['largo'] = fuzz.trapmf(tiempo_secado.universe, (65, 95, 100, 100))

velocidad_lavado = ctrl.Consequent(np.arange(0, 101, 1), 'velocidad_lavado')
velocidad_lavado['baja'] = fuzz.trapmf(velocidad_lavado.universe,( 0, 0, 5, 35))
velocidad_lavado['media'] = fuzz.gaussmf(velocidad_lavado.universe, 30, 50)
velocidad_lavado['alta'] = fuzz.trapmf(velocidad_lavado.universe, (65, 95, 100, 100))

nivel_agua = ctrl.Consequent(np.arange(0, 101, 1), 'nivel_agua')
nivel_agua['bajo'] = fuzz.trapmf(nivel_agua.universe, (0, 0, 10, 40))
nivel_agua['medio'] = fuzz.pimf(nivel_agua.universe, 10, 40, 60, 90)
nivel_agua['alto'] = fuzz.trapmf(nivel_agua.universe, (60, 90, 100, 100))


# Define las otras salidas de manera similar (temperatura, tiempo_secado, velocidad_lavado, nivel_agua)


# Define las reglas de inferencia difusa
# Crea el sistema de control difuso
# Crea el simulador del sistema de control difuso
# Definir las reglas de inferencia difusa
rule1 = ctrl.Rule(antecedent=(tipo_tela['piel'] & tipo_suciedad['manchas_comida'] & nivel_carga['ligero']), 
                  consequent=(tiempo_lavado['largo'], temperatura['fria'], tiempo_secado['corto'], 
                              velocidad_lavado['media'], nivel_agua['bajo']))

rule2 = ctrl.Rule(antecedent=(tipo_tela['piel'] & tipo_suciedad['manchas_comida'] & nivel_carga['medio']), 
                  consequent=(tiempo_lavado['largo'], temperatura['templada'], tiempo_secado['medio'], 
                              velocidad_lavado['media'], nivel_agua['medio']))

rule3 = ctrl.Rule(antecedent=(tipo_tela['piel'] & tipo_suciedad['manchas_comida'] & nivel_carga['pesado']), 
                  consequent=(tiempo_lavado['largo'], temperatura['templada'], tiempo_secado['largo'], 
                              velocidad_lavado['media'], nivel_agua['alto']))

rule4 = ctrl.Rule(antecedent=(tipo_tela['piel'] & tipo_suciedad['grasa'] & nivel_carga['ligero']), 
                  consequent=(tiempo_lavado['medio'], temperatura['templada'], tiempo_secado['corto'], 
                              velocidad_lavado['media'], nivel_agua['bajo']))

rule5 = ctrl.Rule(antecedent=(tipo_tela['piel'] & tipo_suciedad['grasa'] & nivel_carga['medio']), 
                  consequent=(tiempo_lavado['medio'], temperatura['templada'], tiempo_secado['medio'], 
                              velocidad_lavado['media'], nivel_agua['medio']))

rule6 = ctrl.Rule(antecedent=(tipo_tela['piel'] & tipo_suciedad['grasa'] & nivel_carga['pesado']), 
                  consequent=(tiempo_lavado['medio'], temperatura['templada'], tiempo_secado['largo'], 
                              velocidad_lavado['media'], nivel_agua['alto']))

rule7 = ctrl.Rule(antecedent=(tipo_tela['piel'] & tipo_suciedad['tierra'] & nivel_carga['ligero']), 
                  consequent=(tiempo_lavado['corto'], temperatura['fria'], tiempo_secado['corto'], 
                              velocidad_lavado['baja'], nivel_agua['bajo']))

rule8 = ctrl.Rule(antecedent=(tipo_tela['piel'] & tipo_suciedad['tierra'] & nivel_carga['medio']), 
                  consequent=(tiempo_lavado['corto'], temperatura['fria'], tiempo_secado['medio'], 
                              velocidad_lavado['baja'], nivel_agua['medio']))

rule9 = ctrl.Rule(antecedent=(tipo_tela['piel'] & tipo_suciedad['tierra'] & nivel_carga['pesado']), 
                  consequent=(tiempo_lavado['corto'], temperatura['fria'], tiempo_secado['largo'], 
                              velocidad_lavado['baja'], nivel_agua['alto']))

rule10 = ctrl.Rule(antecedent=(tipo_tela['seda'] & tipo_suciedad['manchas_comida'] & nivel_carga['ligero']), 
                  consequent=(tiempo_lavado['largo'], temperatura['fria'], tiempo_secado['corto'], 
                              velocidad_lavado['baja'], nivel_agua['bajo']))

rule11 = ctrl.Rule(antecedent=(tipo_tela['seda'] & tipo_suciedad['manchas_comida'] & nivel_carga['medio']), 
                  consequent=(tiempo_lavado['largo'], temperatura['fria'], tiempo_secado['medio'], 
                              velocidad_lavado['baja'], nivel_agua['medio']))

rule12 = ctrl.Rule(antecedent=(tipo_tela['seda'] & tipo_suciedad['manchas_comida'] & nivel_carga['pesado']), 
                  consequent=(tiempo_lavado['largo'], temperatura['fria'], tiempo_secado['largo'], 
                              velocidad_lavado['baja'], nivel_agua['alto']))

rule13 = ctrl.Rule(antecedent=(tipo_tela['seda'] & tipo_suciedad['grasa'] & nivel_carga['ligero']), 
                  consequent=(tiempo_lavado['medio'], temperatura['fria'], tiempo_secado['corto'], 
                              velocidad_lavado['baja'], nivel_agua['bajo']))

rule14 = ctrl.Rule(antecedent=(tipo_tela['seda'] & tipo_suciedad['grasa'] & nivel_carga['medio']), 
                  consequent=(tiempo_lavado['medio'], temperatura['fria'], tiempo_secado['medio'], 
                              velocidad_lavado['baja'], nivel_agua['medio']))
                              
rule15 = ctrl.Rule(antecedent=(tipo_tela['seda'] & tipo_suciedad['grasa'] & nivel_carga['pesado']), 
                  consequent=(tiempo_lavado['medio'], temperatura['fria'], tiempo_secado['largo'], 
                              velocidad_lavado['baja'], nivel_agua['alto']))

rule16= ctrl.Rule(antecedent=(tipo_tela['seda'] & tipo_suciedad['tierra'] & nivel_carga['ligero']), 
                  consequent=(tiempo_lavado['corto'], temperatura['fria'], tiempo_secado['corto'], 
                              velocidad_lavado['baja'], nivel_agua['bajo']))

rule17= ctrl.Rule(antecedent=(tipo_tela['seda'] & tipo_suciedad['tierra'] & nivel_carga['medio']), 
                  consequent=(tiempo_lavado['corto'], temperatura['fria'], tiempo_secado['medio'], 
                              velocidad_lavado['baja'], nivel_agua['medio']))

rule18= ctrl.Rule(antecedent=(tipo_tela['seda'] & tipo_suciedad['tierra'] & nivel_carga['pesado']), 
                  consequent=(tiempo_lavado['corto'], temperatura['fria'], tiempo_secado['largo'], 
                              velocidad_lavado['baja'], nivel_agua['alto']))

rule19 = ctrl.Rule(antecedent=(tipo_tela['lana'] & tipo_suciedad['manchas_comida'] & nivel_carga['ligero']), 
                  consequent=(tiempo_lavado['largo'], temperatura['fria'], tiempo_secado['corto'], 
                              velocidad_lavado['media'], nivel_agua['bajo']))

rule20 = ctrl.Rule(antecedent=(tipo_tela['lana'] & tipo_suciedad['manchas_comida'] & nivel_carga['medio']), 
                  consequent=(tiempo_lavado['largo'], temperatura['fria'], tiempo_secado['medio'], 
                              velocidad_lavado['media'], nivel_agua['medio']))

rule21 = ctrl.Rule(antecedent=(tipo_tela['lana'] & tipo_suciedad['manchas_comida'] & nivel_carga['pesado']), 
                  consequent=(tiempo_lavado['largo'], temperatura['fria'], tiempo_secado['largo'], 
                              velocidad_lavado['media'], nivel_agua['alto']))

rule22 = ctrl.Rule(antecedent=(tipo_tela['lana'] & tipo_suciedad['grasa'] & nivel_carga['ligero']), 
                  consequent=(tiempo_lavado['medio'], temperatura['fria'], tiempo_secado['corto'], 
                              velocidad_lavado['baja'], nivel_agua['bajo']))

rule23 = ctrl.Rule(antecedent=(tipo_tela['lana'] & tipo_suciedad['grasa'] & nivel_carga['medio']), 
                  consequent=(tiempo_lavado['medio'], temperatura['fria'], tiempo_secado['medio'], 
                              velocidad_lavado['baja'], nivel_agua['medio']))
                              
rule24 = ctrl.Rule(antecedent=(tipo_tela['lana'] & tipo_suciedad['grasa'] & nivel_carga['pesado']), 
                  consequent=(tiempo_lavado['medio'], temperatura['fria'], tiempo_secado['largo'], 
                              velocidad_lavado['baja'], nivel_agua['alto']))

rule25 = ctrl.Rule(antecedent=(tipo_tela['lana'] & tipo_suciedad['tierra'] & nivel_carga['ligero']), 
                  consequent=(tiempo_lavado['corto'], temperatura['fria'], tiempo_secado['corto'], 
                              velocidad_lavado['baja'], nivel_agua['bajo']))

rule26 = ctrl.Rule(antecedent=(tipo_tela['lana'] & tipo_suciedad['tierra'] & nivel_carga['medio']), 
                  consequent=(tiempo_lavado['corto'], temperatura['fria'], tiempo_secado['medio'], 
                              velocidad_lavado['baja'], nivel_agua['medio']))

rule27 = ctrl.Rule(antecedent=(tipo_tela['lana'] & tipo_suciedad['tierra'] & nivel_carga['pesado']), 
                  consequent=(tiempo_lavado['corto'], temperatura['fria'], tiempo_secado['largo'], 
                              velocidad_lavado['baja'], nivel_agua['alto']))

rule28 = ctrl.Rule(antecedent=(tipo_tela['algodon'] & tipo_suciedad['manchas_comida'] & nivel_carga['ligero']), 
                  consequent=(tiempo_lavado['largo'], temperatura['templada'], tiempo_secado['corto'], 
                              velocidad_lavado['alta'], nivel_agua['bajo']))

rule29 = ctrl.Rule(antecedent=(tipo_tela['algodon'] & tipo_suciedad['manchas_comida'] & nivel_carga['medio']), 
                  consequent=(tiempo_lavado['largo'], temperatura['templada'], tiempo_secado['medio'], 
                              velocidad_lavado['alta'], nivel_agua['medio']))

rule30 = ctrl.Rule(antecedent=(tipo_tela['algodon'] & tipo_suciedad['manchas_comida'] & nivel_carga['pesado']), 
                  consequent=(tiempo_lavado['largo'], temperatura['templada'], tiempo_secado['largo'], 
                              velocidad_lavado['alta'], nivel_agua['alto']))

rule31 = ctrl.Rule(antecedent=(tipo_tela['algodon'] & tipo_suciedad['grasa'] & nivel_carga['ligero']), 
                  consequent=(tiempo_lavado['medio'], temperatura['templada'], tiempo_secado['corto'], 
                              velocidad_lavado['media'], nivel_agua['bajo']))

rule32 = ctrl.Rule(antecedent=(tipo_tela['algodon'] & tipo_suciedad['grasa'] & nivel_carga['medio']), 
                  consequent=(tiempo_lavado['medio'], temperatura['templada'], tiempo_secado['medio'], 
                              velocidad_lavado['media'], nivel_agua['medio']))
                              
rule33 = ctrl.Rule(antecedent=(tipo_tela['algodon'] & tipo_suciedad['grasa'] & nivel_carga['pesado']), 
                  consequent=(tiempo_lavado['medio'], temperatura['templada'], tiempo_secado['largo'], 
                              velocidad_lavado['media'], nivel_agua['alto']))

rule34 = ctrl.Rule(antecedent=(tipo_tela['algodon'] & tipo_suciedad['tierra'] & nivel_carga['ligero']), 
                  consequent=(tiempo_lavado['corto'], temperatura['fria'], tiempo_secado['corto'], 
                              velocidad_lavado['baja'], nivel_agua['bajo']))

rule35 = ctrl.Rule(antecedent=(tipo_tela['algodon'] & tipo_suciedad['tierra'] & nivel_carga['medio']), 
                  consequent=(tiempo_lavado['corto'], temperatura['fria'], tiempo_secado['medio'], 
                              velocidad_lavado['baja'], nivel_agua['medio']))

rule36 = ctrl.Rule(antecedent=(tipo_tela['algodon'] & tipo_suciedad['tierra'] & nivel_carga['pesado']), 
                  consequent=(tiempo_lavado['corto'], temperatura['fria'], tiempo_secado['largo'], 
                              velocidad_lavado['baja'], nivel_agua['alto']))

rule37 = ctrl.Rule(antecedent=(tipo_tela['poliester'] & tipo_suciedad['manchas_comida'] & nivel_carga['ligero']), 
                  consequent=(tiempo_lavado['largo'], temperatura['caliente'], tiempo_secado['corto'], 
                              velocidad_lavado['alta'], nivel_agua['bajo']))

rule38 = ctrl.Rule(antecedent=(tipo_tela['poliester'] & tipo_suciedad['manchas_comida'] & nivel_carga['medio']), 
                  consequent=(tiempo_lavado['largo'], temperatura['caliente'], tiempo_secado['medio'], 
                              velocidad_lavado['alta'], nivel_agua['medio']))

rule39 = ctrl.Rule(antecedent=(tipo_tela['poliester'] & tipo_suciedad['manchas_comida'] & nivel_carga['pesado']), 
                  consequent=(tiempo_lavado['largo'], temperatura['caliente'], tiempo_secado['largo'], 
                              velocidad_lavado['alta'], nivel_agua['alto']))

rule40 = ctrl.Rule(antecedent=(tipo_tela['poliester'] & tipo_suciedad['grasa'] & nivel_carga['ligero']), 
                  consequent=(tiempo_lavado['medio'], temperatura['templada'], tiempo_secado['corto'], 
                              velocidad_lavado['media'], nivel_agua['bajo']))

rule41 = ctrl.Rule(antecedent=(tipo_tela['poliester'] & tipo_suciedad['grasa'] & nivel_carga['medio']), 
                  consequent=(tiempo_lavado['medio'], temperatura['templada'], tiempo_secado['medio'], 
                              velocidad_lavado['media'], nivel_agua['medio']))
                              
rule42 = ctrl.Rule(antecedent=(tipo_tela['poliester'] & tipo_suciedad['grasa'] & nivel_carga['pesado']), 
                  consequent=(tiempo_lavado['medio'], temperatura['templada'], tiempo_secado['largo'], 
                              velocidad_lavado['media'], nivel_agua['alto']))

rule43 = ctrl.Rule(antecedent=(tipo_tela['poliester'] & tipo_suciedad['tierra'] & nivel_carga['ligero']), 
                  consequent=(tiempo_lavado['corto'], temperatura['fria'], tiempo_secado['corto'], 
                              velocidad_lavado['baja'], nivel_agua['bajo']))

rule44 = ctrl.Rule(antecedent=(tipo_tela['poliester'] & tipo_suciedad['tierra'] & nivel_carga['medio']), 
                  consequent=(tiempo_lavado['corto'], temperatura['fria'], tiempo_secado['medio'], 
                              velocidad_lavado['baja'], nivel_agua['medio']))

rule45 = ctrl.Rule(antecedent=(tipo_tela['poliester'] & tipo_suciedad['tierra'] & nivel_carga['pesado']), 
                  consequent=(tiempo_lavado['corto'], temperatura['fria'], tiempo_secado['largo'], 
                              velocidad_lavado['baja'], nivel_agua['alto']))


# Puedes continuar añadiendo las reglas restantes de manera similar


rules = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
         rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20,
         rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30,
         rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40,
         rule41, rule42, rule43, rule44,rule45]
# Cargar el sistema de control difuso desde el archivo FIS
lavadora_ctrl = ctrl.ControlSystem(rules)


# Crea el simulador del sistema de control difuso
lavadora_sim = ctrl.ControlSystemSimulation(lavadora_ctrl)

# Ejecutar la aplicación
root.mainloop()
