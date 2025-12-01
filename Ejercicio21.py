i = 1               
hayNegativo = False 

print("Introduce 100 números (no pueden ser 0).")

while i <= 100:
    
    try:
        num = int(input(f"Introduce el número {i}: "))

        if num == 0:
            print("Error: El número no puede ser 0. Inténtalo de nuevo.")
        
        else:
            if num < 0:
                hayNegativo = True 
            i = i + 1 
            
    except ValueError:
        print("Error: Debes introducir un número entero.")

if hayNegativo == True: 
    print("Se ha introducido al menos un número negativo.")
else:
    print("No se ha introducido ningún número negativo.")