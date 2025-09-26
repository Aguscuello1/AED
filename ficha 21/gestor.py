from soporte import * 
import random

#funciones
def validar_pos(mensaje):
    n = 0
    while n <= 0:
        n = int(input(mensaje))
        if n <= 0:
            print("Valor incorrecto!")
    return n

def read(tickets):
    for i in range(len(tickets)):
        numero = random.randint(1,1000)
        tipo = random.randint(0,1)
        if tipo == 0:
            descripcion = "Error "
        else:
            descripcion = "Report "
        descripcion += str(numero)
        estado = random.randint(0,2)
        
        tickets[i] = Ticket(numero, tipo, descripcion, estado)


def mostar_vector(tickets):
    for i in range(len(tickets)):
        write(tickets[i])

def matriz(tickets):
    mat = [0] * 2
    for i in range(len(mat)):
        mat[i] = [0] * 3
    
    for i in range(len(tickets)):
        fila = tickets[i].tipo
        col = tickets[i].estado

        mat[fila][col] +=1

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] != 0:
                print("Tipo ", i, "- Estado ", j, "- Cantidad ", mat[i][j])

def buscar(tickets,x):
    for i in range(len(tickets)):
        if x == tickets[i].numero:
            return i
    return -1


#funcion principal
def principal():
    n = validar_pos("Ingrese la cantidad de tickets del mes: ")
    tickets = [None] * n
    carga = False

    op = -1
    while op != 5:
        print("Menu de opciones")
        print("1. Cargar los datos")
        print("2. Mostrar vector")
        print("3. Cantidad por tipo y estado")
        print("4. Buscar")
        print("5. Salir")

        op = int(input("Ingresar opcion del menu: "))

        if op == 1:
            read(tickets)
            carga = True
        elif op == 2:
            if carga:
                mostar_vector(tickets)
            else:
                print("Primero debe cargar los datos...")
                print()
        elif op == 3:
            if carga:
                matriz(tickets)
            else:
                print("Primero debe cargar los datos...")
                print()
        elif op == 4:
            if carga:
                x = int(input("Ingrese el numero de tickets a buscar: "))
                pos = buscar(tickets,x)
                if pos == -1:
                    print("No se ha encontrado el ticket buscado")
                else:
                    tickets[pos].estado = 2
                    write(tickets[pos])


            else:
                print("Primero debe cargar los datos...")
                print()


        elif op == 5:
            print("Adios")
        else:
            ("Opcion incorrecta...")


#ejecucion de funcion principal
if __name__ == "__main__":
    principal()