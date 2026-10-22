numeros = [2, 5, 1, 45, 75, 22]

# numeros.sort(reverse=True)
numeros2 = sorted(numeros, reverse=True)

print(numeros)
print(numeros2)


usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]


# def ordena(elemento):
#     return elemento[1]


usuarios.sort(key=lambda el: el[1])
print(usuarios)
