from soporte import * 
import random


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
        elif op == 5:
            print("Adios")
        else:
            ("Opcion incorrecta...")



if __name__ == "__main__":
    principal()