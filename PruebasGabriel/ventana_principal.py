import os
import tkinter as tk
from pantalla_carga import PantallaCarga
from pantalla_busqueda import PantallaBusqueda

class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Gestión de Eventos Deportivos")
        ventana.geometry("600x400")
        ventana.configure(bg="#f0f0f0")    

        # ----- Lista de archivos
        self.lista_archivos = tk.Listbox(ventana, font=("Segoe UI", 10))
        self.lista_archivos.pack(fill="both", expand=True, padx=10, pady=10)
        self.cargar_archivos()

        # ----- Frame principal
        self.frame_principal = tk.Frame(ventana)
        self.frame_principal.pack()
        # ----- Botones de navegacion
        tk.Button(self.frame_principal, text="Cargar Evento", width=20, command=self.abrir_carga).pack(pady=5)       
        tk.Button(self.frame_principal, text="Buscar Eventos", width=20, command=self.abrir_busqueda).pack(pady=5)

        # ----- Informacion del grupo
        self.info_app = tk.Label(
            ventana,
            text="Gestión de Eventos Deportivos v1.0 | Grupo nro. 4 \n Reverter Santiago - Ruffo Eduardo - Ale - Martin",
            font=("Segoe UI", 9),
            fg="#7b7d7d",
            bg="#d0d3d4"
        )
        self.info_app.pack(side="bottom", fill="x", pady=5)

    def abrir_carga(self):
        self.ventana.withdraw()  # Oculta la ventana principal
        PantallaCarga(self.ventana, self)  # Pasa la instancia para recargar archivos

    def abrir_busqueda(self):
        self.ventana.withdraw()
        PantallaBusqueda(self.ventana, self)  

    def cargar_archivos(self):
        ruta_datos = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Datos")
        if not os.path.exists(ruta_datos):
            os.makedirs(ruta_datos)

        archivos = os.listdir(ruta_datos)
        self.lista_archivos.delete(0, tk.END)
        for archivo in archivos:
            self.lista_archivos.insert(tk.END, archivo)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Aplicacion(ventana)
    ventana.mainloop()
