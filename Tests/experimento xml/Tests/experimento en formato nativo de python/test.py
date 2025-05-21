#bases
info_carrera = {'cantidad_competidores':1, 'record':0}
competidor = {'numero':1, 'tiempo':0}

#el diccionario raiz, donde se pone toda la info recolectada
#esta en el formato nativo de python, se puede convertir directamente a xml o json usando librerias
raiz = {}


def obtener_info_cmd(base):
    diccionario = base.copy()
    for i in diccionario:
        print('poner_valor_para:', i)
        diccionario[i] = input()
    return diccionario

def instanciar_competidores():
    iteraciones = 0
    while iteraciones < int(raiz['info_carrera']['cantidad_competidores']):
        print('competidor:', iteraciones + 1)
        raiz[iteraciones] = obtener_info_cmd(competidor)
        iteraciones = iteraciones + 1
        

print('info de la carrera')
raiz['info_carrera'] = obtener_info_cmd(info_carrera)

print('info de los competidores')
instanciar_competidores()

print(raiz)
