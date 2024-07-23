#CLASE 16 de Julio

# analizar el código y explicar que hace cada linea ✔
# luego reemplazarlo por otra condición ✔
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
    
# 🔸 Código Modificado 🔸

n = 0                          # --> 👉🏻 se declara la variable "n" (contador) y tiene asignado el valor 0.

while n < 6:                   # --> 👉🏻 se inicia un bucle "while" que tiene como condicion que se va a repetir
                                         #mientras n sea menor que 6.
    if (n == 2):               # --> 👉🏻 se declara una condición "si n es igual a 2"
        print (n, "es 2")      # --> 👉🏻 se imprime "n, es 2".
    else:                      # --> 👉🏻 si no se cumple la condición
        print (n, "No es 2")   # --> 👉🏻 se imprime "n, no es 2".
    n+=1                       # --> 👉🏻 se indica que en cada iteración el contador (variable n) incrementa en 1.

#---------------------------------------------------------------------------------------------------------------
#  IF ELSE ELIF
# Construir un algoritmo con lo viste en clase bajo el mismo diagrama de flujo de la imagen que está en la carpeta assets del repo

print ("\t------------------------------------------- \n")
print ("\t********* BIENVENIDO AL PROGRAMA *********\n")

print (" Presione s/n para operar en el sistema...")
entrar = input (">> Desea Ingresar?:  ")

if entrar == "s":
    print ("🔹🔹 Bienvenida/o al sistema!!! 🔹🔹")
elif entrar == "n":
    ingreso = input (">> Quiere ingresar su nombre? s/n: ")
    if ingreso == "s":
        print (" Hola! Cómo estás??")
    else: 
        salir = input (">> Quiere Salir del Sistema? s/n: ")
        if salir == "s":
            print ("Ud ha salido exitosamente!!!")
            print ("----------------------------\n")
        else:
            print ("\t ❌ No se reconoce el comando ❌")
            print (" \t Vuelva a Intentarlo!! \n")   
else:
    print (">> SOLO DEBE INGRESAR s/n: ")