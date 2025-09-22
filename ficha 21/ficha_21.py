#ARREGLOS BIDIMENSIONALES

"""
#creacion de una matriz con valores fijos...
m0 = [
    [1,3,4],
    [3,5,2],
    [4,7,1]
]

print("Matriz con valores fijos: ", m0)

#forma equivalente...
 m0 = [[1,3,4],[3,5,2],[4,7,1]]
print(m0) """


""" 
#primera forma...
n = 3, m = 4

m1 = []
for f in range(n):
    m1.append([])
    for c in range(m):
        m1[f].append(None)

#segunda forma...
n = 3, m = 4

m2 = [None] * n
for f in range(n):
    m2[f] = [None] * m

#tercera forma... (por comprension)
n = 3, m = 4

m3 = [[None] * m for f in range(n)] 
"""

#RECORRIDO Y CARGA DE UNA MATRIZ

""" 
len(a) = la cantidad de filas
len(a[f]) = la cantidad de columnas
"""




