def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print("La suma es:", resultado)


suma(2, 5)
suma(10, 20, 30)
suma(1, 2, 3, 4, 5)

# En este ejemplo, la función `suma` utiliza `*numeros` para aceptar un número variable de argumentos. Luego, recorre cada número en `numeros`, los suma y finalmente imprime el resultado.
# Funciona de la siguiente manera:
# - Cuando llamamos a `suma(2, 5)`, la función suma 2 y 5, resultando en 7.
# - Cuando llamamos a `suma(10, 20, 30)`, la función suma 10, 20 y 30, resultando en 60.
# - Cuando llamamos a `suma(1, 2, 3, 4, 5)`, la función suma 1, 2, 3, 4 y 5, resultando en 15.
