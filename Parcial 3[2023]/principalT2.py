#incluir librerias...
import random
from moduloT2 import *

#definicion de funciones...
#punto 1...
def validar():
    n = int(input("Ingrese cantidad de tickets: "))
    while n <= 0:
        n = int(input("Error! Ingrese cantidad de tickets: "))
    return n

def cargar_vector(n, vec):
    nombres = ("AJ","BC","ZE","RT","PL","HS","UB","KW","LM")
    for i in range(n):
        #generar datos...
        codigo = random.choice(nombres) + str(i)
        numero_id = random.randint(1,400)
        destino = random.randint(1,20)
        numero_asiento = random.randint(1,200)
        importe = round(random.uniform(0,2000),2)
       
        #crear el registro...
        tickets = Ticket(codigo,numero_id,destino,numero_asiento,importe)

        #grabarlo en el vector...
        vec.append(tickets)

#punto 2...
def mostrar(vec):
    #ordenar de menor a mayor, por orden de codigo de vuelo(codigo)
    n = len(vec)
    for i in range(n-1):
        for j in range(i+1,n):
            if vec[i].codigo > vec[j].codigo:
                vec[i],vec[j] = vec[j],vec[i]
    
    #mostramos los datos de todos los tickets cuyo numero de asiento sea mayor
    #a un valor num que se carga por teclado
    num = int(input("Número de asiento (se mostrarán los tickets cuyo número de asiento sea mayor a este): "))
    for i in range(n):
        if vec[i].numero_asiento > num:
            print(vec[i])
    print()


#punto 3...
def acumular(vec):
    n = len(vec)
    c = 20 * [0]

    for i in range(n):
        ind = vec[i].destino - 1
        c[ind] += vec[i].importe

    t = int(input("Importe (se mostrara los acumuladores mayoresa a este valor: )"))
    print(f"Importes acumulados por pais, mayores a {t}: ")
    
    for k in range(20):
        if c[k] > t:
            print("Pais destino: ", k+1, "Importe acumulado: ", round(c[k],2))
    print()

#punto 4....
def buscar(vec):
    n = len(vec)
    id = int(input("Numero de identificacion del pasajero a buscar: "))

    for i in range(n):
        if id == vec[i].numero_id:
            print("Encontrado")
            print("Numero de asiento: ", vec[i].numero_asiento, " - Pais de destino: ", vec[i].destino)
            print()
            return
    print("No estaba")
    print()

#funcion principal...
def test():

    vec = []

    #menu de opciones...
    op = -1
    while op != 5:
        print("MENU")
        print("1. Cargar el arreglo")
        print("2. Mostrar")
        print("3. Importe acumulado")
        print("4. Identificacion de ticket")
        print("5. Salir del programa")

        op = int(input("Ingresar opcion del menu: "))

        if op == 1:
            #pedir la cantidad de elementos...
            n = validar()
            #cargar el arreglo...
            cargar_vector(n,vec)
        elif op == 2:
            if vec:
                mostrar(vec)
            else:
                print("El arreglo no fue cargado...")
        elif op == 3:
            if vec:
                acumular(vec)
            else:
                print("El arreglo no fue cargado...")
        elif op == 4:
            if vec:
                buscar(vec)
            else:
                print("El arreglo no fue cargado...")
        elif op == 5:
            print("Se ha terminado el programa...")
#invocacion a la funcion principal...
if __name__ == "__main__":
    test()