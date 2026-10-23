from pprint import pprint

# # 1. Eliminar los espacios en blanco de un string
# y devolver una lista con los caracteres restantes

# 2. Contar en un diccionario cuanto se repiten
# los caracteres de un string

# 3. Ordenar las llaves de un diccionario
# por el valor que tienen y devolver una lista
# que contiene tuplas [("a", 3), ("b", 2), ("c", 3), ("d", 4)]

# 4. de un listado de tuplas, devolver las tuplass
# que tengan el mayor valor.
# [("a", 3), ("b", 2), ("c", 4), ("d", 4)] -> [("c", 4), ("d", 4)]

# 5. Crear nu mensaje que diga:
# Los caracteres que mas se repiten con 4 repeticiones son:
# - C
# - D

# 6. Juntar la solucion de los ejercicios anteriores
# para encontrar los caracteres que mas se repiten de un string

string = "Hola mundo este es mi string"

# texto = texto.lower().replace(" ", "")

stringNoSpace = string.replace(" ", "")
print(string)
print(stringNoSpace)


def listar(texto):
    return [char for char in texto]


def cuentaCaracteres(lista):
    charsDict = {}
    for char in lista:
        if char in charsDict:
            charsDict[char] += 1
        else:
            charsDict[char] = 1
    return charsDict


def ordena(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True
    )


def mayoresTuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


def creaMensaje(diccionario):
    mensaje = "Los que mas se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key.upper()} con {valor} repeticiones \n"
    return mensaje


listado = listar(stringNoSpace)
contados = cuentaCaracteres(stringNoSpace)
ordenados = ordena(contados)
mayores = mayoresTuplas(ordenados)
mensaje = creaMensaje(mayores)
print(mensaje)
