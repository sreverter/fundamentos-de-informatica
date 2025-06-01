import tkinter as tk
from tkinter import messagebox
from logica.abm_eventos import eventos
from logica.reglas_negocio import buscar_por_corredor

class PantallaBusqueda:
    def __init__(self, ventana_principal, app):
        self.ventana_principal = ventana_principal  # ventana principal original
        self.app = app  # referencia a la app para recargar o manejar estados si hace falta

        # Creamos la ventana secundaria
        self.ventana = tk.Toplevel(self.ventana_principal)
        self.ventana.title("Buscar Eventos")
        self.ventana.geometry("600x400")
        
        # Cuando se cierre esta ventana, que se muestre la principal
        self.ventana.protocol("WM_DELETE_WINDOW", self.volver_a_inicio)

        self.frame = tk.Frame(self.ventana)
        self.frame.pack(pady=10)

        # Entrada de busqueda
        tk.Label(self.frame, text="Buscar por nombre de corredor").pack()
        self.entrada = tk.Entry(self.frame)
        self.entrada.pack(pady=5)

        # Boton buscar
        tk.Button(self.frame, text="Buscar", command=self.buscar).pack(pady=5)

        # Resultados
        self.resultado = tk.Listbox(self.frame, width=80)
        self.resultado.pack(pady=10)

        # Boton volver
        tk.Button(self.frame, text="Volver al inicio", command=self.volver_a_inicio).pack(pady=10)

        # Footer
        self.info_app = tk.Label(
            self.ventana,
            text="Gestion de Eventos Deportivos v1.0 | Grupo nro. 4 \n Reverter Santiago - Ruffo Eduardo - Ale - Martin",
            font=("Segoe UI", 9),
            fg="#7b7d7d",
            bg="#d0d3d4"
        )
        self.info_app.pack(side="bottom", fill="x", pady=5)

    def buscar(self):
        nombre = self.entrada.get().strip()
        self.resultado.delete(0, tk.END)

        if not nombre:
            messagebox.showwarning("Advertencia", "Ingrese un nombre de corredor para buscar.")
            return

        encontrados = buscar_por_corredor(eventos, nombre)

        if encontrados:
            for e in encontrados:
                self.resultado.insert(tk.END, f"{e.nombre} - {e.fecha} - {e.lugar}")
        else:
            self.resultado.insert(tk.END, "No se encontraron eventos con ese corredor.")

    def volver_a_inicio(self):
        # Cerramos la ventana de búsqueda
        self.ventana.destroy()
        # Mostramos la ventana principal
        self.ventana_principal.deiconify()
        # Refrescamos la lista de archivos en la ventana principal, si es que la app lo tiene
        if hasattr(self.app, 'cargar_archivos'):
            self.app.cargar_archivos()