#ARREGLO UNIDIMENSIONAL

#CREACION Y USO:
#dos formas de crear arreglo unidimensional:
""" 
v = []
v = list()
los dos son arreglos vacios...



ARREGLO CON VALORES DE ANTEMANO...
v = [1,2,3,4,5,6] ---> ese arreglo tiene 7 COMPONENTES...   

PUEDE CONTENER VALORES DE TIPOS DIFERENTES...
v = ["Luis", 78, "Masculino", 45.909.045] 
"""
#ACCESO Y MODIFICACION DE COMPONENTES INDIVIDUALES:
""" cambiando de valor los componentes... 
v = [1,2,3,4,5,6]
v[1] = 7
usandolo el arreglo unidimensional como contador... 
v = [1,2,3,4,5,6]
v[0] += 1
mostrar un valor del arreglo... 
v = [1,2,3,4,5,6]
print(v[2])
operacion entre componentes del arreglo... 
v = [1,2,3,4,5,6]
v[2] = v[0] + v[4]
print(v)
carga por teclado un valor directamente para un componente del arreglo... 
v = [1,2,3,4,5,6]
v[2] = input("Ingrese lo que quiera: ")
print(v) 
si se necesita crear una lista con cierta cant de elementos iguales a un valor dado, usamos la multiplicacion y repetimos n veces...
ceros = 15 * [0]
print('Arreglo de 15 ceros:', ceros)
# muestra: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] """

#CARGA DE UN ARREGLO(metodo append)...
""" 
notas = []
notas.append(4)
notas.append(7)
notas.append(8)
notas.append(5)
print('Notas:', notas)
muestra: Notas: [4, 7, 8, 5] 

uso de la funcion len...
n = 4
notas = n *[0]
for i in range(n):
    notas[i] = int(input("nota: "))
print(notas)

suma = 0
n = len(notas)
for i in range(n):
 suma += notas[i]
promedio = suma // n
print(promedio)
"""

#INDICES NEGATIVOS - ELIMINACION DE COMPONENTES...
""" 
indices negativos...
v = [1,2,3,4]
print(v[-1])

eliminacion de componentes(del)...
numeros = [1,2,3,4]
del numeros[2] ---> del es una instruccion, tambien puede eliminar el arreglo completo
print(numeros)
"""

#CORTES DE INDICE...
""" 
numeros = [1,2,3,4]
nueva = numeros[1:3]
print(nueva)

insertar un elemento.... en este caso en la posicion 2... 
numeros = [1,2,3,4]
numeros[2:2] = [90]
print(numeros)

como interpreta python si no agregamos un indice al final del corte... 
numeros = [1,2,3,4,5,6,7]
nueva = numeros [2:]
print(nueva)---->[3, 4, 5, 6, 7]---> note como python interpreta que es hasta el final de la lista... 

numeros = [1,2,3,4,5,6,7]
nueva = numeros [:]
print(nueva)--->[1,2,3,4,5,6,7]----> toma toda la lista...

numeros = [1,2,3,4,5]
nueva = numeros[2:-1]---> como no el indice no toma el 5 sino que toma el anterior...
print(nueva)

numeros = [1,2,3,4,5,6,7,8]
nueva = numeros[2:6] * 2 ---> al colocar el operador * 2, la lista se copia dos veces y se guarda en la variante...
print(nueva)  

numeros = [1,2,3,4,5]
nueva = numeros[1:4] + [76,89,66]
print(nueva) 
"""

#MANERA DE CREAR UN ARREGLO DE N COMPONENETES...
"""
forma tipica...
n = int(input("Ingresar tamanaño del arreglo: "))
numeros = []
for i in range(1, n+1):
    numeros.append(i)
print (f"Arreglo creado: {numeros}")

lo mismo, por comprension... 
n = 10
numeros = [i for i in range(1, n+1)]
print(f"Arreglo creado: {numeros}") 
"""


#OBTENER UNA LISTA DE TUPLAS (X,Y) CON (X IN V1) AND (Y IN V2) AND (X < Y)...
"""
v1 = [7,3,4,8]
v2 = [1,3,5,9]
pares = []
for x in v1:
    for y in v2:
        if x < y:
            pares.append((x,y))

print(f"Pares formados {pares}") """


v1 = [7,3,4,8]
v2 = [1,3,5,9]
pares = [(x,y) for x in v1 for y in v2 if x < y]
print(f"Pares formados {pares}")

