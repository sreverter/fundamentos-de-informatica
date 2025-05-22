import os
import json
from modelos.entidades import Evento

eventos = []

def agregar_evento(evento):
    eventos.append(evento)
    guardar_evento_json(evento)

def guardar_evento_json(evento):
    datos = {
        "Nombre": evento.nombre,
        "Fecha": evento.fecha,
        "Tipo": evento.tipo,
        "Distancia": evento.distancia,
        "Cantidad": evento.cantidad,
        "Lugar": evento.lugar,
        "Record": evento.record,
        "Ganadores": evento.ganadores,
        "Corredores": [
            {"Nombre": c.nombre, "Numero": c.numero, "Tiempo": c.tiempo}
            for c in evento.corredores
        ]
    }

    carpeta = os.path.join(os.path.dirname(__file__), "..", "Datos")
    os.makedirs(carpeta, exist_ok=True)

    nombre_archivo = f"{evento.nombre.replace(' ', '_')}_{evento.fecha.replace('-', '')}.json"
    ruta_archivo = os.path.join(carpeta, nombre_archivo)

    with open(ruta_archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)