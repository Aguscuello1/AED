#incluir librerias
import random
from moduloT1 import *

#definicion de funciones

#validar un valor positivo
def validar():
    n = int(input("Ingrese la cantidad de elementos: "))
    while n <= 0:
        n = int(input("ERROR, ingrese la cantidad de elementos: "))
    return n 

#cargar el vector...
def cargar_vector(n, vec):
    for i in range(n):
        #generar datos...
        numero = (i+1)
        descripcion = "Trabajo " + str(numero)
        tipo = random.randint(0,39)
        sueldo = round(random.uniform(1000,10000),2)

        #crear el registro...
        trabajo = Empleo(numero,descripcion,tipo,sueldo)
        #grabarlo en el vector...
        vec.append(trabajo)

#mostrar el vector...
def mostrar(vec):
    suma = 0
    for trabajo in vec:
        print(trabajo)
        suma += trabajo.sueldo

    #mostrar el resultado...
    print("La suma de los importes es: ",suma)

def conteo(vec):
    #definir el vector de contadores...
    vec_conteo = 40 * [0]

    for i in range(len(vec)):
        #obtener la posicion a donde contar...
        pos = vec[i].tipo 
        vec_conteo[pos] += 1

    for i in range(len(vec_conteo)):
        if vec_conteo[i] > 0:
            print(vec_conteo[i])


def buscar(vec):
    n = len(vec)
    num = int(input("Ingresar numero de identificacion del empleo a buscar: "))
    for i in range(n):
        if num == vec[i].numero:
            print("Encontrado!")
            print("Descripcion: " + vec[i].descripcion + " - Sueldo: " + vec[i].sueldo)
            print()
            return
    print("No estaba...")
    print()




#funcion principal
def test():

    vec = []

    #menu de opciones...
    op = -1
    while op != 5:
        print("MENU:")
        print("1. Cargar arreglo")
        print("2. Mostrar ordenado")
        print("3. Conteo por tipo")
        print("4. BUscar")
        print("5. Salir")

        op = int(input("Ingresar opcion: "))

        #evaluar las opciones...
        if op == 1:
            #pedir la cantidad de elementos...
            n = validar()
            #cargar el arreglo...
            cargar_vector(n,vec)

        elif op == 2:
            if vec:
                mostrar(vec)
            else:
                print("El vector no fue cargado...")
        elif op == 3:
            if vec:
                conteo(vec)
            else:
                print("El vector no fue cargado...")
        elif op == 4:
            if vec:
                buscar(vec)
            else:
                print("El vector no fue cargado...")
        elif op == 5:
            print("Salir del programa.")
        else:
            print("Opcion incorrecta...")


#invocacion a la funcion principal
if __name__ == "__main__":
    test()
    
