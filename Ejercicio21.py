# 1. Inicializamos las variables
i = 1               # Este es el contador de números leídos
hayNegativo = False # Esta es nuestra "bandera"

print("Introduce 100 números (no pueden ser 0).")

# 2. Bucle 'while' para leer 100 números
while i <= 100:
    
    try:
        num = int(input(f"Introduce el número {i}: "))

        # 3. Comprobar si es nulo (0)
        if num == 0:
            # Si es 0, mostramos error y NO incrementamos 'i'
            # El bucle 'while' se repetirá pidiendo el número {i} otra vez
            print("Error: El número no puede ser 0. Inténtalo de nuevo.")
        
        else:
            # 4. Es un número válido (no es 0)
            
            # Comprobamos si es negativo
            if num < 0:
                hayNegativo = True # Activamos la bandera
            
            # 5. Incrementamos el contador SOLO si el número fue válido
            i = i + 1 
            
    except ValueError:
        print("Error: Debes introducir un número entero.")

# 6. Fuera del bucle (después de leer los 100 números), mostramos el resultado
if hayNegativo == True: # También puedes poner "if hayNegativo:"
    print("Se ha introducido al menos un número negativo.")
else:
    print("No se ha introducido ningún número negativo.")