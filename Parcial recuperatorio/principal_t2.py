#imports...
from clase_t2 import *
import random
import os
import pickle


#funciones...
def menu():
    print("=====MENU=====")
    print("1. Cargar arreglo")
    print("2. Mostrar arreglo")
    print("3. Contar cantidad de alumnos")
    print("4. Generar archivo binario")
    print("5. Mostrar archivo")
    print("6. Procesar cadena")
    print("7. Salir")

#punto 1...
def validar(inf):
    n = int(input("Ingresar cantidad de alumnos: "))
    while n <= inf:
        n = int(input("Ingresar cantidad de alumnos mayoresa a ", str(inf), ": "))
    return n

def add_in_order(v,alumnos):
    n = len(v)
    pos = n
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der) // 2
        if alumnos.legajo == v[c].legajo:
            pos = c
            break

        if alumnos.legajo > v[c].legajo:
            izq = c + 1
        else:
            der = c - 1

    if izq > der:
        pos = izq
    v[pos:pos] = [alumnos]


def cargar_arreglo(v):
    n = validar(0)
    nombres = ("Alejandro", "Luis", "Ana", "Leonardo", "Verónica", "Soledad", "Juan")
    apellidos = ("Suárez", "Chiesa", "Brown", "Contreras", "Fenoglio")
    observaciones_cadena = (
        "Es excelente alumno.", "Parece que recursa.", "Estudiante inquieto.",
        "Puede empezar igual.", "Antes era mejor.",
    )

    for i in range(n):
        legajo = random.randint(1,10)
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        curso = random.randint(1,20)
        nota_final = random.randint(6,10)
        observaciones = random.choice(observaciones_cadena)
        alumnos = Alumno(legajo, nombre,apellido,curso,nota_final,observaciones)
        add_in_order(v,alumnos)
    return v


#punto 2...
def mostrar_arreglo(v):
    n = len(v)
    l = int(input("Legajo a controlar: "))
    ct = 0

    for alumnos in range(n):
        print(v[alumnos])
        if v[alumnos].legajo < l:
            ct += 1
    
    p = round((ct * 100) /n, 2)
    print("Porcentaje pedido: ", p)
    print()


#punto 3...
def contar(v):
    filas = 5
    columnas = 20

    mat = [[0] * columnas for i in range(filas)]
    for alumno in v:
        f = alumno.nota - 6
        c = alumno.curso - 1
        mat[f][c] +=1

    print("Conteo por nota y curso: ")
    for f in range(filas):
        for c in range(columnas):
            if mat[f][c] != 0:
                print("Nota:", f+6, " - Curso:", c+1, " - Cantidad:", mat[f][c])
    print()


#punto 4...
def generar_archivo_binario(fd, v):
    ac = 0
    for alu in v:
        ac += alu.nota
    p = round(ac/len(v), 2)

    c = int(input("Curso para filtrar: "))
    m = open(fd, "wb")
    for alu in v:
        if alu.nota > p and alu.curso == c:
            pickle.dump(alu, m)
    m.close()
    print("Archivo creado...")
    print()

#punto 5...
def mostrar_archivo(fd):
    m = open(fd,"rb")
    t = os.path.getsize(fd)

    print("Contenido del archivo de alumnos: ")
    while m.tell() < t:
        cur = pickle.load(m)
        print(cur)
    m.close()
    print()



#punto 6...
def procesar_texto(v):
    primero = v[0]
    texto = primero.observaciones
    sca = ss = False
    cl = cpok = 0

    for car in texto:
        if car in " .":
            if sca and not ss:
                cpok +=1

            cl = 0
            sca = ss = False
        else:
            cl +=1
            if cl == 1 and car.lower() in "eèiìoòuù":
                sca = True
            
            if car.lower() == "s":
                ss = True
    
    print("Texto procesado: ", texto)
    print("Cantidad de palabras que comienzan con una vocal distinta de [aA] y no tiene [s]: ", cpok)
    print()


#funcion principal...
def principal():
    v = []
    op = -1
    fd = "archivo.dat"

    while op != 7:
        menu()
        op = int(input("Ingresar opcion del menu: "))

        if op == 1:
            cargar_arreglo(v)
        if op == 2:
            if v:
                mostrar_arreglo(v)
            else:
                print("No se han cargado el arreglo...")
        if op == 3:
            if v:
                contar(v)
            else:
                print("No se han cargado el arreglo...")
        if op == 4:
            if v:
                generar_archivo_binario(fd,v)
            else:
                print("No se han cargado el arreglo...")
        if op == 5:
            mostrar_archivo(fd)
        if op == 6:
            procesar_texto(v)
        if op == 7:
            print("Saliste del programa...")


#ejecucion de funcion principal...
if __name__ == "__main__":
    principal()

    