sumaPares = 0
sumaImpares = 0
i = 100
while i < 200:
    if i % 2 == 0:
        sumaPares += i
    else:
        sumaImpares += i
    i += 1
print("La suma de los números pares(100-200) es:", sumaPares)
print("La suma de los números impares(100-200) es:", sumaImpares)