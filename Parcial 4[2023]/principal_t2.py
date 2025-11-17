import os.path
import random
import clase_t2
import pickle

#funciones
def menu():
    print("MENU")
    print("1. Cargar arreglo")
    print("2. Mostrar arreglo")
    print("3. Buscar y mostrar")
    print("4. Generar archivo binario")
    print("5. Mostrar archivo")
    print("6. Salir")

def validar(inf):
    n = int(input("Ingresar cantidad de libros: "))
    while n <= inf:
        n = int(input("Error! Se pidio crear una arreglo mayor a " + str(inf) + "...Cargue de nuevo: "))
    return n


def add_in_order(v, libro):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if libro.isbn == v[c].isbn:
            pos = c
            break

        else:
            if libro.isbn < v[c].isbn:
                der = c - 1
            else:
                izq = c + 1

    if izq > der:
        pos = izq
    v[pos:pos] = [libro]


def cargar_arreglo():
    n = validar(0)
    v = []

    tit1 = ("Guerra", "Espacio", "Abismo", "Fanatismo")
    tit2 = ("Oscuridad", "Tristeza", "Felicidad", "Honor")
    nombres = ("Carlos", "Ana", "José", "María", "Pedro", "Belén", "Martín", "Soledad")
    apellidos = ("Díaz", "Giuliani", "Trejo", "Masiero", "Duplesis", "Johnson", "Iriarte")

    for i in range(n):
        isbn = random.randint(1, 100000000)
        tit = random.choice(tit1) + " y " + random.choice(tit2) + " " + str(i)
        aut = random.choice(nombres) + " " + random.choice(apellidos) + " " + random.choice(apellidos)
        cod = random.randint(1, 5)
        pre = round(random.uniform(1000, 10000), 2)
        libro = clase_t2.Libro(isbn, tit, aut, cod, pre)
        add_in_order(v, libro)

    print("Listo, el arreglo fue generado...")
    print()
    return v


def mostrar(v):
    n = len(v)
    print("Listado de libros...")
    for i in range(n):
        print(v[i])
    print()

def binaria(v, isb):
    n = len(v)
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if isb == v[c].isbn:
            return c
        
        if isb < v[c].isbn:
            der = c - 1
        else:
            izq = c + 1

    return -1

def buscar(v):
    isb = int(input("ISBN a buscar: "))
    pos = binaria(v, isb)
    if pos != -1:
        print("Encontrado!")
        print(v[pos])
        if v[pos].cod_idioma == 4:
            d = (22 * v[pos.precio]) // 100
            v[pos].precio -= d
            print("Datos cambiados: ")
            print(v[pos].precio)
    else:
        print("No contamos cone el libro", isb, "pero vuelva, pleaseeee!")
    print()



def grabar(v, fd):
    m = open(fd, "wb")
    a = int(input("Buscar autor..."))
    p = float(input("Buscar por precio..."))

    for i in range(len(v)):
        if v[i].autor == a and v[i].precio <= p:
            pickle.dump(v[i], m)

    m.close()
    print("Ya se ha creado el archivo...")
    print()


def mostrar_archivo(fd):
    c = 0
    t = os.path.getsize
    m = open(fd, "rb")

    while m.tell() < t:
        r = pickle.load(m)
        c += 1
        print(r)
    m.close()

    print("Cantidad de libros que contamos: ", c)
    print()


#funcion principal
def principal():
    v = []
    fd = "datos.dat"
    op = -1
    while op != 6:
        menu()
        op = int(input("Ingresar opcion del menu: "))

        if op == 1:
            v = cargar_arreglo()

        elif op == 2:
            if v:
                mostrar(v)
            else:
                print("El arreglo no se ha cargado...")

        elif op == 3:
            if v:
                buscar(v)
            else:
                print("El arreglo no se ha cargado...")

        elif op == 4:
            if v:
                grabar(v, fd)
            else:
                print("El arreglo no se ha cargado...")

        elif op == 5:
            if os.path.exists:
                mostrar_archivo(fd)
            else:
                print("No existe el archivo...")

        elif op == 6:
            print("Saliste del programa...")
    
#ejecucion de la funcion principal
if __name__ == "__main__":
    principal()

