#imports
import random
from moduloT4 import *

#funciones
#punto 1...
def validar():
    n = int(input("Ingresar cantidad de datos: "))
    while n <= 0:
        n = int(input("Error! Ingresar cantidad de datos (maoyres a cero): "))
    return n

def cargar_vector(vec,n):

    nombres = ("Carlos", "Ana", "José", "María", "Pedro", "Belén", "Martín", "Soledad")
    apellidos = ("Díaz", "Giuliani", "Trejo", "Masiero", "Duplesis", "Johnson", "Iriarte")
    for i in range(n):
        #generar valores...
        codigo = random.randint(0,10)
        nom1 = random.choice(apellidos)
        nom2 = random.choice(apellidos)
        descripcion = nom1 + "vs" + nom2
        tipo = random.randint(1,15)
        nombre = random.choice(nombres) + " " + nom1
        monto = round(random.uniform(1000,10000),2)
    
        #crear registro...
        juicios = Juicio(codigo,descripcion,tipo,nombre,monto)
        #grabarlo en el vector...
        vec.append(juicios)

def mostrar(vec):
    n = len(vec)
    

    for i in range(n-1):
        for j in range(i+1,n):
            if vec[i].descripcion > vec[j].descripcion:
                vec[i],vec[j] = vec[j],vec[i]

    mon = float(input("Ingresar monto: (se mostrara los datos mayoresa a este monto): "))
    c1 = 0
    for i in range(n):
        if vec[i].monto > mon:
            print(vec[i])
            c1 += 1
    print("Cantidad de juicios: ", c1)
    print()

#punto 3...
def contar(vec):
    n = len(vec)
    con = 15 * [0]

    for i in range(n):
        ind = vec[i].tipo - 1
        con[ind] += 1

    c = int(input("Cantidad a filtrar (se mostrarán los contadores con valor mayor a este): "))
    print("Cantidad de juicios por tipo:")

    for k in range(15):
        if con[k] > c:
            print("Tipo de juicio:", k+1, "Cantidad:", ct[k])
    print()

#punto 4...
def buscar(vec):
    n = len(vec)
    cod = int(input("Ingresar codigo a buscar: "))
    for i in range(n):
        if vec[i].codigo == cod:
            print("Encontrado!")
            hon = float(input("Nuevo monto de honorarios: "))
            vec[i].monto = round(hon,2)
            print(vec[i])
            return
    print("No estaba...")
    print()    


#principal
def test():
    vec = []
    #menu principal...
    op = -1
    while op != 4:
        print("1. Cargar datos")
        print("2. Mostrar datos")
        print("3. Determinar y mostrar")
        print("4. Igual codigo de expediente")
        print("5. Salir")

        op = int(input("Ingresar opcion del menu: "))

        if op == 1:
            #validar
            n = validar()
            #cargar el arreglo
            cargar_vector(vec,n)
        elif op == 2:
            if vec:
                mostrar(vec)
            else:
                print("No se han cargado los datos...")
        elif op == 3:
            if vec:
                contar(vec)
            else:
                print("No se han cargado los datos...")
        elif op == 4:
            if vec:
                buscar(vec)
            else:
                print("No se han cargado los datos...")
        elif op == 5:
            print("Se ha cerrado el programa.")
#ejecutando principal
if __name__ == "__name__":
    test()