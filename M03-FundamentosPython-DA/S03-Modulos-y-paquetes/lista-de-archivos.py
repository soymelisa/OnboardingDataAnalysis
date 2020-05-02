import os

# Obteniendo la data (obtener la lista de archivos)
def obtiene_entradas(ruta):
    """" Obtiene la lista de entradas de ruta y regresa una lista con el nombre y tamaño para cada una """
    # Se obtiene el nombre de las entradas 
    nombres = os.listdir(ruta)
    # Obtener el tamaño de cada uno de los elementos que son archivos
    # [
    # ["archivo1", 1234],
    # ["archivo2", 5678],
    # ...
    # ]

    # Agregando ruta a los nombres de archivo
    # for i, n in enumerate(nombres): # [(0, "arch1"), (1, "arch2"), (3,"arch3"),n enumerate(nombres): [(0, "arch1"), (1, "arch2"),
    #   nombres[i] = os.path.join(ruta, n)
    nombres = [os.path.join(ruta,n) for n in nombres] # listas de compresión 

    entradas = []
    for n in nombres:
        if os.path.isfile(n):
            # obtener el tamaño de n-
            # -agregarlo a la lista-
            tamanio = os.path.getsize(n)
            entrada = [n, tamanio]
            entradas.append(entrada)
            print("Archivo:", n)
        else:
            # entonces es una carpeta
            # -asignar 
            # agregarlo a la lista
            entrada = [n, 0]
            entradas.append(entrada)
            
        return entradas

# Imprimiendo resultados
def imprime_entradas(entradas):
    """" Imprime la lista de entrada en la salida estándar en forma tabular """
    for e in entradas:
        print("{:60} {:10}".format(*e))

# uso de las funciones

ruta ="C:/Users/soyme/SandBox2020/OnboardingDataAnalysis/M03-FundamentosPython-DA/S03-Modulos-y-paquetes"
entradas = obtiene_entradas(ruta) 
imprime_entradas(entradas)
