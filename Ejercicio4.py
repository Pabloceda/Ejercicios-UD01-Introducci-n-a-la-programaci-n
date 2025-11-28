num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
suma = num1 + num2
resta = num1 - num2
multiplicación = num1 * num2
división = num1 / num2 if num2 != 0 else "Indefinida (no se puede dividir por cero)"
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicación)
print("División:", división)