#importes
import random
#from moduloT3 import *
from moduloT3 import Servicio


#funciones

#punto 1...
def validar():
    n = int(input("Ingresar cantidad de datos: "))
    while n <= 0:
        n = int(input("Error! Ingresar cantidad de datos (mayor a cero): "))
    return n

def crear_vector(n,vec):
    nombres = ("Juan","Pedro","Susana","Abril","Guido","Mateo","Cata","Facundo","Santiago","Nacho")
    for i in range(n):
        #generar datos
        codigo_id = random.randint(0,50) 
        nombre_cliente = random.choice(nombres)
        tipo = random.randint(1,10)
        importe = round(random.uniform(1000,10000),2)

        #crear el registro
        servicios = Servicio(codigo_id,nombre_cliente,tipo,importe)
        #grabarlo en el vector
        vec.append(servicios)

#punto 2....
def mostrar(vec):
    n = len(vec)
    i1 = float(input("Ingresar primer importe: "))
    i2 = float(input("Ingresar segundo importe: "))
    cs = 0

    for i in range(n-1):
        for j in range(i+1,n):
            if vec[i].codigo_id > vec[j].codigo_id:
                vec[i],vec[j] = vec[j],vec[i]
            
    #mostrar datos cuyos importes esten entre i1 y i2...
    for i in range(n):
        if i1 <= vec[i].importe <= i2:
            cs +=1
            print(vec[i])
    print("Cantidad de servicios contados:", cs)
    print()

#punto 3...
def contar(vec):
    n = len(vec)
    c = 10 * [0]

    for i in range(n):
        ind = vec[i].tipo - 1
        c[ind] +=1

    print("Cantidad de servicios por tipo")
    for k in range(10):
        if c[k] > 0:
            print("tipo de servicio: ",k+1, " - Cantidad: ", c[k])
    print()

#punto 4...
def buscar(vec):
    n = len(vec)
    nom = input("Ingresar nombre a buscar: ")

    for i in range(n):
        if vec[i].nombre_cliente == nom:
            print("Encontrado!")
            vec[i].importe += 2000
            print("Datos del importe actualizados")
            print(vec[i])
            return
    print("No estaba...")
    print()


#principal
def test():
    vec = []
    #menu de opciones:
    op = -1
    while op != 5:
        print("1. Cargar datos")
        print("2. Mostrar datos")
        print("3. Determinar cuantos servicios hay")
        print("4. Encontrar servicio")
        print("5. Salir")

        op = int(input("Ingresar opcion del menu: "))

        if op == 1:
            #validacion de datos del vector...
            n = validar()
            #creando el vector...
            crear_vector(n,vec)
        elif op == 2:
            if vec:
                mostrar(vec)
            else:
                print("No se han cargado datos...")
        elif op == 3:
            if vec:
                contar(vec)
            else:
                print("No se han cargado datos...")                
        elif op == 4:
            if vec:
                buscar(vec)
            else:
                print("No se han cargado datos...")                

        elif op == 5:
            print("El programa se cerro...")
#ejecutando principal
if __name__ == "__main__":
    test()