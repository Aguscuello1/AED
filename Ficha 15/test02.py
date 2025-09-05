import arreglos

def validate(inf):
    n = inf
    while n <= inf:
        n = int(input(f"Ingrese cantidad de elementos (mayor a {str(inf)} por favor): "))
        if n <= inf:
            print((f"Error se pide mayor a {inf} ...cargue de nuevo..."))

    return n

def test():

    #cargar cantidad de elementos...
    n = validate(0)

    #crear un arreglo de n elementos (valor inicial 0)...
    v = n * [0]

    #cargar el arreglo por teclado...
    arreglos.read(v)

    #cargar el numero k por el cual se multiplicara al vector...
    k = int(input("Ingresar el valor de k: "))

    #multiplar el vector por k...
    arreglos.product(v,k)

    #mostrar el vector final...
    print(f"El vector final quedo asi: {v}")


if __name__ == "__main__":
    test()



