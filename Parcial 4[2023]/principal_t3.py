import random
import clase_t3
import os.path
import pickle


#funciones
def menu():
    print("1. Cargar arreglo")
    print("2. Mostrar arreglo")
    print("3. Contar")
    print("4. Generar archivo binario")
    print("5. Mostrar archivo.")
    print("6. Salir")


def validar(inf):
    n = int(input("Ingresar cantidad de pantalones: "))
    while n <= inf:
        n = int(input("Error, se pidio un valor mayor a ", str(inf), "...Cargue de nuevo: "))
    return n


def add_in_order(v, reg):
    n = len(v)
    pos = n
    izq , der = 0 , n - 1

    while izq <= der:
        c = (izq + der) // 2
        if v[c].codigo == reg.codigo:
            pos = c
            break

        if reg.codigo < v[c].codigo:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq
    v[pos:pos] = [reg]
    

def cargar_vector():
	n = validar(0)
	v = []
	for i in range(n):
		codigo = random.randint(100, 100000)
		nombre = "Pantalon " + str(random.randint(1500, 33450))
		largo = random.randint(30, 50)
		cintura = random.randint(30, 50)
		tela = random.randint(1, 3)
		stock = random.randint(1, 1500)
		reg = clase_t3.Pantalon(codigo, nombre, largo, cintura, tela, stock)
		add_in_order(v, reg)
	return v
    
def mostrar(v):
    n = len(v)
    print("Listado de pantalones...")
    for i in range(n):
        print(v[i])
    print()

def generar_matriz(v):
    m = [[0] * 21 for j in range(21)]
    n = len(v)

    for i in range(n):
        f = v[i].largo - 30
        c = v[i].cintura - 30
        m[f][c] += v[i].sotck

    return m

def mostrar_matriz(m, u):
    for f in range(len(m)):
        for c in range(len(m[f])):
            if m[f][c] > u:
                print("Largo ", f + 30, " Cintura ", c + 30, " Stock: ", m[f][c])
    print()

def generar_archivo(v, fd, tela):
    n = len(v)
    m = open(fd, "wb")
    for i in range(n):
        if v[i].stock > 0 and v[i].tipo_tela == tela:
            pickle.dump(v[i], m)
    m.close()


def calcular_promedio(cantidad, total):
    promedio = 0
    if cantidad > 0:
        promedio = total // cantidad
    return promedio


def mostrar_archivo(fd):
    t = os.path.getsize(fd)
    m = open(fd, "rb")
    cont = acu = 0

    while m.tell() < t:
        reg = pickle.load(m)
        acu += reg.stock
        cont += 1
        print(reg)

    m.close()
    prom = calcular_promedio(cont, acu)
    print("El stock promedio disponible es", prom, " unidades")


#funcion principal...
def princial():
    fd = "datos.dat"
    v = []
    op = -1
    while op != 6:
        menu()
        op = int(input("Ingresar opcion del menu: "))

        if op == 1:
            v = cargar_vector()
        elif op == 2:
            if v:
                mostrar(v)
            else:
                print("No se ha cargado el vector...")

        elif op == 3:
            if v:
                m = generar_matriz(v)
                u = int(input("Ingrese la cnatidad de unidades minimas a mostrar..."))
                mostrar_matriz(m, u)
            else:
                print("No se ha cargado el vector...")
                
        elif op == 4:
            if v:
                tela = int(input("Ingresar tipo de tela..."))
                generar_archivo(v,fd, tela)
        elif op == 5:
            if os.path.exists:
                pass
            else:
                print("El archivo no fue generado....")
        elif op == 6:
            print("Saliste del programa...")

#eje. principal...
if __name__ == "__main__":
    princial()

