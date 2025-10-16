#ARCHIVOS DE TEXTO
#GRABACION Y LECTURA
    #m.write(cadena) sin salto de linea
    #cad = m.read() lee y retorna todo el archivo
    #cad  = m.readline() lee y retorna hasta el primer salto de linea o hasta el final del archivo
    #cad  = m.readlines() lee y retorna todas las lineas en una lista o arreglo.

""" 
#USO DEL WRITEA(CAD)  #sin salto de linea
m = open("datos.txt", "wt")
m.write("Una linea de texto")
m.write("Segunda linea de texto") 
m.close()

#USO DEL WRITEA(CAD)  #con salto de linea
m = open("datos.txt", "wt")
m.write("Una linea de texto\n")
m.write("Segunda linea de texto") 
m.close()

#USO DEL READ()
m = open("datos.txt", "r")
cad = m.read()
print("Contenido completo: ")
print(cad)
m.close()

#USO DE READLINE()
m = open("datos.txt")
r1 = m.readline()
r2 = m.readline()
print("\nContenido linea por linea: ")
print(r1, end="")
print(r2)
m.close()

#USO DE READLINES()
m = open("datos.txt", "r")
lista = m.readlines()
print("\nLista de lineas contenidas: ")
print(lista)
m.close()



#LECTURA CON CICLO INTEGRADOR...
m = open("datos.txt")
print("\nContenido con iterador: ")
for linea in m:
    print(linea, end="")
m.close()

#LECTURA CONTROLADA....
m = open("datos.txt")
print("\nContenido con control de lectura: ")

while True:
    #intentar leer una linea...
    linea = m.readline()

    #¿Cadena vacia? cortar el ciclo...
    if linea == "":
        break

    #si lo tenia, sacar el caracter salto de linea...
    if linea[-1] == "\n":
        linea = linea[:-1]

    print(linea)

m.close() 
"""

#REPOSICIONAMIENTO DEL FILE POINTER
seek()
io.SEEK_SET
io.SEEK_CUR
io.SEEK_END


