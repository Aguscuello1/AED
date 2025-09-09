#ARREGLOS - ALGORITMOS Y TECNICAS BASICAS

#ORDENAMIENTO POR SELECCION DIRECTA O POR SELECCION SIMPLE...
""" 
como encontrar el menor en un arreglo cualquiera... (no ordenado)
v = [4,6,2,3]

i = 0
for j in range(i +1, n):
    if v[i] > v[j]:
        v[i], v[j] = v[j], v[i]

seleccion directa: de menor a mayor... (ordenado)
v = [4,6,2,3]

def selection_sort(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1,n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]

seleccion directa: de mayor a menor... (ordenado)
v = [4,6,2,3]

def selection_sort(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1,n):
            if v[i] < v[j]:
                v[i], v[j] = v[j], v[i]
    return v

print(selection_sort(v))
"""

#BUSQUEDA SECUENCIAL
""" 
def linear_search(v,x):
    #test de pertenencia ...
    for i in range(len(v)):
        if x == i:
            return True
        return False
    
def linear_search(v,x):
    #retorno de posicion ...
    for i in range(len(v)):
        if x == i:
            return i
        return -1
    
 """


#BUSQUEDA BINARIA ( mas rapido que la busqueda secuencial)
""" 
def binary_search(v,x):
    #busqueda binaria...asume arreglo ordenado...
    izq, der = 0, len(v) -1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c]:
            return c
        if x < v[c]:
            der = c - 1
        else:
            izq = c + 1
    return -1
 """

#FUSION DE ARREGLOS ORDENADOS
""" 
#fusion primera parte...
a = [3,5,7,8]
b = [2,6,9]

n, m = len(a), len(b)
t = n + m

#creamos el tercer arrelgo con todos los valores iguales a 0, arreglo de salida...
c = t * [0]

#aplicamos proceso de fusion...
i = k = j = 0
while i < n and j < m:
    if a[i] < b[i]:
        c[k] = a[i]
        i += 1
    else:
        c[k] = b [i]
        j += 1
    k += 1


#fusion segunda parte...
#apuntar con v al vector que NO termino...
v, pos = b, j

if i < n:
    v, pos = a, i

#copiar en el vector c todo lo que quedaba en v...
while pos < len(v):
    c[k] = v[pos]
    pos += 1
    k +=1 
"""



    
