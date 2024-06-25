#LONGITUD DE CADENA --> FUNCION LEN <--

esto_es_un_string = "hola, soy un string"

print (len (esto_es_un_string))
#--------------------------------------------
string = "    "
print( len(string))
#--------------------------------------------

#REBANAR UN STRING --> SLICING <--
# [INICIO : FIN : PASO]
"""
inicio: el imdice del primer caracter del string q queremos rebanar
fin: el indice del ultimo caracter no incluido en la cadena
paso: cada cuantos caracteres se selecciona inicio y fin
"""

saludo = "hola, como estan?"
print (len (saludo))

saludo [0:3:1]
print (saludo[0:3:1])
#-----------------------------------------

palabra = "pithon"
print (palabra)
print (palabra[1])
#como la cadena es inmutable y n puedo reemplazar solo un caracter: 
palabra = palabra[0:1] + "y" + palabra [2:]
#imprime python
print (palabra)

#-----------------------------------------------------------------------
#  --> LISTAS Y TUPLAS <--
mi_lista = [-11, 20, 3, 41]
print("esta es mi lista: ")
print (mi_lista)

otra_lista = ["Hola", "Como", "estas", "?"]
print("esta es otra lista")
print(otra_lista)

variable_1 = "una variable"

listita = [1, -10, 132.5, "un string", "otro string", variable_1]
print ("Una lista con varios tipos de datos")
print(listita)

#accedo a elementos por posicion
print(listita[0])
print (listita [-1])

#concateno listas
print (listita + [otra_lista, "algo random"])


