import os
import time

# Módelo 
### Segmentar con el principio MVC
def obtiene_entradas(ruta):
    """" Obtiene la lista de entradas de ruta y regresa una lista con el nombre y tamaño para cada una """
    # Se obtiene el nombre de las entradas 
    nombres = os.listdir(ruta)
    fecha = os.listdir(ruta)
    # Obtener el tamaño de cada uno de los elementos que son archivos
    # [
    # ["archivo1", 1234],
    # ["archivo2", 5678],
    # ...
    # ]

    # Agregando ruta a los nombres de archivo
    # for i, n in enumerate(nombres): # [(0, "arch1"), (1, "arch2"), (3,"arch3"),n enumerate(nombres): [(0, "arch1"), (1, "arch2"),
    #   nombres[i] = os.path.join(ruta, n)

    nombres = [os.path.join(ruta, n) for n in nombres] # listas 
    entradas = []
    total= 0
    for n in nombres:
        fecha = os.path.getatime(n) # segundos 
        fecha = time.ctime(fecha)
        # str 

        if os.path.isfile(n):
            # obtener el tamaño de n-
            # -agregarlo a la lista-
            tamanio = os.path.getsize(n)
            entrada = [n, tamanio, fecha]
            entradas.append(entrada)
            total += tamanio # total = total + tamanio
        else:
            # entonces es una carpeta
            # -asignar 
            # agregarlo a la lista
            entrada = [n, 0, fecha]
            entradas.append(entrada)
            # total += 0 # si es 0, no tiene caso
            
    return entradas, total # sub, iva, fechas

# Vista: Genera resultado para el usuario
def imprime_entradas(entradas, total):
    """" Imprime la lista de entrada en la salida estándar en forma tabular """
    for e in entradas:
        print("{:60} {:10} {:24}".format(*e))
    print("Total de bytes: {} bytes".format(total))

# Controlador:
# Manipula las funciones del modelo y la vista 
def main():
    """ Función principal del script """
    ruta ="C:/Users/soyme/SandBox2020/OnboardingDataAnalysis/M03-FundamentosPython-DA/S03-Modulos-y-paquetes"
    entradas = obtiene_entradas(ruta) 
    # obtiene_e al final es un dato por lo que 
    imprime_entradas(entradas, total)
    
# las variables con __ son variables internas y NO se deberían de tocar, solo utilizar
if __name__ == "__main__": # el script es el programa principal? 
    main()