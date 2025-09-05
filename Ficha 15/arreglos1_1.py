def validar_tamaño():

    n = int(input("Ingresar tamaño del vector: "))
    while n <= 0:
        n = int(print("El tamaño del vector tiene que ser positivo, ingrese otro..."))
    return n

def crear(tam):
    v = []
    for i in range(tam):
        dato = int(input(f"Ingrese v[{str(i)}]: "))
        v.append(dato)
    return v

def contar_repeticiones(v):
    repeticiones = 0
    for elemento in v:
        if elemento == v[-1]:
            repeticiones +=1
    return repeticiones

def buscar_menores(v):
    menores = []
    for elemento in v:
        if elemento < v[0]:
            menores.append(elemento)
    return menores


        
