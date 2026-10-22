edad = int(input("Ingrese su edad: "))

if edad > 64:
    print("Puede ver la pelicula con SUPER descuento")
elif edad > 54:
    print("Puede ver la pelicula con descuento")
elif edad > 17:
    print("Puede ver la pelicula")
else:
    print("No puede ver la pelicula")

print("Listo")

# En este ejemplo, se utiliza una estructura if-elif-else para evaluar la edad ingresada por el usuario y determinar
# si puede ver la película con descuento, sin descuento o no puede verla.
