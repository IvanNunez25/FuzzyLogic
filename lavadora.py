import pygame
import tkinter as tk
from tkinter import ttk

x = 100
LAVADORA_1 = (112, 110, 109)
BOTONES_LAV = (189, 183, 180)

pygame.init()
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Lavadora")

clock = pygame.time.Clock()
running = True

# Crear ventana de Tkinter
root = tk.Tk()
root.title("Seleccionar Figura")

# Crear frame
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

# Variable para el radio button
action_var = tk.IntVar()
action_var.set(0)  # Establecer el valor inicial

# Crear radio buttons
ttk.Radiobutton(frame, text="Lavadora", value=0).pack(anchor="w")
ttk.Radiobutton(frame, text="Cuadrado", value=1).pack(anchor="w")
ttk.Radiobutton(frame, text="Círculo", value=2).pack(anchor="w")

# Ejecutar la ventana
root.mainloop()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Limpiar la pantalla
    

    # Dibujar base de la lavadora
    points = [(100 + x, 20), (500 + x, 20), (490 + x, 50), (110 + x, 50)]
    pygame.draw.polygon(screen, LAVADORA_1, points)
    
    points = [(110 + x, 50), (490 + x, 50), (600 + x, 350), (0 + x, 350)]
    pygame.draw.polygon(screen, LAVADORA_1, points)
    
    points = [(600 + x, 350), (0 + x, 350), (70 + x, 550), (530 + x, 550)]
    pygame.draw.polygon(screen, LAVADORA_1, points)
    
    # Dibujar área de botones
    points = [(35 + x, 270), (565 + x, 270), (590 + x, 340), (10 + x, 340)]
    pygame.draw.polygon(screen, BOTONES_LAV, points)
    
    # Botones
    

    pygame.display.flip()
    clock.tick(60)
