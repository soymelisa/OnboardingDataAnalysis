# Lee el valor de número de claves n

esCorrecto = False
while not esCorrecto:
    n = input("Ingresa un entero: ")
    esCorrecto = n.isdigit()
    if not esCorrecto:
        print("El valor ", n, " no es un entero, por favor ingresa un entero.")
    else: 
        n = int(n)
        
print(n, type(n))