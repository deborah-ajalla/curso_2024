#CLASE 16 de Julio
# analizar el código y explicar que hace cada linea,
# luego reemplazarlo por otra condición
#-----------------------------------------------------
#WHILE
n = 10                                 # --> 👉🏻 se declara la variable "n" (contador) y tiene asignado el valor 10.

while n<10:                            # --> 👉🏻 se inicia un bucle "while" que tiene como condicion que se va a repetir
                                                 #mientras n sea menor que 10.
    if (n%2)==0:                       # --> 👉🏻 se declara una condición "si el módulo 2" arroja resultado cero. 
        print(n,"Es un numero par")    # --> 👉🏻 se imprime "n, es un número par".
    else:                              # --> 👉🏻 si no se cumple la condición
        print(n,"es un numero impar")  # --> 👉🏻 se imprime "n, es un número impar".
    n+=1                               # --> 👉🏻 se indica que en cada iteración el contador (variable n) incrementa en 1.
    
#  IF ELSE ELIF
# Construir un algoritmo con lo viste en clase bajo el mismo diagrama de flujo de la imagen que está en la carpeta assets del repo