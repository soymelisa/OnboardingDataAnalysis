# Generando estructuras de datos

recorridos = [
    {
        "ORIGEN":"Reforma", 
        "DESTINO": "Tabacalera", 
        "DISTANCIA": 3.5,
        "TIEMPO": "15:00"
    },
    {
        "ORIGEN":"Reforma", 
        "DESTINO": "Juárez", 
        "DISTANCIA": 1.2,
        "TIEMPO": "08:00"
    },
    {
        "ORIGEN":"Alameda", 
        "DESTINO": "Condesa", 
        "DISTANCIA": 5.4,
        "TIEMPO": "20:00"
    }

]

distancia_total = 0
for recorrido in recorridos:
    distancia_total += recorrido["DISTANCIA"]

print("-"*40)
# print("{:10} {:10} {:5} {:5}".format(llaves[0], llaves[1], llaves[2], llaves[3]))
print("{:10} {:10} {:5} {:5}".format(*recorridos[0].keys()))
print("-"*40)

for recorrido in recorridos:
    print("{ORIGEN:10} {DESTINO:10} {DISTANCIA:10} {TIEMPO:10}".format(**recorrido))
print ("-"*40)
print("{:5} {:5} {:10} {:10}".format("",
"", "Distancia total:", distancia_total))

