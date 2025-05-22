class Corredor:
    def __init__(self, nombre, numero, tiempo):
        self.nombre = nombre
        self.numero = numero
        self.tiempo = tiempo

class Evento:
    def __init__(self, nombre, fecha, tipo, distancia, cantidad, lugar, record, ganadores, corredores):
        self.nombre = nombre
        self.fecha = fecha
        self.tipo = tipo
        self.distancia = distancia
        self.cantidad = cantidad
        self.lugar = lugar
        self.record = record
        self.ganadores = ganadores
        self.corredores = corredores