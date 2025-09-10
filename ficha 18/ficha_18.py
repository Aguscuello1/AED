#CASOS DE ANALISIS

"""
Desarrollar un programa con menu de opciones que permita:
1. Cargar un arreglo con las alturas de n personas.
2. Mostrar el arreglo.
3. Determinar la altura media del grupo, e unformar cuantas alturas son mayores
a la media, y cuantas son menores o iguales.
4. Buscar el arreglo una altura igual a x e informar si esta o no.
5. Ordenar de menor a mayor.
"""
""" 
def validate(inf):
    n = inf
    while n < inf:
        n = int(input(f"Ingrese cantidad de elementos (mayor a {str(inf)} por favor:) "))
        if n <= inf:
            print("Error, se pidio un valor mayor a {inf}...cargue de nuevo...")
    return n

def read(alt):
    n = len(alt)
    print("Cargue las alturas (en centimetros) del grupo: ")
    for i in range(n):
        alt[i] = int(input(f"Altura [{str(i)}]: "))

def average(alt):
    n, s = len(alt), 0
    for i in range(n):
        s += alt[i]
    return s/n

def count(alt,med):
    n = len(alt)
    c1 = c2 = 0
    for i in range(n):
        if alt[i] > med:
            c1 +=1
        else:
            c2 +=1

    return c1,c2

def search(alturas,x):
    n = len(alturas)
    for i in range(n):
        if x == alturas[i]:
            return i
    return -1

def sort(alturas):
    n = len(alturas)
    for i in range(n-1):
        for j in range(i +1):
            if alturas[i] > alturas[j]:
                alturas[i], alturas[j] = alturas[j], alturas[i]



def test():
    #creamos un arreglo vacio...
    alturas = []

    #menu de opciones...
    op = -1
    while op != 6:
        #mostramos el menu...
        print("1. Cargar un arreglo con las alturas de n personas: ")
        print("2. Mostrar el arreglo: ")
        print("3. Determinar la altura media del grupo, e unformar cuantas alturas son mayores a la media, y cuantas son menores o iguales: ")
        print("4. Buscar el arreglo una altura igual a x e informar si esta o no: ")
        print("5. Ordenar de menor a mayor: ")
        print("6. Terminar y salir.")
        op = int(input("Ingrese el numero de la opcion elegida: "))
        print()

        if op == 1:
            #cargar por teclado el arreglo...
            n = validate(0)
            alturas = n * [0]
            read(alturas)
            print()

        elif op == 2:
            #controlar si el arreglo fue cargado...
            if len(alturas) != 0:
                print(f"Las alturas cargadas son: {alturas}")
            else:
                print("No hay datos cargados...")
            print()

        elif op == 3:
            #controlar si el arreglo fue cargado...
            if len(alturas) != 0:
                media = average(alturas)
                mayores, menores = count(alturas, media)
                print(f"La altura media del grupo es: {media}")
                print(f"Alturas mayores a la media: {mayores}")
                print(f"Alturas menores a la media: {menores}")
                print()

            else:
                print("No hay datos cargados...")
            print()

        elif op == 4:
            #controlar si el arreglo fue cargado...
            if len(alturas) != 0:
                #cargamos y bucamos una altura...
                x = int(input("Altura a buscar: "))
                pos = search(alturas,x)
                if pos >= 0:
                    print(f"Esta en la casilla {pos}")
                else:
                    print("Noesta en el arreglo.")

            else:
                print("No hay datos cargados...")
            print()

        elif op == 5:
            #controlar si el arreglo fue cargado...
            if len(alturas) != 0:
                sort(alturas)
                print("Hecho. El arreglo fue ordenado de menor a mayor")
            else:
                print("No hay datos cargados...")
            print()



if __name__ == "__main__":
    test() 
"""


v1 = [3,6,8,5]
v2 = [1,3,5,9,2]

def generate(v1,v2):
    v3 = []
    for i in range(len(v1)):
        for j in range(len(v2)):
            if v1[i] == v2[j]:
                v3.apppend(v1[i])
                break
    return v3

