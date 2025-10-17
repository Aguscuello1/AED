#ARCHIVOS - APLICACIONES

#CASO DE ANALISIS...


#INSERCION CON BUSQUEDA SECUENCIAL...(muchi tiempo de ejecucion, siempre funciona)
#

""" 
def add_in_order(p, paciente):
    n = len(p)
    pos = n

    for i in range(n):
        if paciente.hist_clinica < p[i].hist_clinica:
            pos = i
            break

    p[pos:pos] = [paciente] 
"""

#INSERCION CON BUSQUEDA BINARIA...(mucho mas veloz)
#si el arreglo esta ordenado 

def add_in_order(p, paciente):
    n = len(p)
    pos = n
    izq , der = 0, n-1

    while izq <= der:
        c = (izq + der) // 2 #calculamos el indice del medio
        if p[c].hist_clinica == paciente.hist_clinica:
            pos = c
            break

        if paciente.hist_clinica < p[c].hist_clinica:
            der = c - 1
        else:
            izq = c + 1 
    
    if izq > der:
        pos = izq

    p[pos:pos] = [paciente]


