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

""" p = []
for i in range(3):
    p.append([])
    for j in range(2):
        p[i].append([])
        for k in range(4):
            p[i][j].append([])

p[2][1][3] = 'Prueba'
print(p) """

""" 
def test(mat):
    fils = len(mat)
    cols = len(mat[0])
    for k in range(cols):
        ac = 0
        for g in range(fils):
            ac += mat[k][g]
        p = ac / fils
        print('Indice:', k, '- Promedio:', p)

test(mat = [[]]) 
"""

def test(mat):
    n = len(mat)
    m = len(mat[0])

    r = m * [0]
    for i in range(m):
        ac = 0
        for j in range(n):
            ac += mat[j][i]
        r[i] = ac / n

    return r

test(mat = [1])