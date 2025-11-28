hayDiez = False
nota = float(input("Introduce una nota entre 0 y 10(-1 para salir del programa): "))
while nota != -1:
    if nota == 10:
        hayDiez = True
    nota = float(input("Introduce otra nota entre 0 y 10(-1 para salir del programa): "))
if hayDiez == False:
    print("No se ha introducido ninguna nota igual a 10")
else:
    print("Se ha introducido al menos una nota igual a 10")
