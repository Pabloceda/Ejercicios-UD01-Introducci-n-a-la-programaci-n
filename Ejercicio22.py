i = 1
contadorPositivos = 0
contadorNegativos = 0
while i <= 100:
    numero = int(input("Ingrese un número entero: "))
    if numero == 0:
        print("El número cero no se considera ni positivo ni negativo, Intente nuevamente.")
    elif numero < 0:
        contadorNegativos += 1
    else:
        contadorPositivos += 1
    i += 1
print("Cantidad de números positivos ingresados:", contadorPositivos)
print("Cantidad de números negativos ingresados:", contadorNegativos)
