#BUSQUEDA DE PRIMOS...

import arreglo_3_2
from funciones_3_1 import validar_mayor_a_cero

def principal():
    print("Manejo de arreglos")
    print("==========================")

    tam = validar_mayor_a_cero("Ingrese el tamaño del vector: ")
    vector  = arreglo_3_2.crear(tam)

    print()
    print(f"Vector original: ")
    print(arreglo_3_2.mostrar(vector))

    primos = arreglo_3_2.generar_vector_primos(vector)
    print()
    print("Vector con los numeros primos contenidos en el original: ")
    print(arreglo_3_2.mostrar(primos))


    prom = arreglo_3_2.promedio(primos)
    print()
    print(f"El promedio de los numeros primos es: {prom}")


if __name__ == "__main__":
    principal()    



