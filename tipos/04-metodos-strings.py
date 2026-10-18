animal = "chanchito feliz"
print(animal.upper())  # Convierte a mayúsculas
print(animal.lower())  # Convierte a minúsculas
print(animal.title())  # Convierte a formato de título
print(animal.strip())  # Elimina espacios en blanco
print(animal.lstrip())  # Elimina espacios en blanco a la izquierda
print(animal.rstrip())  # Elimina espacios en blanco a la derecha
# Reemplaza una subcadena por otra
print(animal.replace("chanchito", "perrito"))
print(animal.split())  # Divide la cadena en una lista de palabras
print("chanchito" in animal)  # Verifica si una subcadena está en la cadena
# Verifica si una subcadena no está en la cadena
print("perrito" not in animal)
# Verifica si la cadena comienza con una subcadena
print(animal.startswith("chan"))
# Verifica si la cadena termina con una subcadena
print(animal.endswith("feliz"))
