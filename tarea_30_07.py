# SETS
# En una variable grupo:
print ("\n ----------------------------------------------")
grupo = {"Fernando", "Federico", "Francisco", "Ricardo"}
print ("Integrantes Iniciales del Grupo: \n", grupo)

# 1) --> Añadir a las siguientes personas: Jose, Maria, Gerardo, Fabian

grupo.add ("Jose") 
grupo.add ("Maria")
grupo.add ("Gerardo")
grupo.add ("Fabian")
print ("\n ----------------------------------------------")
print ("Se añaden integrantes al grupo: \n", grupo)


# 2) --> Eliminar a las personas: Fernando, Federico, Francisco
print ("\n ----------------------------------------------")
grupo.remove("Fernando")
print ("Grupo actualizado sin 'Fernando': \n", grupo)
print ("\n")

grupo.remove ("Federico")
print ("Grupo actualizado sin 'Federico': \n", grupo)
print ("\n")

grupo.remove ("Francisco")
print ("Grupo actualizado sin 'Francisco': \n", grupo)
#----------------------------------------------------------------------------------------------
# DICCIONARIOS
print ("\n ----------------------------------------------")
animalitos = {"elefante": ""}
# Añadir al diccionario las claves perro, gato y tucan con sus valores "Tobi", "Michi" y "Diego"

# Modificar la clave elefante por delfin