cantidad_euros = int(input("Ingrese la cantidad de euros multiplo de 5: "))
restante = cantidad_euros
while restante % 5 != 0 or restante < 0:
    print("Error: La cantidad debe ser un múltiplo de 5 y no negativa.")
    cantidad_euros = int(input("Ingrese la cantidad de euros multiplo de 5: "))
    restante = cantidad_euros
billetes_500 = restante // 500
restante = restante % 500
billetes_200 = restante // 200
restante = restante % 200
billetes_100 = restante // 100
restante = restante % 100
billetes_50 = restante // 50
restante = restante % 50
billetes_20 = restante // 20
restante = restante % 20
billetes_10 = restante // 10
restante = restante % 10
billetes_5 = restante // 5
restante = restante % 5
print("Desglose en billetes:")
print("Billetes de 500€:", billetes_500)
print("Billetes de 200€:", billetes_200)
print("Billetes de 100€:", billetes_100)
print("Billetes de 50€:", billetes_50)
print("Billetes de 20€:", billetes_20)
print("Billetes de 10€:", billetes_10)
print("Billetes de 5€:", billetes_5)