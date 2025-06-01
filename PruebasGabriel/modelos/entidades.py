class Corredor:
    def __init__(self, nombre, numero, tiempo):
        self.nombre = nombre
        self.numero = numero
        self.tiempo = tiempo

class Evento:
    def __init__(self, nombre, fecha, tipo_carrera, distancia, cantidad_corredores, lugar, record, ganadores, corredores):
        self.nombre = nombre
        self.fecha = fecha
        self.tipo_carrera = tipo_carrera
        self.distancia = distancia
        self.cantidad_corredores = cantidad_corredores
        self.lugar = lugar
        self.record = record
        self.ganadores = ganadores
        self.corredores = corredores