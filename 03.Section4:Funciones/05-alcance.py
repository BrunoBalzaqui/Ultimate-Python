saludo = "Hola global"


def saludar():
    # print(saludo) # Esto imprimirá "Hola global" porque la variable `saludo` está definida en el ámbito global y es accesible dentro de la función `saludar`.
    saludo = "Hola Mundo"
    print(saludo)
    # Esto imprimirá "Hola Mundo" porque la variable `saludo` está definida dentro de la función `saludar`.


def saludaChanchito():
    saludo = "Hola Chanchito"
    # Esto imprimirá "Hola Chanchito" porque la variable `saludo` está definida dentro de la función `saludaChanchito`.
    print(saludo)


saludar()  # Llamada a la función `saludar`, que imprimirá "Hola Mundo".
saludaChanchito()  # Llamada a la función `saludaChanch
# Esto imprimirá "Hola global" porque la variable `saludo` está definida en el ámbito global y es accesible fuera de las funciones.
print(saludo)


# print(saludo)
# # Esto arrojara error porque la variable `saludo` no está definida en el ámbito global. La variable `saludo` solo existe dentro de
# # las funciones `saludar` y `saludaChanchito`, y no puede ser accedida fuera de ellas.

# NO es recomendable definir variables globales dentro de funciones, ya que puede llevar a confusión y errores en el código.
# Es mejor mantener las variables locales dentro de su función correspondiente para evitar conflictos de nombres y mantener un código más limpio y fácil de entender.

# En resumen, el alcance de las variables en Python determina dónde se pueden acceder y modificar.
# Las variables definidas dentro de una función son locales a esa función y no pueden ser accedidas desde fuera de ella,
# mientras que las variables definidas en el ámbito global pueden ser accedidas desde cualquier parte del código.

# Funciona de la siguiente manera:
# 1. Si una variable está definida dentro de una función, solo puede ser accedida dentro de esa función.
# 2. Si una variable está definida en el ámbito global, puede ser accedida desde cualquier parte del código, incluyendo dentro de funciones.
# 3. Si una variable local tiene el mismo nombre que una variable global, la variable local tendrá prioridad dentro de la función, y la variable global no será accesible dentro de esa función.
