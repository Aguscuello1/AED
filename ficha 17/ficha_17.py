#ARREGLOS PARALELOS
""" 
def read(nombres, edades, sueldos):
    n = len(nombres)

    for i in range(n):
        nombres[i] = input(f"Nombre[{str(i)}]: ")
        edades[i] = int(input("Edad: "))
        sueldos[i] = int(input("Sueldo: "))


def sort(nombres,edades,sueldos):
    n = len(nombres)
    for i in range(n-1):
        for j in range(i+1, n):
            if nombres[i] > nombres[j]:
                nombres[i], nombres[j] = nombres[j], nombres[i]
                edades[i], edades[j] = edades[j], edades[i]
                sueldos[i], sueldos[j] = sueldos[j], sueldos[i]


def display(nombres, edades, sueldos):
    n = len(nombres)
    print("Personas mmayores de 18 que ganan menos de 10000 pesos: ")
    for i  in range(n):
        if edades[i] > 18 and sueldos[i] < 10000:
            print(f"Nombre: {nombres[i]} - Edad: {edades[i]} - Sueldo: {sueldos[i]}")


def search(nombres, nom):
    n = len(nombres)
    for i in range(n):
        if nom == nombres[i]:
            return i


def validate(inf):
    n = inf
    while n <= inf:
        n =  int(input(f"Cantidad de elementos (mayor a {str(inf)} por favor): "))
        if n <= inf:
            print(f"Error, se pidio cargar un valor mayor a {str(inf)}. Cargue de nuevo!!")
    return n

def test():
    n = validate(0)
    nombres = n * [""]
    edades = n * [0]
    sueldos = n * [0]
    print("\nCargue los datos de las personas: ")
    read(nombres,edades,sueldos)

    nom = input("Nombre a buscar: ")
    ind = search(nombres, nom)
    if ind >= 0:
        print("Encontrado...")
        print(f"Nombre: {nombres[ind]}")
        print(f"Edades: {edades[ind]}")
        print(f"Sueldo: {sueldos[ind]}")
    else:
        print("No existe esa persona encontrda...")




    sort(nombres,edades,sueldos)
    display(nombres,edades,sueldos)


if __name__ == "__main__":
    test() 
"""

#VECTORES DE CONTEO Y DE ACUMULACION...

def test():
    #creamos el vector de conteo...
    n = 100
    c = n * [0]

    #cargamos y contamos los numeros...
    num = int(input("Ingresar un valor entre 0 y 99 (con -1 se corta): "))

    while num != -1:
        if 0>= num <= 99:
            c[num] = c[num] +1
        else:
            print("Error el valor debia ser entre 0 y 99.")

        num = int(input("Ingresar un valor entre 0 y 99 (con -1 se corta): "))


    print("Resultados...")
    for i in range(n):
        if c[i] != 0:
            print(f"Numero {[i]} - Frecuencia de aparicion {c[i]}")
            

if __name__ == "__main__":
    test()

