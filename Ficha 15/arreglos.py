
def read(v):
    #carga por teclado de un vector de n componentes...
    n = len(v)
    print(f"Carge los elementos del vector: ")
    for i in range(n):
        v[i] = int(input(f"casillas [{str(i)}]: "))




def add(a,b):
    pass

def product(v, k):
    #multiplicar por k el arreglo y lo retorna...
    n = len(v)
    for i in range(n):
        v[i] *= k


def scalar_product(a, b):
    pass
