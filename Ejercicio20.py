num = int(input("Introduce un número: "))
f = 1
i = 1
while i <= num:
    f = f * i
    i = i + 1
else:
    print(f"El factorial de {num} es: {f}")