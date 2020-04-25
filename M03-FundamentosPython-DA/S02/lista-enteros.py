n = 5000000

# Creamos lista de enteros
numeros = list(range(n))

# convertir lista a decimalesa float toda la lista
for i in range(n):
    numeros[i] = float(numeros[i])

for n in numeros: 
    print(n)