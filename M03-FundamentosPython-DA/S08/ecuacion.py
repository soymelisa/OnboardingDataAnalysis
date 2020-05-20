import numpy as np

def main():
    """ Función principal del script """
    # ax = b, 3 x 3

    # Matriz de coeficientes
    a = np.array(
        [2, 1, -3],
        [5, -4, 1],
        [1, -1, -4]
    )
    # Vector de resultados
    b = np.array([7, -19, 4])

    # Resolver el sistema de ecuaciones 
    x = np.linalg.solve(a,b)

    print("El vector solución es X")

    # a x -> b
    b1 = np.dot(a, x)
    print("b original:", b)
    print("b calculado:", b1)

    ok = np.allclouse(b, b1)
    if ok:
        print("Resultado correcto")
    else:
        print("No seas zoupe!")

    # Guarda el vector resultado en el archivo soluciones.txt
    nomarch = "solucion.txt"
    np.savetxt(nomarch, x, fmt="%d")
    print(
        "La solución se ha guardado en",
        nomarch
    )

if __name__ == "__main__":
    main() 

