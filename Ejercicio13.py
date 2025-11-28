numero = int(input("Introduce un número: "))
if numero < 1:
    print("El número debe ser mayor o igual a 1.")
else:
    print(f"Mostrando números del 1 al {numero}:")
    i = 1
    while i <= numero:
        print(i)
        i += 1
