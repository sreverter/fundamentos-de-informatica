def buscar_por_corredor(eventos, nombre):
    return [e for e in eventos if any(c.nombre == nombre for c in e.corredores)]