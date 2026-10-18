# and, or, not

# x > 5 and x < 10 basta con que los dos sean verdaderos

# x > 5 or x < 10 basta con que uno de los dos sea verdadero

# not x > 5 es lo contrario de x > 5, es decir, x <= 5 niega la condición

gas = False
encendido = True
edad = 18

# if not gas and (encendido and edad > 17):
#     print("El coche puede arrancar")


# operadores de corto circuito

if not gas or encendido or edad > 17:
    print("El coche puede arrancar")
