# numero = 1
# while numero <= 100:
#     print(numero)
#     numero *= 3

# # while funciona de manera similar a for, pero no tiene un límite definido, por lo que se debe tener cuidado de no crear un bucle infinito.


# comando = ""

# while comando.lower() != "salir":
#     comando = input("$ ")
#     print(comando)

# En este ejemplo, se utiliza un bucle while para solicitar al usuario que ingrese un comando.
# El bucle continuará ejecutándose hasta que el usuario ingrese la palabra "salir",
# momento en el cual se detendrá la ejecución del bucle y se imprimirá el último comando ingresado por el usuario.


comando = ""

while True:
    comando = input("$ ")
    if comando.lower() == "salir":
        break
    print(comando)

# En este ejemplo, se utiliza un bucle while con la condición True para crear un bucle infinito.
# Dentro del bucle, se solicita al usuario que ingrese un comando y se verifica si el comando ingresado es "salir".
# Si es así, se utiliza la instrucción break para salir del bucle. De lo contrario, se imprime el comando ingresado por el usuario.
