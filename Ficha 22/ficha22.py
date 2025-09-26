#ORDENAMIENTO

#metodo simples: Intercambio directo(burbuja)
def bubble_sort(v):
    n = len(v)
    for i in range(n-1):
        ordenado = True
        for j in range(n-i-1):
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]
                ordenado = False
        if ordenado:
            break
        


