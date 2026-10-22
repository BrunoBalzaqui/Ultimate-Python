def suma(a, b):
    resultado = a + b
    return resultado


c = suma(1, 2)
d = suma(c, 2)

print(d)

# En este ejemplo, la función `suma` toma dos argumentos `a` y `b`, calcula su suma y devuelve el resultado. Luego, se llama a la función dos veces: primero con los valores 1 y 2, y luego con el resultado de la primera llamada y el valor 2. Finalmente, se imprime el resultado final, que es 5.
# Funciona de la siguiente manera:
# - La primera llamada a `suma(1, 2)` devuelve 3, que se almacena en la variable `c`.
# - La segunda llamada a `suma(c, 2)` devuelve 5, que se almacena en la variable `d`.
# - Finalmente, `print(d)` imprime el valor 5 en la consola.
