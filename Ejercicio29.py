import time

# 1. Mensaje de bienvenida
print("Piensa un número entre 1 y 100, y yo intentaré adivinarlo.")
print("Cuando haga un intento, respóndeme 'mayor', 'menor' o 'igual'.")
time.sleep(2) # Damos tiempo a que el usuario piense

# 2. Inicializar límites
minimo = 1
maximo = 100
respuesta = ""

# 3. Bucle principal del juego
while respuesta != "igual":
    
    # 4. Calcular el intento (Búsqueda binaria)
    # Usamos (minimo + maximo) // 2 para la división entera
    intento = (minimo + maximo) // 2
    
    # 5. Preguntar al usuario
    # .lower() convierte la respuesta a minúsculas para evitar errores
    respuesta = input(f"Mi intento es {intento}. ¿Tu número es 'mayor', 'menor' o 'igual'? ").lower()
    
    # 6. Procesar la respuesta del usuario
    if respuesta == "mayor":
        # Si el número del usuario es MAYOR, mi intento fue muy bajo.
        # Por lo tanto, el nuevo MÍNIMO es mi intento + 1.
        minimo = intento + 1
        
    elif respuesta == "menor":
        # Si el número del usuario es MENOR, mi intento fue muy alto.
        # Por lo tanto, el nuevo MÁXIMO es mi intento - 1.
        maximo = intento - 1
        
    elif respuesta == "igual":
        # Si es IGUAL, hemos terminado.
        print(f"¡Genial! He adivinado tu número. Es el {intento}.")
        
    else:
        # Manejar respuestas no válidas
        print("Error: Por favor, solo responde 'mayor', 'menor' o 'igual'.")

    # (Opcional) Detección de trampas:
    # Si minimo se vuelve más grande que maximo, el usuario ha mentido.
    if minimo > maximo:
        print("Has hecho trampa como el Barcelona. Al carrer!!")
        break

# 7. Fin del juego
print("¡Juego terminado!")