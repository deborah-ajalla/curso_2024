
# 🔸 TAREA DE CLASE 25/6: 🔸
# TENIENDO DOS LISTAS : lista_1 y lista_2  👉🏻hay que hacer los siguientes ejercicios:

#Añadir a la lista_1 el entero 4567 y despues el string "UNAHUR"
print("///////////////////////////////////////")
print("▶ creo listas y agrego contenido")
# --> creo listas vacias
lista_1 = []
lista_2 = []
print("lista 1 = ", lista_1)
print("lista 1 = ", lista_2)

# --> agrego contenido
lista_1.append(4567)
lista_2.append("UNAHUR")
print("listas con contenido: ")
print("Lista 1:", lista_1)
print("Lista 2:", lista_2)

#------------------------------------------------------------------
#Añadir a la lista_2 el string "EDUCACION" y despues el entero 789
print("/////////////////////////////////////// \n")
print("▶ agrego contenido a lista 2")

lista_2.append ("EDUCACION")
lista_2.append (789)

# --> imprimo resultado
print("Contenido Actualizado de lista 2= ", lista_2)

#------------------------------------------------------------------
#Crear una lista_3 con todos los elementos de la lista_2 MENOS el último
print("///////////////////////////////////////  \n")
print("▶ creo lista 3 con algunos elementos de lista 2")
lista_3 = lista_2[0:2]

print ("Contenido de lista 3= ", lista_3)

#------------------------------------------------------------------
#Crear una lista_4 con todos los elementos de la lista_2 MENOS el primero y último
print("///////////////////////////////////////  \n")
print("▶ creo lista 4 con algunos elementos de lista 2")
lista_4 = []
lista_4.append(lista_2[1])
print ("Contenido de lista 4 = ", lista_4)

#------------------------------------------------------------------
#Crear una lista_5 con todos los elementos de la lista_3 y de la lista_4
print("///////////////////////////////////////  \n")
print("▶ creo lista 5 con elementos de lista 3 y lista 4: ")

print("Lista 3: ", lista_3)
print("Lista 4: ", lista_4)
lista_5 = []
print("Lista 5: ", lista_5)

lista_5 = lista_3   #-> agrego contenido de lista 3
lista_5.append(lista_4)  # -> agrego contenido de lista 4
print ("Lista 5 con contenido de dos listas: ", lista_5)

#------------------------------------------------------------------
# 🔸 AHORA CON TUPLAS 🔸

#Crear una variable llamada tupla con más de 15 items y printear lo siguiente:
print("-------------------------------------------------  \n")
print("▶ creo TUPLA con 15 elementos: ")

tupla = ("té","café", "yerba", "agua", "jugo", ["manzana", "pera", "durazno", "ananá"], "gaseosa",
          "galletitas", "mermelada", "dulce de leche", "edulcorante", "aceite", "aceite de oliva",
          "arroz parboil", "mayonesa", "mostaza" )
print ( "😉 Mi tupla de productos: \n", tupla)

# 1- El ultimo item de la tupla creada.
print("-------------------------------------------------  \n")
print("▶ Último producto: ", tupla[-1])

#------------------------------------------------------------------
# 2- el numero de items de la misma, 
print("-------------------------------------------------  \n")
print("▶ Cantidad de Elementos de mi TUPLA: ", len (tupla))

#------------------------------------------------------------------
# 3- la posicion donde se encuentra algun item que haya dentro, 
print("-------------------------------------------------  \n")
print("▶  El segundo elemento de mi TUPLA es: ", tupla[1])

#------------------------------------------------------------------
# 4- una lista con los ultimos cuatro items de la tupla, 
print("-------------------------------------------------  \n")
print ( "😉 Mi tupla de productos: \n", tupla)
print("▶ Los últimos cuatro elementos de mi TUPLA son: ", tupla[-4:])

#------------------------------------------------------------------
# 5- un item que haya en la posicion 8, 
print("-------------------------------------------------  \n")
print("▶  El elemento de la posición ocho es: ", tupla[7])

#------------------------------------------------------------------
# 6- el numero de veces que se repite algún item dentro de la misma.
print("-------------------------------------------------  \n")
print("▶  Número de veces que se repite 'yogur' dentro de mi TUPLA: ", tupla.count("yogur"))

#------------------------------------------------------------------
print("\t \t ------------------------------")
print("\t \t 🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹")
print(" \t \t  ------ FIN DEL PROGRAMA ----- ")
print("\t \t 🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹")

