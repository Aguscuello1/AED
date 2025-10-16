import random
import pickle
import os
import os.path
import io


class Libro:
    def __init__(self, cod, tit, stk):
        self.isbn = cod
        self.titulo = tit
        self.stock = stk


def display(libro):
    print("ISBN: ", libro.isbn, end="")
    print(" - Titulo: ", libro.titulo, end="")
    print(" - Stock: ", libro.stock)


def cargar_arreglo():
    v = []
    titulos = ("F00", "T00", "X00")

    n = int(input("Cuantos libros desea cargar?: "))
    for i in range(n):
        cod = random.randint(1,10000)
        tit = random.choice(titulos) + str(i)
        stk = random.randint(0,100)
        lib = Libro(cod,tit,stk)
        v.append(lib)

    return v

def mostrar_arreglo(v):
    if v is None or len(v) == 0:
        print("No hay datos en el arreglo...")
        print()
        return
    
    print("Los libros registrados son: ")
    for libro in v:
        display(libro)
    print()

def crear_archivo(v,fd):
    if len(v) == 0:
        print("No se han cargado los datos de arreglo...")
        print()
        return
    
    c = int(input("Ingrese la cantidad de stock a comparrar: "))
    m = open(fd, "wb")
    for lib in v:
        if lib.stock > c:
            pickle.dump(lib, m)
    m.close()
    print("Se creo el archivo", fd, "con los registros con stock mayor a ", c)
    print()

def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("El archivo", fd, "no existe...")
        print()
        return
    
    print("Contenido actual del archivo", fd, ":")
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        lib = pickle.load(m)
        display(lib)
    m.close()
    print()


def crear_arreglo(fd):
    if not os.path.exists(fd):
        print("El archivo", fd, "no existe...")
        print()
        return
    
    v = []
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        lib = pickle.load(m)
        if lib.titulo[0] == "F":
            v.append(lib)
    m.close()
    print("Se creo el vector con parte del archivo", fd)
    print()

    return v



def test():
    v1 = []
    v2 = []
    fd = "libros.dat" #nombre del archivo con el que vamos a trabajar
    op = -1

    while op != 7:
        print("Procesamiento combinado de arreglos, registros y archivos...")
        print("1. Crear el arreglo de libros (en forma automatica)")
        print("2. Mostrar el arreglo principal de libros.")
        print("3. Crear archivo con los libros cuyo stock es mayor a c.")
        print("4. Mostrar el archivo de libros.")
        print("5. Crear otro vector con los cuyo titulo comienza con F")
        print("6. Mostrar el segundo arreglo de libros.")
        print("7. Salir")
        op = int(input("Ingresar opcion del menu: "))

        if op == 1:
            v1 = cargar_arreglo()

        elif op == 2:
            mostrar_arreglo(v1)

        elif op == 3:
            crear_archivo(v1,fd)
            
        elif op == 4:
            mostrar_archivo(fd)

        elif op == 5:
            v2 = crear_arreglo(fd)

        elif op == 6:
            mostrar_arreglo(v2)

        elif op == 7:
            print("Saliste del programa...")



if __name__ == "__main__":
    test()

