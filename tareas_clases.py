#TAREA:

#CLASE 18/6: CREAR UN SCRIPT EN EL QUE PODAMOS CALCULAR LA NOTA FINAL EN BASE A 5 EXAMENES, ESTOS EXAMENES EQUIVALEN A UN PORCENTAJE DE LA NOTA FINAL.

# LA NOTA NUMERO 1 CORRESPONDE AL 20% DE LA NOTA FINAL.
# LA NOTA NUMERO 2 CORRESPONDE AL 10% DE LA NOTA FINAL.
# LA NOTA NUMERO 3 CORRESPONDE AL 10% DE LA NOTA FINAL.
# LA NOTA NUMERO 4 CORRESPONDE AL 10% DE LA NOTA FINAL.
# LA NOTA NUMERO 5 CORRESPONDE AL 50% DE LA NOTA FINAL.

#A esto se lo suele llamar promedio ponderado: no todos los valores tienen el mismo "peso".
#Por ejemplo, dado el ejercicio de arriba me conviene sacarme una mejor nota en el examen donde la nota vale casi el 50% de la nota final.

#-------------------------------------------------------------------------------------------------------------------------------
print ("---------------------------------------------------------------------")

print ("El presente programa permite la carga de notas y obtiene su promedio")

print ("---------------------------------------------------------------------")

#Carga de Datos:
nota1 = int (input("Ingrese la primera nota: "))
nota2 = int (input ("Ingrese la segunda nota: "))
nota3 = int (input ("Ingrese la tercera nota: "))
nota4 = int (input ("Ingrese la cuarta nota: "))
nota5 = int (input ("Ingrese la quinta nota: "))

#Función:  PROMEDIO PONDERADO 
# --> multiplicar cada nota por su respectivo porcentaje <--
nota1 = nota1 * 0.2
nota2 = nota2 * 0.1
nota3 = nota3 * 0.1
nota4 = nota4 * 0.1
nota5 = nota5 * 0.5

#--> se suman los resultados obtenidos <--
nota_promedio = nota1 + nota2 + nota3 + nota4 + nota5

# --> se imprime el resultado <--
print ("---------------------------------------------------------------------")
print (" --> El Promedio es:", nota_promedio)
print ("---------------------------------------------------------------------")
print("GRACIAS POR USAR NUESTRO PROGRAMA!!!")


