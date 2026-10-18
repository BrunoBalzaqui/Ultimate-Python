def es_palindromo(texto):
    # Convertir el texto a minúsculas y eliminar espacios
    texto = texto.lower().replace(" ", "")
    # Comparar el texto con su reverso
    return texto == texto[::-1]
# Como funciona texto[::-1]: Esto es un ejemplo de rebanado (slicing) en Python. La notación [::-1] se utiliza para invertir una secuencia, como una cadena de texto.
# En este caso, se está comparando el texto original con su versión invertida para determinar si es un palíndromo.


print("Abba", es_palindromo("Abba"))  # True
print("Reconocer", es_palindromo("Reconocer"))  # True
print("Hola mundo", es_palindromo("Hola mundo"))  # False


# Como funciona la función `es_palindromo`:
# 1. La función recibe un parámetro `texto`, que es la cadena de texto que se desea verificar si es un palíndromo.
# 2. Se convierte el texto a minúsculas utilizando el método `lower()` para que la comparación no sea sensible a mayúsculas y minúsculas.
# 3. Se eliminan los espacios en blanco utilizando el método `replace(" ", "")` para que la comparación no se vea afectada por los espacios.
# 4. Se compara el texto con su reverso utilizando la notación de rebanado `texto[::-1]`, que invierte la cadena.
# 5. La función retorna `True` si el texto es igual a su reverso (es un palíndromo) y `False` en caso contrario.
# 6. Finalmente, se imprimen los resultados de la función `es_palindromo` para diferentes cadenas de texto, mostrando si son palíndromos o no.
