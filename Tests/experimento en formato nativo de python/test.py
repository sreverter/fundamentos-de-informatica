#diccinarios bases
base_info_carrera = {'cantidad_competidores':1, 'record':0}
base_competidor = {'numero':1, 'tiempo':0}

#el diccionario raiz, donde se pone toda la info recolectada
#esta en el formato nativo de python, se puede convertir directamente a xml o json usando librerias
raiz = {}


def obtener_info_cmd(base_seleccionada): #promptear a la terminal para llenar cada objeto dentro dentro del diccionario base seleccionado
    diccionario_base = base_seleccionada.copy() #crea una copia del diccionario base, que se llenara de información
    for i in diccionario_base:
        print('poner_valor_para:', i)
        diccionario_base[i] = input()
    return diccionario_base #la funcion devuelve la copia del diccionario base, llena de la info prompteada

def instanciar_competidores(): #corre un obtener info cmd por cada competidor que haya que añadir; usando el archivo base 'competidor'
    iteraciones = 0
    while iteraciones < int(raiz['info_carrera']['cantidad_competidores']):
        print('competidor:', iteraciones + 1)
        raiz['competidores'][iteraciones] = obtener_info_cmd(base_competidor) #añadirle a raiz un subnivel unico y llenarlo con los datos del competidor
        iteraciones = iteraciones + 1
        

print('info de la carrera')
raiz['info_carrera'] = obtener_info_cmd(base_info_carrera) #añadirle a raiz el subinivel 'info carrera' y dentro de ese subnivel promptear a la terminal para que lo llene c'el contenido en base al archivo base 'info carrera'

print('info de los competidores')
raiz['competidores'] = {} #crear un subnivel
instanciar_competidores() #añadir competidores

print(raiz)
