import funciones as prueba
#import random

#ingresar_nombre_carrera()
#    carrera_nombre = ingrese nombre de la carrera_nombre
# Se ingresa el nombre de la carrera

prueba.ingresar_nombre_carrera()

#ingresar_cantidad_corredores()
#    cantidad_corredores = ingrese cantidad de corredores
# Se ingresa la cantidad de corredores que van a participar en la carrera

cantidad = prueba.ingresar_cantidad_corredores() 

'''
class Corredor:
    def __init__(self, nombre, edad, tiempo, numero):
        mostrar por pantalla (Creando corredor {nombre} con edad {edad} de numero {numero} y tiempo {tiempo})
        self.nombre = nombre
        self.edad = edad
        self.tiempo = tiempo
        self.numero = numero
'''
#Se crea el objeto Corredor para guardarlo dentro de un arreglo
class Corredor:
    def __init__(self, nombre, tiempo, numero):
        print(f"Creando corredor con el nombre {nombre}, el numero {numero}, y el tiempo de {tiempo}")
        self.nombre = nombre
        self.tiempo = tiempo
        self.numero = numero
        pass


'''
ingresar_data_corredores()
    corredores = []
    para i en rango de (cantidad de corredores):
        nombre = ingrese nombre del corredor
        edad = ingrese edad del corredor
        tiempo = ingrese tiempo del corredor
        random.randint(1, cantidad de corredores) 
        corredores[i] = Corredor(nombre, edad, tiempo, numero)
    devolver corredores
'''
# Funcion en la cual se ingresan los datos de los corredores y se guardan en un arreglo de objetos Corredor

def ingresar_data_corredores():
    corredores = []
    for i in range (cantidad):
        nombre = input("Ingrese nombre del corredor: ")
        tiempo = int(input("Ingrese tiempo del corredor: "))
        #numero = random.randint(1, cantidad)
        numero = i + 1
        corredores.append(Corredor(nombre, tiempo, numero))
        print(corredores)
    return corredores

'''
mostrar_ganador()
    para i en rango de (cantidad de corredores):

### comparamos los tiempos de los corredores para obtener el menor tiempo y el numero correspondiente del corredor que hizo dicho tiempo. Se va a ver que tipo de busqueda es la mejor para realizar este problema

        tiempo_ganador = corredores[i].tiempo
        numero_ganador = corredores[i].numero
        tiempo_a_comparar = corredores[i+1].tiempo
        numero_a_comparar = corredores[i+1].numero
        si tiempo_ganador es mayor a tiempo_a_comparar:
            tiempo_ganador = tiempo a comparar
            numero_ganador = numero_a_comparar
            incrementar en 1 i
        sino
            incrementar en 1 i
        mostrar tiempo_ganador
            

'''

def metodoBurbuja(corredores):
    n = len(corredores)
    for recorrido in range (1, n):
        for i in range (len(corredores) - recorrido):
            if corredores[i].tiempo > corredores[i + 1].tiempo:
                corredores[i], corredores[i + 1] = corredores[i + 1], corredores[i]
    return corredores[0]  # Retorna el corredor con el menor tiempo

'''
ingresar_tiempo_record()
    tiempo_record = ingrese tiempo record
    si tiempo_record < tiempo_ganador
        mostrar "Se ha roto el tiempo record. El nuevo tiempo record es: {tiempo_record}"
'''

def ingresar_tiempo_record():
    tiempo_record = int(input("Ingrese el tiempo record: "))
    if tiempo_record > tiempo_ganador:
        print(f"Se ha roto el tiempo record. El nuevo tiempo record es: {tiempo_record}")
    else:
        print(f"No se ha roto el tiempo record. El tiempo record sigue siendo: {tiempo_record} segundos")


'''
calcular_promedios_tiempos()
    total_tiempo = 0
    total_tiempo = total_tiempo + corredores[i].tiempo
    promedio_tiempo = total_tiempo / cantidad_corredores
    mostrar promedio_tiempo
'''

def calcular_promedios_tiempos(corredores):
    total_tiempo = 0
    n = len(corredores)
    for i in range(n):
        total_tiempo += corredores[i].tiempo
    promedio_tiempo = total_tiempo / n
    print(f"El promedio de tiempo de los corredores es: {promedio_tiempo} segundos")



#Recorrido normal del programa

lista_corredores = ingresar_data_corredores()

checkear_ganador = input("¿Desea ver al ganador? (si/no): ")
if checkear_ganador == "si":
    ganador = metodoBurbuja(lista_corredores)
    print(f"El ganador es {ganador.nombre} con el tiempo de {ganador.tiempo} segundos y el numero de corredor {ganador.numero}")
    tiempo_ganador = ganador.tiempo
ingreso_tiempo_record = input("¿Desea ingresar el tiempo record? (si/no): ")
if ingreso_tiempo_record == "si":
    ingresar_tiempo_record()
mostrar_promedio = input("¿Desea ver el promedio de tiempos? (si/no): ")
if mostrar_promedio == "si":
    calcular_promedios_tiempos(lista_corredores)

