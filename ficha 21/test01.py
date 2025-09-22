def validate(inf):
    t = inf
    while t <= inf:
        t = int(input("Ingrese valor (mayor a " + str(inf) + " por favor): "))
        if t <= inf:
            print("Error: se pidio mayor a", inf, "... cargue de nuevo...")
    return t
    
def read(m,n):
    #crear y cargar por teclado una matriz... por filas en orden creciente...
    #m filas n columnas
    cant = [[0] * n for f in range(m)]
    for f in range(m):
        for c in range(n):
            cant[f][c] = int(input("Valor [" + str(f) + "][" + str(c) + "]: "))
    return cant

def totales_por_vendedor(cant):
    m,n = len(cant),len(cant[0])
    print()
    print("Cantidades vendidas por cada vendedor")
    for f in range(m):
        ac = 0
        for c in range(n):
            ac += cant[f][c]
        print("Vendedor", f, "\t - Cantidad total vendidas: ", ac)

def totales_por_articulo(cant):
    #totalizacion por columnas...
    m,n = len(cant),len(cant[0])
    print()
    print("Cantidades vendidas por cada articulo")
    for c in range(n):
        ac = 0
        for f in range(m):
            ac += cant[f][c]
        print("Articulo", c, "\t - Cantidad total vendidas: ", ac)



def test():
    print("Cantidad de vendedores: ")
    m = validate(0)

    print("Cantidad de articulos: ")
    n = validate(0)

    print("Carge las cantidades de articulos por vendedor: ")
    cant = read(m,n)

    totales_por_vendedor(cant)
    totales_por_articulo(cant)


if __name__ == "__main__":
    test()