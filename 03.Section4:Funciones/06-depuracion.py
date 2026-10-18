def largo(texto):
    resultado = 0
    for char in texto:
        resultado += 1
    return resultado


print("chanchito")
l = largo("Hola Mundo")
# Esto imprimirá 1, ya que la función retorna el valor de`resultado` en la primera iteración del bucle, antes de contar todos los caracteres del texto.
print(l)

# En este ejemplo, la función `largo` cuenta el número de caracteres en una cadena de texto. La variable `resultado` se inicializa en 0 y se incrementa en 1 por cada carácter en el texto.
# Al final, la función retorna el valor de `resultado`, que representa la longitud del texto.
# Funciona de la siguiente manera:
# 1. La función `largo` recibe un parámetro `texto`, que es la cadena de texto que se desea medir.
# 2. Se inicializa la variable `resultado` en 0, que se utilizará para contar los caracteres.
# 3. Se utiliza un bucle `for` para iterar sobre cada carácter en el texto.
# 4. Por cada carácter, se incrementa la variable `resultado` en 1.
# 5. Al final del bucle, la función retorna el valor de `resultado`, que representa la longitud del texto.
# 6. Finalmente, se imprime el valor retornado por la función `largo`, que es la longitud de la cadena "Hola Mundo", que es 10.
