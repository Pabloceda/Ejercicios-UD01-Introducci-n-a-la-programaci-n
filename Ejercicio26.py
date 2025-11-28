nombre = input("Introduce nombre del trabajador: ")
horas_trabajadas = float(input("Introduce las horas trabajadas: "))
tarifa_hora = float(input("Introduce la tarifa por hora: "))
tarifa_plus = tarifa_hora * 1.5
HorasExtras = horas_trabajadas - 35
if horas_trabajadas <= 35:
    salario_bruto = horas_trabajadas * tarifa_hora
else:
    salario_bruto = (35 * tarifa_hora) + (HorasExtras * tarifa_plus)

if salario_bruto <= 500:
    impuestos = 0
elif salario_bruto <= 900:
    impuestos = (salario_bruto - 500) * 0.25
else:
    impuestos = (400 * 0.25) + ((salario_bruto - 900) * 0.45)
salario_neto = salario_bruto - impuestos
print(f"Trabajador: {nombre}")
print(f"Salario bruto: {salario_bruto} euros")
print(f"Impuestos a pagar: {impuestos} euros")
print(f"Salario neto: {salario_neto} euros")
