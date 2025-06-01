import os
import tkinter as tk
from tkinter import messagebox
from modelos.entidades import Evento, Corredor
from logica.abm_eventos import agregar_evento

class PantallaCarga:
    def __init__(self, ventana_principal, app):
        self.ventana_principal = ventana_principal
        self.app = app

        self.ventana = tk.Toplevel(self.ventana_principal)
        self.ventana.title("Carga de Evento")
        self.ventana.geometry("600x600")

        self.frame = tk.Frame(self.ventana)
        self.frame.pack()

        # Campos del evento
        self.campos = {}
        for campo in ["Nombre", "Fecha", "Tipo_carrera", "Distancia", "Cantidad_corredores", "Lugar", "Record"]:
            tk.Label(self.frame, text=campo.replace("_", " ")).pack()
            entry = tk.Entry(self.frame)
            entry.pack()
            self.campos[campo] = entry

        # Agregar corredores
        self.corredores = []
        tk.Button(self.frame, text="Agregar Corredores", command=self.agregar_corredor).pack()
        self.lista_corredores = tk.Listbox(self.frame)
        self.lista_corredores.pack()

        # Boton guardar
        tk.Button(self.frame, text="Guardar Evento", command=self.guardar_evento).pack()
        
        # Boton volver
        tk.Button(self.frame, text="Volver al inicio", command=self.volver_a_inicio).pack(pady=10)

        # Info del grupo
        self.info_app = tk.Label(
            self.ventana,
            text="Gestión de Eventos Deportivos v1.0 | Grupo nro. 4\nReverter Santiago - Ruffo Eduardo - Ale - Martin",
            font=("Segoe UI", 9),
            fg="#7b7d7d",
            bg="#d0d3d4"
        )
        self.info_app.pack(side="bottom", fill="x", pady=5)

    def agregar_corredor(self):
        win = tk.Toplevel(self.ventana)
        win.title("Nuevo Corredor")

        nombre = tk.Entry(win)
        numero = tk.Entry(win)
        tiempo = tk.Entry(win)

        for i, (label_text, entry) in enumerate([("Nombre", nombre), ("Número", numero), ("Tiempo", tiempo)]):
            tk.Label(win, text=label_text).grid(row=i, column=0)
            entry.grid(row=i, column=1)

        def guardar():
            try:
                c = Corredor(nombre.get(), int(numero.get()), tiempo.get())
                self.corredores.append(c)
                self.lista_corredores.insert(tk.END, f"{c.nombre} #{c.numero} - {c.tiempo}")
                win.destroy()
            except ValueError:
                messagebox.showerror("Error", "Número debe ser un entero.")

        tk.Button(win, text="Guardar", command=guardar).grid(row=3, columnspan=2)

    def guardar_evento(self):
        try:
            datos = {k: v.get() for k, v in self.campos.items()}

            if len(self.corredores) < 3:
                messagebox.showwarning("Datos incompletos", "Debes ingresar al menos 3 corredores para generar podio.")
                return

            ganadores = {
                "PrimerPuesto": {"Nombre": self.corredores[0].nombre, "Tiempo": self.corredores[0].tiempo},
                "SegundoPuesto": {"Nombre": self.corredores[1].nombre, "Tiempo": self.corredores[1].tiempo},
                "TercerPuesto": {"Nombre": self.corredores[2].nombre, "Tiempo": self.corredores[2].tiempo},
            }

            evento = Evento(
                datos["Nombre"],
                datos["Fecha"],
                datos["Tipo_carrera"],
                datos["Distancia"],
                int(datos["Cantidad_corredores"]),
                datos["Lugar"],
                datos["Record"],
                ganadores,
                self.corredores
            )

            agregar_evento(evento)
            self.confirmar_cierre()

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el evento.\n{str(e)}")

    def volver_a_inicio(self):
        # Cerramos la ventana de busqueda
        self.ventana.destroy()
        # Mostramos la ventana principal
        self.ventana_principal.deiconify()
        # Refrescamos la lista de archivos en la ventana principal, si es que la app lo tiene
        if hasattr(self.app, 'cargar_archivos'):
            self.app.cargar_archivos()

    def confirmar_cierre(self):
        respuesta = messagebox.showinfo("Éxito", "Evento guardado con éxito.")
        if respuesta == "ok":
            self.ventana.destroy()
            self.ventana_principal.deiconify()
            self.app.cargar_archivos()
