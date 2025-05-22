import tkinter as tk
from logica.abm_eventos import eventos
from logica.reglas_negocio import buscar_por_corredor

class PantallaBusqueda:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root)
        self.frame.pack()

        tk.Label(self.frame, text="Buscar por nombre de corredor").pack()
        self.entrada = tk.Entry(self.frame)
        self.entrada.pack()

        tk.Button(self.frame, text="Buscar", command=self.buscar).pack()
        self.resultado = tk.Listbox(self.frame, width=80)
        self.resultado.pack()

    def buscar(self):
        nombre = self.entrada.get()
        encontrados = buscar_por_corredor(eventos, nombre)
        self.resultado.delete(0, tk.END)
        for e in encontrados:
            self.resultado.insert(tk.END, f"{e.nombre} - {e.fecha} - {e.lugar}")