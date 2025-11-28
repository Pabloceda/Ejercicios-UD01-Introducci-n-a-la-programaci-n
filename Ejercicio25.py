calificacion = float(input("Introduce la calificación (0-10): "))
if calificacion >= 0 and calificacion < 3:
    print("Muy deficiente")
elif calificacion >= 3 and calificacion < 5:
    print("Insuficiente")
elif calificacion >= 5 and calificacion < 6:
    print("Suficiente")
elif calificacion >= 6 and calificacion < 7:
    print("Bien")
elif calificacion >= 7 and calificacion < 9:
    print("Notable")
elif calificacion >= 9 and calificacion <= 10:
    print("Sobresaliente")
else:
    print("Calificación no válida. Por favor, introduce un número entre 0 y 10.")
3