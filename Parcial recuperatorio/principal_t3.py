from clase_t3 import * 
import random
import os
import pickle


def menu():
    print("=====MENU=====")
    print("1. Cargar el arreglo")
    print("2. Mostrar el arreglo")
    print("3. Calcular y mostrar")
    print("4. Generar y guardar en un archivo binario")
    print("5. Mostrar el archivo binario")
    print("6. Procesar cadena de texto")
    print("7. Salir")

def validar(inf):
    n = int(input("Ingresar cantidad de contactos: "))
    while n <= inf:
        n = int(input("Que sea mayor a ", str(inf), ". Ingresa de nuevo: "))
    return n

def validate_range(mn=0, mx=29):
    cod = int(input('Ingrese valor (>= ' + str(mn) + ' y <= ' + str(mx) + '): '))
    while cod < mn or cod > mx:
        cod = int(input('Error... era >=' + str(mn) + ' y <='+str(mx) + '). De nuevo: '))
    return cod

def add_in_order(v,contactos):
    n = len(v)
    pos = n
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der) // 2
        if v[c].nombre == v[contactos].nombre:
            pos = c
            break

        if v[contactos].nombre > v[c].nombre:
            izq = c + 1
        else:
            der = c - 1

        if izq > der:
            pos = izq
        v[pos:pos] = [contactos]


def cargar_arreglo(v):
    n = validar(0)
    nombres = ("Alejandro", "Luis", "Ana", "Leonardo", "Verónica", "Soledad", "Juan")
    notas = (
        "No llamar nunca2.", "Ni me a4cuerdo quién es.", "Hincha d3e Belgrano.",
        "Amig1azo de5l al2ma.", "Hincha de3 Tall5eres.",
    )
    for i in range(n):
        nombre = random.choice(nombres)
        cod_pais = random.randint(1,999)
        num_telefonico = random.randint(1,20)
        tipo_contacto = random.randint(1,7)
        campo_de_notas = random.choice(notas)
        contactos = Contacto(nombre,cod_pais,num_telefonico,tipo_contacto,campo_de_notas)
        add_in_order(v,contactos)
    return v

def mostrar_arreglo(v):
    n = len(v)
    t = int(input("Ingresar valor de tipo: "))
    cont = 0
    porc = 0

    for contacto in range(n):
        print(v[contacto])
        if v[contacto] == t:
            cont +=1
            if cont >= 1:
                porc = round((cont * 100) / n,2)
    print("Porcentaje de contactos iguales a ", t, ": ", porc)


def contar(v):
    filas = 999
    columnas = 1
    mat = [[0]*columnas for i in range(filas)]

    for con in v:
        f = con.cod_pais - 1
        c = con.tipo - 1 
        mat[f][c]

    print("Conteo por pais y tipo: ")
    for f in range(filas):
        for c in range(columnas):
            if mat[f][c] != 0:
                print("Pais:", f+1, " - Tipo:", c+1, " Cantidad:", mat[f][c])

    acp = 0
    print("Numero del pais a acumular (entre 1 y 999): ")
    p = validate_range(1,999)
    for c in range(columnas):
        acp += mat[p-1][c-1]
    print("Total pais", p, ":", acp)
    print()


def archivo_binario(fd,v):
    m = open(fd,"wb")
    for contactos in v:
        if v[contactos].tipo_contacto != 1:
            pickle.dump(contactos, m)
    m.close()
    print("Archivo generado...")


def mostrar_archivo(fd):
    m = open(fd,"rb")
    t = os.path.getsize(fd)
    cr = 0

    while m.tell() < t:
        cur = pickle.load(m)
        print(cur)
        cr += 1
    m.close()
    print("Cantidad de contactos mostrados: ", cr)

def procesar_cadena(v):
    ultimo = [-1]
    texto = ultimo.notas
    cd = 0
    pal = 0
    ttp = False

    for car in texto:
        if car in " .":
            if cd >= 1 and ttp == False:
                pal += 1
            cd = 0
            ttp = False
        else:
            if car in "123456789":
                cd += 1
            
            if car in "TtPp":
                ttp = True
    print("Texto procesados: ", texto)
    print("Cantidad de palabras con digitos: ", ttp)


def principal():
    v = []
    op = -1
    fd = "archivo.dat"

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
                contar(v)
            else:
                print("No se ha cargado el arreglo...")
        elif op == 4:
            pass
        elif op == 5:
            mostrar_archivo
        elif op == 6:
            if v:
                procesar_cadena(v)
            else:
                print("No se ha cargado el arreglo...")
        elif op == 7:
            print("Saliste del programa...")

if __name__ == "__main__":
    principal()
