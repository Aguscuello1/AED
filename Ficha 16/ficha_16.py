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
    
