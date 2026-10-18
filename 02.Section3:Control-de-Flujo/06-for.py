# for numero in range(5):
#     print(numero, numero * "hola mundo ")

buscar = 5

for numero in range(5):
    if numero == buscar:
        print("Se encontró el número", buscar)
        break
    print(numero)
else:
    print("No se encontró el número", buscar)

for char in "Ultimate Python":
    print(char)

# for es una estructura de control de flujo que permite iterar sobre una secuencia de elementos, como listas, tuplas, cadenas de texto, entre otros.
# En el primer ejemplo, se utiliza un bucle for para iterar sobre un rango de números del 0 al 4 y se imprime cada número junto con la cadena "hola mundo".
