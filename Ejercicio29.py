import time

print("Piensa un número entre 1 y 100, y yo intentaré adivinarlo.")
print("Cuando haga un intento, respóndeme 'mayor', 'menor' o 'igual'.")
time.sleep(2) 

minimo = 1
maximo = 100
respuesta = ""

while respuesta != "igual":
    intento = (minimo + maximo) // 2
    respuesta = input(f"Mi intento es {intento}. ¿Tu número es 'mayor', 'menor' o 'igual'? ").lower()
    
    if respuesta == "mayor":
        minimo = intento + 1
        
    elif respuesta == "menor":
        maximo = intento - 1
        
    elif respuesta == "igual":
        print(f"¡Genial! He adivinado tu número. Es el {intento}.")
        
    else:
        print("Error: Por favor, solo responde 'mayor', 'menor' o 'igual'.")

    if minimo > maximo:
        print("Has hecho trampa como el Barcelona. Al carrer!!")
        break
print("¡Juego terminado!")