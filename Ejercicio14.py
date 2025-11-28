numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
r_suma = numero1 + numero2
r_resta = numero1 - numero2
r_multiplicacion = numero1 * numero2
r_division = numero1 / numero2 if numero2 != 0 else "Indefinida (división por cero)"
print(f"Suma: {r_suma}")
print(f"Resta: {r_resta}")
print(f"Multiplicación: {r_multiplicacion}")
print(f"División: {r_division}")