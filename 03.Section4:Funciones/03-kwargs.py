def get_product(**datos):
    print(datos["nombre"], "$", datos["precio"])


# diccionario con los datos del producto
get_product(nombre="Laptop", precio=1500, marca="Dell", stock=20)

# En este ejemplo, la función `get_product` utiliza `**datos` para aceptar un número variable de argumentos con nombre (keyword arguments).
# Luego, accede a los valores del diccionario `datos` utilizando las claves correspondientes y los imprime.
# Funciona de la siguiente manera:
# - Cuando llamamos a `get_product(nombre="Laptop", precio=1500, marca="Dell", stock=20)`, la función accede a
# los valores de `nombre` y `precio` en el diccionario `datos` y los imprime, resultando en "Laptop $1500".
