#imports
import os.path
import random
import clase_t1
import pickle

#funciones
def menu():
    print("1. Cargar el arreglo")
    print("2. Mostrar el contenido")
    print("3. Acumular y mostar")
    print("4. Generar un archivo")
    print("5. Mostrar el archivo generado")
    print("6. Salir")

def validar(inf):
    n = int(input(f"Ingrese la cantidad de lotes(mayores a {str(inf)}) "))
    while n <= inf:
        n = int(input(f"Error se pidio un numero mayor a {str(inf)}, cargue de nuevo...."))

    return n

def add_in_order(v, lote):
    n = len(v)
    pos = n

    izq ,der = 0, n-1

    while izq <= der:
        c = (izq + der) // 2
        if v[c].nombre == lote.nombre:
            pos = c
            break

        if lote.nombre < v[c].nombre:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [lote]
         
def cargar():
    n = validar(0)
    v = []

    nombres = ("Carlos", "Ana", "José", "María", "Pedro", "Belén", "Martín", "Soledad")
    apellidos = ("Díaz", "Giuliani", "Trejo", "Masiero", "Duplesis", "Johnson", "Iriarte")

    for i in range(n):
        nom  = random.choice(nombres) + random.choice(apellidos)
        man = random.randint(1, 35)
        lot = random.randint(1, 20)
        ori = random.randint(1,4)
        sup = round(random.uniform(200, 4000), 2)
        imp = round(random.uniform(10000, 200000), 2)
        lote = clase_t1.Lote(nom, man, lot, ori, sup, imp)
        add_in_order(v, lote)

    print("Listo, el arreglo fue ordenado...")
    print()

    return v

def mostrar(v):
    n = len(v)
    print("Listado de lotes...")
    for i in range(n):
        print(v[i])
    print()

def contar(v):
    n = len(v)

    ac = [[0] * 4 for f in range(35)]

    for i in range(n):
        f = v[i].manzana - 1
        c = v[i].orientacion - 1 
        ac[f][c] += v[i].superficie

    print("Resultados...")
    for f in range(35):
        for c in range(4):
            if ac[f][c] != 0:
                print("Manzana:", f+1, "Orientacion: ", c+1, "Superficie: ", ac[f][c])
    print()

    m = int(input("Manzana que desea acumular (entre 1y 35)?: "))
    sa = 0
    f = m - 1
    for c in range(4):
        sa += ac[f][c]
    print("La superficie total para la manzana", m, "es: ", sa)


def generar_archivo(v, fd):
    l1 = int(input("Valor de l1: "))
    l2 = int(input("Valor de l2: "))

    n = len(v)
    m = open(fd, "wb")
    for i in range(n):
        if l1 <=v[i].lote <= l2:
            pickle.dump(v[i], m)
    m.close()
    print("Archivo generado...")
    print()

def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("No existe el archivo ", fd, "...")
        print()
        return
    
    print("Listado de lotes...")
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    c = 0

    while m.tell < t:
        r = pickle.load(m)
        c += 1
        ac = r.importe
        print(r)
    m.close()

    p = 0
    if c != 0:
        p = ac / c
    print("Importe promedio de venta: ", round(p,2))
    print()
    

#funcion princial
def main():
    v = []
    fd = "lotes.dat"
    op = -1
    while op != 6:
        menu()
        op = int(input("Ingresar opcion del menu: "))

        if op == 1:
            v = cargar()

        elif op == 2:
            if v:
                mostrar(v)
            else:
                print("El arreglo no fue cargado...")
            
        elif op == 3:
            if v:
                contar(v)
            else:
                print("El arreglo no fue cargado...")
        elif op == 4:
            generar_archivo(v, fd)
        elif op == 5:
            mostrar_archivo(fd)
        elif op == 6:
            print("Saliste del programa.")


#ejecucion de la funcion principal
if __name__ == "__main__":
    main()


