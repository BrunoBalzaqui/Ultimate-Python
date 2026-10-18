# def hola():
#     print("Hola, mundo!")
#     print("Ultimate Python")


# hola()

# # En este ejemplo, la función hola() se define y luego se llama para ejecutar su contenido.
# # Al llamar a la función, se imprimen los mensajes "Hola, mundo!" y "Ultimate Python" en la consola.


# def hola(nombre, apellido):
#     print("Hola, mundo!")
#     print(f"Bienvenido, {nombre} {apellido}!")  # parametros


# hola("Bruno", "Balzaqui")  # argumentos
# hola("Juan", "Garcia")  # argumentos

# En este ejemplo, la función hola() se define con un parámetro nombre.
# Al llamar a la función, se pasan diferentes argumentos ("Bruno" y "Juan")
# Funciona de la siguiente manera: cuando se llama a la función hola("Bruno"), el valor "Bruno" se asigna al parámetro nombre, y se imprime "Bienvenido, Bruno!".


def hola(nombre, apellido="Feliz"):  # parametros con valor predeterminado opcional
    print("Hola, mundo!")
    print(f"Bienvenido, {nombre} {apellido}!")  # parametros


hola("Bruno", "Balzaqui")  # argumentos
hola("Juan")  # argumentos

# En este ejemplo, la función hola() se define con un parámetro nombre y un parámetro apellido con un valor predeterminado "Feliz".
# Al llamar a la función hola("Bruno", "Balzaqui"), se pasan ambos argumentos, y se imprime "Bienvenido, Bruno Balzaqui!".
# Al llamar a la función hola("Juan"), solo se pasa el argumento nombre, y el valor predeterminado "Feliz" se utiliza para el parámetro apellido, imprimiendo "Bienvenido, Juan Feliz!"


hola(apellido="Balzaqui", nombre="Bruno")  # argumentos con nombre

# En este ejemplo, la función hola() se llama utilizando argumentos con nombre.
# Al llamar a la función hola(apellido="Balzaqui", nombre="Bruno"),
# se especifica explícitamente qué valor corresponde a cada parámetro, independientemente del orden en que se definieron en la función.
# Esto permite mayor claridad y flexibilidad al llamar a la función
