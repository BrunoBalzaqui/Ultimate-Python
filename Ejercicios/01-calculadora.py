# n1 = float(input("Ingrese el primer número: "))
# n2 = float(input("Ingrese el segundo número: "))
# print("Seleccione la operación a realizar:")
# print("1. Suma")
# print("2. Resta")
# print("3. Multiplicación")
# print("4. División")
# opcion = input("Ingrese el número de la operación (1/2/3/4): ")

# if opcion == "1":
#     resultado = n1 + n2
#     print(f"El resultado de la suma es: {resultado}")
# elif opcion == "2":
#     resultado = n1 - n2
#     print(f"El resultado de la resta es: {resultado}")
# elif opcion == "3":
#     resultado = n1 * n2
#     print(f"El resultado de la multiplicación es: {resultado}")
# elif opcion == "4":
#     if n2 != 0:
#         resultado = n1 / n2
#         print(f"El resultado de la división es: {resultado}")
#     else:
#         print("Error: No se puede dividir entre cero.")
# else:
#     print("Opción no válida. Por favor, seleccione una operación válida.")

n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
El resultado de la suma es: {suma}
El resultado de la resta es: {resta}
El resultado de la multiplicación es: {multi}
El resultado de la división es: {div}
"""
print(mensaje)
