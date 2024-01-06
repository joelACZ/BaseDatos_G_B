# user1_if_2_7_empleado.py

import tkinter as tk

class BolitaMovil:
    def __init__(self, contenedor, **kwargs):
        self.canvas = tk.Canvas(contenedor, width=200, height=200, bg="white")
        self.canvas.pack(fill="both", expand=True)

        self.bolita = self.canvas.create_oval(10, 10, 30, 30, fill="blue")  # Crear la bolita en el lienzo
        self.dx = 2  # Velocidad en la dirección x
        self.dy = 2  # Velocidad en la dirección y

    def mover(self):
        # Mover la bolita en la dirección especificada por dx y dy
        self.canvas.move(self.bolita, self.dx, self.dy)

        # Obtener las coordenadas actuales de la bolita
        x1, y1, x2, y2 = self.canvas.coords(self.bolita)

        # Verificar si la bolita ha alcanzado los límites del lienzo
        if x1 <= 0 or x2 >= self.canvas.winfo_width():
            self.dx = -self.dx  # Invertir la dirección en x

        if y1 <= 0 or y2 >= self.canvas.winfo_height():
            self.dy = -self.dy  # Invertir la dirección en y

        # Llamar a la función nuevamente después de un breve tiempo para animar la bolita
        self.canvas.after(10, self.mover)

def iniciar_programa_bolita_movil(contenedor):
    bolita_movil = BolitaMovil(contenedor)
    bolita_movil.mover()
