import xml.etree.ElementTree as ET
bufer = '/home/Azul/Proyects/Fundamentoas Info./TP0/experimento xml/test.xml'
file = ET.parse(bufer)
root = file.getroot()
#actuamente esto esta medio roto
#si hay mas de una raiz en el xml da error
#igual es un tema de la libreria, va a haber que ver como configurarla para que se puede hacer eso

#esta funcion imprime todo un nivel, con su contenido y subniveles. hasta 3 niveles
def imprimir_nivel(nivel_1=None, nivel_2=None, nivel_3=None):
    if nivel_3 != None:
        direccion = root[nivel_1][nivel_2][nivel_3]
    elif nivel_2 != None:
        direccion = root[nivel_1][nivel_2]
    elif nivel_1 != None:
        direccion = root[nivel_1]
    else:
        direccion = root

    print(direccion.tag)
    for child in direccion:
        print('|->',child.tag,':', child.text)
        if len(child):
            for subchild in child:
                print('   |->',subchild.tag,':', subchild.text)
                if len(child):
                    for sub2child in subchild:
                        print('      |->',sub2child.tag,':', sub2child.text)


imprimir_nivel()


