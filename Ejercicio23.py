contadorNegativo = 0
contadorPositivo = 0
hayNegativo = False
try:
    numero = int(input("Ingrese un número entero (ingrese 0 para finalizar): "))
    while numero != 0:
        if numero < 0:
            hayNegativo = True
            contadorNegativo += 1
        else:
            contadorPositivo += 1
        numero = int(input("Ingrese otro número (0 para finalizar): "))
    if hayNegativo == True:
        print("Sí se han encontrado números negativos.")
    else:
        print("No se han encontrado números negativos.")  
    print(f"Total de números positivos: {contadorPositivo}")
    print(f"Total de números negativos: {contadorNegativo}")
except ValueError:
    print("Error: Debe ingresar un número entero.")