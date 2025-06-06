import funciones as funcion

#Recorrido normal del programa

nombre_carrera = funcion.ingresar_nombre_carrera()

nombres, tiempos, numeros = funcion.ingresar_data_corredores()

ganador = None
checkear_ganador = input("¿Desea ver al ganador? (si/no): ")
if checkear_ganador == "si":
    ganador = funcion.metodoBurbuja(nombres, tiempos, numeros)
    print(f"El ganador es {ganador[0]} con un tiempo de {funcion.convertir_a_hms(ganador[1])} y el número de corredor {ganador[2]}")
    tiempo_ganador = ganador[1]

ingreso_tiempo_record = input("¿Desea ingresar el tiempo record? (si/no): ")
if ingreso_tiempo_record == "si":
    if ganador is not None:
        funcion.ingresar_tiempo_record(ganador[1])
    else:
        print("Primero necesitás ver al ganador para comparar con el récord.")
    
mostrar_promedio = input("¿Desea ver el promedio de tiempos? (si/no): ")
if mostrar_promedio == "si":
    funcion.calcular_promedios_tiempos(tiempos)


# Fin del recorrido normal del programa