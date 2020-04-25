#### Importación de módulos
import random

esCorrecto = False
while not esCorrecto:
    n = input("Ingresa un entero: ")
    esCorrecto = n.isdigit()
    if not esCorrecto:
        print("El valor ", n, " no es un entero, por favor ingresa un entero.")
    else: 
        n = int(n)

# Lee el valor de número de claves n
m = 8
esCorrecto = False
while not esCorrecto:
    r = input("Ingresalongitud de clave(8): ")
    esCorrecto = r.isdigit() or r == ""
    if not esCorrecto:
        print("El valor ", m, " no es un entero, por favor ingresa un entero.")
    else: 
        if r.isdigit():
            m = int(r)
        
print(n, type(n))
print(m, type(m))


# Generando clave (primero 1)
# Incluir mayúsculas

mayusculas = "ABCCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = mayusculas.lower()
digitos = "1234567890"
simbolos = "¡?=)(/&%$#_:[*¨?" # string.punctuation()

alfabeto = mayusculas + minusculas + digitos + simbolos

# from string import punctuation, ascii_letters, digits

for x in range(n):
    clave = random.choice(mayusculas)
    clave += random.choice(minusculas)
    clave += random.choice(digitos)
    clave += random.choice(simbolos)

    nl= m - 4
    faltan = random.choices(alfabeto, k=nl)

    faltan = "".join(faltan)  
    clave += faltan 
    # regresamos o convertimos listas a str para obtener la clave concatenada
    clave = "".join(random.sample(clave, m)) 
    print(clave)

