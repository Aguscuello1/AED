#imports
from clase_t1 import *
import random
import os
import pickle


#funciones
#funcion menu...
def menu():
    print("=====MENU=====")
    print("1. Cargar arreglo")
    print("2. Mostrar los datos")
    print("3. Generar y guardar en un archivo binario")
    print("4. Mostrar el archivo binario.")
    print("5. Buscar en el arreglo")
    print("6. Procesar cadena de caracteres.")
    print("7. Salir")

#funciones 
#punto 1...
def vialidar(inf):
    n = int(input("Ingresar cantidad de objetos: "))
    while n <= inf:
        n = int(input("Tiene que ser mayor a ", str(inf), "Porfavor, ingresar la cantidad de objetos: "))
    return n

def add_in_order(v,comercios):
    n = len(v)
    pos = n
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der) // 2
        if v[c].nombre == comercios.nombre:
            pos = c
            break
        if comercios.nombre < v[c].nombre:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq
    v[pos:pos] = [comercios]
    

def cargar_objetos(v):
    n = vialidar(0)

    nombres = ('Super','Farmacia','Almacen')
    direcciones = ('Avellaneda 123.','San Martin 1520 111.')

    for i in range(n):
        id = random.randint(0, 10)
        nombre = random.choice(nombres)
        direccion = random.choice(direcciones)
        cant_empleados = random.randint(1, 100)
        monto = round(random.uniform(1000, 10000),2)
        comercios = Comercio(id, nombre, direccion, cant_empleados, monto)
        add_in_order(v,comercios)
    print("Arreglo ordenado...")
    print()

    return v


#prunto 2...
def mostrar_arreglo(v):
    n = len(v)
    tot = 0
    for comercio in range(n):
        print(v[comercio])
        tot += v[comercio].cant_empleados
    print("Cantidad de empleados: ", tot)


#punto 3...
def archivo_binario(v,fd):
    n = len(v)
    i1 = int(input("Ingresar primer valor: "))
    i2 = int(input("Ingresar segundo valor: "))
    m = open(fd, "wb")
    
    for comercios in range(n):
        if i1 <= v[comercios].monto <= i2:
            pickle.dump(v[comercios],m)
    m.close()
    print("Archivo generado...")


#punto 4...
def mostrar_archivo(fd):
    m = open(fd,"rb")
    suma,cant = 0, 0

    if not os.path.exists(fd):
        print("No existe el archivo", fd)
        return
    
    t = os.path.getsize(fd)

    while m.tell() < t:
        com = pickle.load(m)
        print(com)
        suma += com.monto
        cant +=1
    m.close()

    #calculamos el promedio...
    if cant > 0:
        prom = suma // cant
    else:
        prom = 0

    print("Promedio: ", prom)


#punto 5...
def buscar_binario(v,nom):
    n = len(v)
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].nombre == nom:
            print("Encontrado: ", v[c])
            return v[c].direccion
        if v[c].nombre < nom:
            izq = c + 1
        else:
            der = c - 1
    return "El comercio no existe, llame al (111) 0303456 para mayor detalle."


#punto 6
def procesar_cadena(rta):
    print(rta)
    impares = ceros = 0
    palb = 0


    for car in rta:
        if car in " .":
            if impares >= 2 and ceros == 0:
                palb += 1
            impares = ceros = 0
        else:
            if car in "13579":
                impares += 1
            if car == "0":
                ceros += 1
    print("Cantidad de palabras que contiene, al menos 2 impares y ningun 0: ", palb)


#funcion principal
def principal():
    v = []
    op = -1
    fd = "comercios.dat"
    rta = ""

    while op != 7:
        menu()
        op = int(input("Ingresar opcion del menu: "))

        if op == 1:
            cargar_objetos(v)
        if op == 2:
            if v:
                mostrar_arreglo(v)
            else:
                print("El arreglo no fue cargado...")
        if op == 3:
            archivo_binario(v,fd)
        if op == 4:
            mostrar_archivo(fd)
        if op == 5:
            if v:
                nom = input("Ingrese nombre: ")
                rta = buscar_binario(v,nom)
        if op == 6:
            if rta == "":
                print("No se realizo ninguna busqueda.")
            else:
                procesar_cadena(rta)
        if op == 7:
            print("Saliste del programa")


#ejecucion de la funcion principal
if __name__ == "__main__":
    principal()

