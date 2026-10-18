# En este ejercicio se va a crear una calculadora que pueda realizar operaciones básicas como suma, resta, multiplicación y división.
# verifica ssi ya ingresamos un numero antes, indicar que ingrese uno en caso contrario
# ingrese una operaciom, ingrese el segundo numero, y luego mostrar el resultado de la operacion seleccionado,
# el resultado se convierte en el primer numero, y se repite el proceso hasta que el usuario decida salir de la calculadora.

print("Bienvenido a la calculadora")
numero1 = None

while True:
    if numero1 is None:
        numero1 = float(input("Ingrese un número: "))
    else:
        print(f"El número actual es: {numero1}")

    operacion = input(
        "Ingrese una operación (+, -, *, /) o 'salir' para terminar: ")

    if operacion.lower() == "salir":
        print("Saliendo de la calculadora...")
        break

    numero2 = float(input("Ingrese otro número: "))

    if operacion == "+":
        resultado = numero1 + numero2
    elif operacion == "-":
        resultado = numero1 - numero2
    elif operacion == "*":
        resultado = numero1 * numero2
    elif operacion == "/":
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            print("Error: División por cero no permitida.")
            continue
    else:
        print("Operación no válida. Intente de nuevo.")
        continue

    print(f"Resultado: {resultado}")
    # El resultado se convierte en el primer número para la siguiente operación.
    numero1 = resultado

# En este ejemplo, se utiliza un bucle while para crear una calculadora que permite al usuario realizar operaciones básicas.
# El bucle continuará ejecutándose hasta que el usuario ingrese la palabra "salir".
# Dentro del bucle, se solicita al usuario que ingrese un número, una operación y otro número.
# Luego, se realiza la operación seleccionada y se muestra el resultado.
