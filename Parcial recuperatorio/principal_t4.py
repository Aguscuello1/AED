import random
from clase_t4 import * 
import pickle
import os

def menu():
    print("====MENU====")
    print("1. Cargar arreglo")
    print("2. Mostrar arreglo")
    print("3. Buscar por codigo")
    print("4. Generar archivo binario")
    print("5. Mostrar archivo binario")
    print("6. Procesar cadena de texto")
    print("7. Salir")


#punto 1...
def validar(inf):
    n = int(input("Ingresar cantidad de cursos: "))
    while n <= inf:
        n = int(input("Tiene que ser mayor a ", str(inf), " Porfavor, ingresar cantidad: "))
    return n

def add_in_order(v,cursos):
    n = len(v)
    pos = n
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2
        if cursos.id == v[c].id:
            pos = c
            break

        if cursos.id > v[c].id:
            izq = c + 1
        else:
            der = c - 1
        
    if izq > der:
        pos = izq
    v[pos:pos] = [cursos]


def cargar_arreglo(v):
    n = validar(0)
    nombres = (
        "Hola mundo azul y amable.", "Ahora los quiero ver.",
        "Viva Talleres que por fin zafó.", "En este momento aciago."
    )
    for i in range(n):
        id = random.randint(1,10)
        cod_tematica = random.randint(100,500)
        nombre = random.choice(nombres)
        costo = random.randint(1000,10000)
        cursos = Curso(id,cod_tematica,nombre,costo)
        add_in_order(v,cursos)
    return v

def mostrar_arreglo(v):
    #mostrar uno por linea
    #procentaje que representan los cursos t sobre el total de cursos
    n = len(v)
    porc = 0
    t = int(input("Tematica a controlar: "))
    ct = 0

    for i in range(n):
        print(v[i])
        if v[i].cod_tematica == t:
            ct +=1

    porc = round((ct * 100) / n, 2)
    print("Porcentaje que representan los cursos de la tematica ", t, "sobre el total de los cursos ofrecidos: ", porc)


def buscar(v):
    x = int(input("Codigo a buscar: "))
    n = len(v)
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2
        if x == v[c].id:
            print("Encontrado...")
            print(v[c])
            print()
            return v[c].nombre
        
        if x > v[c].id:
            izq = c + 1
        else:
            der = c - 1
    r = "No existe ese curso."
    print(r)
    return r


def generar_archivo_binario(fd,v):
    n = len(v)
    m = open(fd,"wb")
    p = int(input("Filtrar por monto: "))

    for cursos in range(n):
        if v[cursos].costo > p:
            pickle.dump(cursos,m)
    m.close()
    print("Archivo binario generado...")


def mostrar_archivo_binario(fd):
    m = open(fd,"rb")
    t = os.path.getsize(fd)
    ctr = 0

    while m.tell() < t:
        cur = pickle.load(m)
        print(cur)
        ctr += 1
    m.close()
    print("Cantidad de registros que se mostraron: ", ctr)

def procesar_cadena(cad):
    cl = may = 0
    ecb = False

    for car in cad:
        if car in " .":
            if ecb and cl > may:
                may = cl
            ecb = False
            cl = 0

        else:
            cl += 1
            if cl == 1 and car in "aeiouAEIOU":
                ecb = True
    print("Texto procesado: ", cad)
    print("La longitud de la palabra mas larga es de: ", may)


def principal():
    v = []
    op = -1
    fd = "archivo.dat"
    cad = None

    while op != 7:
        menu()
        op = int(input("Ingresar opcion del menu: "))

        if op == 1:
            cargar_arreglo(v)
        elif op == 2:
            if v:
                mostrar_arreglo(v)
            else:
                print("No se ha cargado el arreglo...")
        elif op == 3:
            if v:
                buscar(v)
            else:
                print("No se ha cargado el arreglo...")
        elif op == 4:
            if v:
                generar_archivo_binario(fd,v)
            else:
                print("No se ha cargado el arreglo...")
        elif op == 5:
            if os.path.exists(fd):
                mostrar_archivo_binario(fd)
            else:
                print("No se ha creado el archivo ", fd)
        elif op == 6:
            if cad is not None:
                procesar_cadena(cad)
            else:
                print("La cadena no existe (entre en la opcion 3...)")
        elif op == 7:
            print("Saliste del programa...")

if __name__ == "__main__":
    principal()
