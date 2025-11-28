n1 = int(input("Intruce el primer número: "))
n2 = int(input("Introduce el segundo número: "))
if n1 > n2:
    print(f"El número mayor es: {n1}")
elif n1 == n2:
    print("Los números son iguales")
else:
    print(f"El número mayor es: {n2}")