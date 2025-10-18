def add_in_order(v, poke):
    n = len(v)
    izq, der = 0, n - 1
    pos = n

    while izq <= der:
        c = (izq + der) // 2
        if v[c].numero == poke.numero:
            pos = c
            break
        elif v[c].numero > poke.numero:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq
    v[pos:pos] = [poke]
    



def cargar(v):
    n = validar(0)

    for i in range(n):
        poke = generar_aleatorio()
        add_in_order(v,p)