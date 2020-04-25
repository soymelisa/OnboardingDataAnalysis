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

#Imprimimos tabla (vista)
print("-"*40)
for recorrido in recorridos:
    print("{ORIGEN:10} {DESTINO:10} {DISTANCIA:10} {TIEMPO:10}".format(**recorrido))
print ("-"*43)

