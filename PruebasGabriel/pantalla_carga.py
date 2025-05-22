import tkinter as tk
from modelos.entidades import Evento, Corredor
from logica.abm_eventos import agregar_evento

class PantallaCarga:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root)
        self.frame.pack()

        self.campos = {}
        for campo in ["Nombre", "Fecha", "Tipo", "Distancia", "Cantidad", "Lugar", "Record"]:
            tk.Label(self.frame, text=campo).pack()
            entry = tk.Entry(self.frame)
            entry.pack()
            self.campos[campo] = entry

        self.corredores = []
        self.botón_corredor = tk.Button(self.frame, text="Agregar Corredor", command=self.agregar_corredor)
        self.botón_corredor.pack()

        self.lista_corredores = tk.Listbox(self.frame)
        self.lista_corredores.pack()

        tk.Button(self.frame, text="Guardar Evento", command=self.guardar_evento).pack()

    def agregar_corredor(self):
        win = tk.Toplevel(self.root)
        win.title("Nuevo Corredor")

        nombre = tk.Entry(win)
        numero = tk.Entry(win)
        tiempo = tk.Entry(win)

        for i, (lbl, ent) in enumerate([("Nombre", nombre), ("Número", numero), ("Tiempo", tiempo)]):
            tk.Label(win, text=lbl).grid(row=i, column=0)
            ent.grid(row=i, column=1)

        def guardar():
            c = Corredor(nombre.get(), int(numero.get()), tiempo.get())
            self.corredores.append(c)
            self.lista_corredores.insert(tk.END, f"{c.nombre} #{c.numero} - {c.tiempo}")
            win.destroy()

        tk.Button(win, text="Guardar", command=guardar).grid(row=3, columnspan=2)

    def guardar_evento(self):
        datos = {k: v.get() for k, v in self.campos.items()}
        ganadores = {
            "PrimerPuesto": {"Nombre": self.corredores[0].nombre, "Tiempo": self.corredores[0].tiempo},
            "SegundoPuesto": {"Nombre": self.corredores[1].nombre, "Tiempo": self.corredores[1].tiempo},
            "TercerPuesto": {"Nombre": self.corredores[2].nombre, "Tiempo": self.corredores[2].tiempo},
        }
        evento = Evento(
            datos["Nombre"], datos["Fecha"], datos["Tipo"], datos["Distancia"],
            int(datos["Cantidad"]), datos["Lugar"], datos["Record"],
            ganadores, self.corredores
        )
        agregar_evento(evento)
        tk.Label(self.frame, text="Evento guardado con éxito.").pack()