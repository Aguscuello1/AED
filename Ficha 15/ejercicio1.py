#ULTIMO Y PRIMERO...

import arreglos1_1

def test():

    print("*"*80)
    n = arreglos1_1.validar_tamaño()
    v = arreglos1_1.crear(n)
    print("*"*80)
    rep = arreglos1_1.contar_repeticiones(v)
    print(f"El ultimo numero se repite {rep} veces en el vector.")
    print("*"*80)
    menores = arreglos1_1.buscar_menores(v)
    print(f"Los valores menores al primer elemento son {menores}")



if __name__ == "__main__":
    test()
