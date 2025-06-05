titulo_detalles_carrera = ['cantidad corredores', 'record']
detalles_carrera = []

corredores_indice = []
corredores_numero = [] 
corredores_tiempo = []

'''
def obtener_info_cmd(lista_titulos, lista_datos): #promptear a la terminal para llenar cada objeto

    for i in lista_titulos:
        print('poner_valor_para:', lista_titulos[i])
        lista_datos[i] = input()
#fin


def instanciar_competidores(): #corre un obtener info cmd por cada competidor que haya que añadir; usando el archivo base 'competidor'
    #terminar

#fin  
'''

def ordenar(indice, valores):

    #sorteador de burbuja sacado del internet
    # Outer loop to iterate through the list n times
    for n in range(len(indice) - 1, 0, -1):
        
        # Initialize swapped to track if any swaps occur
        swapped = False  

        # Inner loop to compare adjacent elements
        for i in range(n):
            if valores[indice[i]] > valores[indice[i + 1]]: #compara los valores del array de valores, que el array indice apunta
              
                # Swap elements if they are in the wrong order
                #al sortear, mueve los valores del indice alrededor, no los de valores
                indice[i], indice[i + 1] = indice[i + 1], indice[i] 
                
                # Mark that a swap has occurred
                swapped = True
        
        # If no swaps occurred, the list is already sorted
        if not swapped:
            break        
#fin

def imprimir_lista_indexada(indice,valores):

    i = 0
    while i < len(indice):
        print(valores[indice[i]], '(indx:', indice[i], ')' ,end=', ')
        i += 1
    print('')#newline al final
#fin


#main
#main
#main

'''
print('info de la carrera')
obtener_info_cmd(titulo_detalles_carrera, detalles_carrera) #añadirle a raiz el subinivel 'info carrera' y dentro de ese subnivel promptear a la terminal para que lo llene c'el contenido en base al archivo base 'info carrera'

print('info de los competidores')
raiz['competidores'] = {} #crear un subnivel
instanciar_competidores() #añadir competidores

print(raiz)
'''

corredores_indice = [0,1,2,3,4,5]
corredores_numero = [21,22,23,24,25,26] 
corredores_tiempo = [8,9,10,5,6,4]

ordenar(corredores_indice, corredores_tiempo)

print('tiempo sin sortear:', corredores_tiempo)
print('numero sin sortear:', corredores_numero)

print('tiempo sorteado:', end='')
imprimir_lista_indexada(corredores_indice, corredores_tiempo)
print('numero sorteado:', end='')
imprimir_lista_indexada(corredores_indice, corredores_numero)