# userjacz_if_2_0_menu.py
# userjacz_if_2_0_menu.py

import tkinter as tk
from user1_if_2_7_empleado import iniciar_programa_bolita_movil

class PanelContenido(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, justify="left", padx=10, pady=10, wraplength=400, bg="black", fg="white", **kwargs)
        self.bolita_movil_instancia = None  # Almacenar la instancia de BolitaMovil

    def mostrar_contenido(self, contenido):
        if contenido == "Contenido de Empleado":
            if self.bolita_movil_instancia is not None:
                # Detener la animación si la instancia ya existe
                self.bolita_movil_instancia.detener_animacion()
                # Liberar recursos de la instancia anterior
                self.bolita_movil_instancia = None

            # Iniciar la animación y almacenar la instancia
            self.bolita_movil_instancia = iniciar_programa_bolita_movil(self)
        else:
            self.config(text=contenido)

class ComponenteBarraLateral(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, bg="grey", **kwargs)
        self.pack_forget()

        secciones = [
            ("Itinerario ✈️", "Contenido Itinerario"),
            ("Pago 💳", "Contenido de Pago"),
            ("Cliente 👤", "Contenido de Cliente"),
            ("Aerolínea ✉️", "Contenido de Aerolínea"),
            ("Empleado 👥", "Contenido de Empleado"),
            ("Reserva📦", "Contenido de Reserva"),
            ("Sign In🔐", "Contenido de Sign In"),
            ("Sign Up📝", "Contenido de Sign Up"),
        ]

        for seccion, contenido in secciones:
            boton = tk.Button(self, text=seccion, command=lambda c=contenido: self.mostrar_contenido(c), bg="white", fg="black")
            boton.pack(fill="x", pady=5)

        self.panel_contenido = PanelContenido(master)
        self.panel_contenido.pack(side="right", fill="both", expand=True)

    def mostrar_contenido(self, contenido):
        self.panel_contenido.mostrar_contenido(contenido)
        root.after(1000, self.ocultar_barra_lateral)

    def ocultar_barra_lateral(self, event=None):
        self.pack_forget()

def mostrar_barra_lateral_con_retardo(event=None):
    barra_lateral.pack(side="left", fill="y", padx=10, pady=10)

def ocultar_barra_lateral_con_retardo(event=None):
    barra_lateral.pack_forget()

root = tk.Tk()
root.title("Sistema de Gestión de Aerolínea ✈️")
root.geometry("795x565")

ancho_ventana = 795
alto_ventana = 565
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()
x_pos = (ancho_pantalla - ancho_ventana) // 2
y_pos = (alto_pantalla - alto_ventana) // 2
root.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

root.configure(bg="grey")

barra_lateral = ComponenteBarraLateral(root)

root.bind("<Enter>", mostrar_barra_lateral_con_retardo)
root.bind("<Leave>", ocultar_barra_lateral_con_retardo)

root.mainloop()
