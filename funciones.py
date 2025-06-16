import random

def ingresar_nombre_carrera():
    nombre_carrera = input("Ingrese el nombre de la carrera: ")
    while nombre_carrera.strip() == "":
            nombre_carrera = input("El nombre de la carrera no puede estar vacío. Ingrese nuevamente: ")
    print("El nombre de la carrera es:", nombre_carrera)
    return nombre_carrera

def ingresar_cantidad_corredores():
    cantidad_corredores = input("Ingrese la cantidad de corredores (máximo 10): ")
    while not cantidad_corredores.isdigit() or int(cantidad_corredores) < 1 or int(cantidad_corredores) > 10:
        cantidad_corredores = input("Cantidad inválida. Ingrese un número entre 1 y 10: ")
    cantidad_corredores = int(cantidad_corredores)
    print("La cantidad de corredores es:", cantidad_corredores)
    return cantidad_corredores


#funcion que ingresa los datos de los corredores y los guarda en listas apareadas segun su numero, nombre y tiempo
def ingresar_data_corredores():
    cantidad = ingresar_cantidad_corredores()
    corredores_nombre = []
    corredores_numero = []
    corredores_tiempo = []
    for i in range(cantidad):
        nombre = input("Ingrese nombre del corredor: ")
        while nombre.strip() == "":
            nombre = input("El nombre no puede estar vacío. Ingrese nuevamente: ")
        corredores_nombre.append(nombre)
        #Logica de buscar numeros entre corredores
        numero_corredor = random.randint(1, cantidad)
        numero_repetido = busqueda_secuencial(numero_corredor, corredores_numero)
        if numero_repetido == False:
            corredores_numero.append(numero_corredor)
        else:
            while numero_repetido == True:
                numero_corredor = random.randint(1, cantidad)
                numero_repetido = busqueda_secuencial(numero_corredor, corredores_numero)
            corredores_numero.append(numero_corredor)
        # Ingreso del tiempo con validación
        print("Ingrese el tiempo del corredor (formato hh mm ss):")
        corredores_tiempo.append(ingresar_tiempo())
    mostrar_lista_corredores = input("Desea ver la lista de corredores? (si/no): ")
    if mostrar_lista_corredores.lower() == "si":
        for i in range(cantidad):
            print(f"Corredor N°{corredores_numero[i]}: {corredores_nombre[i]} con tiempo {convertir_a_hms(corredores_tiempo[i])}")
    return corredores_nombre, corredores_tiempo, corredores_numero


#funcion que compara los tiempos de los corredores para obtener el menor tiempo. Al usar listas apareadas, tambien se cambia el nombre y el numero teniendo en cuenta el tiempo del corredor
def metodoBurbuja(nombre, tiempo, numero):
    n = len(nombre)
    for i in range(n-1):
        cambio_realizado = False
        for j in range(0, n-i-1):
            if tiempo[j] > tiempo[j + 1]:
                tiempo[j], tiempo[j + 1] = tiempo[j + 1], tiempo[j]
                nombre[j], nombre[j + 1] = nombre[j + 1], nombre[j]
                numero[j], numero[j + 1] = numero[j + 1], numero[j]
                cambio_realizado = True
        if not cambio_realizado:
            break
    return nombre[0], tiempo[0], numero[0]  # Retorna el corredor con el menor tiempo


#funcion que busca si el numero del corredor ya esta y lo cambia con otro aleatorio
def busqueda_secuencial(valor, numeros):
    for i in range(len(numeros)):
        if numeros[i] == valor:
            return True  # Retorna True si se encuentra el número
    return False  # Retorna False si no se encuentra el número


# Funcion que permite ingresar un tiempo record y compara si es menor al tiempo del ganador
def ingresar_tiempo_record(tiempo_ganador):
    print("Ingrese el tiempo récord (formato hh mm ss):")
    tiempo_record = ingresar_tiempo()
    if tiempo_record > tiempo_ganador:
        print(f"Se ha roto el tiempo record. El nuevo tiempo record es: {tiempo_ganador}")
        print(f"Es decir: {convertir_a_hms(int(tiempo_record))}")
    else:
        print(f"No se ha roto el tiempo record. El tiempo record sigue siendo: {tiempo_record} segundos")
        print(f"Es decir: {convertir_a_hms(int(tiempo_record))}")


# Funcion que calcula el promedio de los tiempos de los corredores y lo muestra por pantalla
def calcular_promedios_tiempos(corredores):
    total_tiempo = 0
    n = len(corredores)
    for i in range(n):
        total_tiempo += corredores[i]
    promedio_tiempo = total_tiempo / n
    print(f"El promedio de tiempo de los corredores es: {promedio_tiempo} segundos")
    print(f"Es decir: {convertir_a_hms(int(promedio_tiempo))}")

# Función para validar ingreso del tiempo en formato correcto
def ingresar_tiempo():
    tiempo_valido = False
    tiempo_en_segundos = 0

    while not tiempo_valido:
        #try:
        h = int(input("Horas: "))
        m = int(input("Minutos: "))
        s = int(input("Segundos: "))
        if h < 0 or m < 0 or s < 0 or m >= 60 or s >= 60:
            print("Tiempo inválido. Los minutos y segundos deben estar entre 0 y 59.")
        else:
            tiempo_en_segundos = h * 3600 + m * 60 + s
            tiempo_valido = True
        #except ValueError:
        #    print("Ingresá solo números enteros.")
    
    return tiempo_en_segundos

# Función para convertir horas, minutos y segundos en segundos
def convertir_a_hms(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return f"{horas}h {minutos}m {segundos_restantes}s"
