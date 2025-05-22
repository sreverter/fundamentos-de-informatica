import tkinter as tk
from pantalla_carga import PantallaCarga
from pantalla_busqueda import PantallaBusqueda

class Aplicacion:
    def __init__(self, root):
        self.root = root
        root.title("Gestión de Eventos Deportivos")

        self.frame_principal = tk.Frame(root)
        self.frame_principal.pack()

        tk.Button(self.frame_principal, text="Cargar Evento", width=20, command=self.abrir_carga).pack(pady=5)
        tk.Button(self.frame_principal, text="Buscar Eventos", width=20, command=self.abrir_busqueda).pack(pady=5)

    def abrir_carga(self):
        self.limpiar()
        PantallaCarga(self.root)

    def abrir_busqueda(self):
        self.limpiar()
        PantallaBusqueda(self.root)

    def limpiar(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()