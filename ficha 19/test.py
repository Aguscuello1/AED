#INTRODUCCION A LA POO EN PYTHON (PROGRAMACION ORIENTADA A OBJETOS)

#ejemplo: punto en un plano:
""" 
import geometry



def opcion1():
    cx = float(input("Coordenada x: "))
    cy = float(input("Coordenada y: "))
    p = geometry.init(cx,cy)
    print(p)



def opcion2():
    cx = float(input("Coordenada x: "))
    cy = float(input("Coordenada y: "))
    p = geometry.point(cx,cy)
    d = p.distance()
    print(f"Distancia al origen: {d}")



def opcion3():
    cx1 = float(input("Punto 1 - Coordenada x: "))    
    cy1 = float(input("Punto 1 - Coordenada y: "))    
    p1 = geometry.point(cx1,cy1)

    cx2 = float(input("Punto 2 - Coordenada x: "))
    cy2 = float(input("Punto 2 - Coordenada y: "))
    p2 = geometry.point(cx2,cy2)

    pd = p1.grandient(p2)
    if pd is not None:
        print(f"Pendiente de la recta que los une: {pd}")
    else:
        print("Pendiente no definida (recta vertical)")



def menu():
    op = -1
    while op != 4:
        print("1. Cargar y mostrar un punto.")
        print("2. Distancia del origen.")
        print("3. Pendiente del origen.")
        print("4. Salir.")
        print()

        op = int(input("Ingrese una opcion: "))

        if op == 1:
            opcion1()
        elif op == 2:
            opcion2()
        elif op == 3:
            opcion3


if __name__ == "__main__":
    menu() 
"""



