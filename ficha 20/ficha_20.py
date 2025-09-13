#ARREGLO DE REGISTROS
""" 
class estudiante:
    def __init__(self, leg, nom, pro):
        self.legajo = leg
        self.nombre = nom
        self.promedio = pro
    

def validate(inf):
    n = inf
    while n <= inf:
        n = int(input(f"Ingresar cantidad de elementos (mayor a {str(inf)} por favor): "))
        if n < inf:
            print(f"Error, se pidio una carga mayor a {inf}, carge de nuevo....")
    return n


def read(estudiantes):
    n = len(estudiantes)
    for i in range(n):
        leg = int(input(f"Legajo [{str(i)}]: "))
        nom = input("Nombre: ")
        pro = float(input("Promedio: "))
        print()

        estudiantes[i] = estudiante(leg,nom,pro)

def sort(estudiantes):
    n = len(estudiantes)
    for i in range(n-1):
        for j in range(i+1):
            if estudiantes[i].legajo < estudiantes[j].legajo:
                estudiantes[i],estudiantes[j] = estudiantes[j], estudiantes[i]


def display(estudiantes,x):
    n = len(estudiantes)
    print(f"Estudiantes que haran el curso (tiene promedio >={x}): ")
    for i in range(n):
        if estudiantes[i].promedio >= x:
            write(estudiantes[i])

def write(est):
    print("Legajo:" ,est.legajo, end=" ")
    print(" - Nombre:" ,est.nombre, end=" ")
    print(" - Promedio:" ,est.promedio)

def test():
    #cargar cantidad de estudiantes
    n = validate(0)

    #crear un arreglo con n casileros de valor indefinido...
    #se usara para almacenar las referencias de los estudiantes...
    estudiantes = n * [None]

    #cargar el arreglo por teclado...
    print("Cargue los datos de los estudiantes: ")
    read(estudiantes)
    print()

    x = float(input("Promedio minimo para poder hacer el curso: "))
    print()

    #ordenar el arreglo de menor a mayor, por legajo...
    sort(estudiantes)

    #mostrar por pantalla el listado...
    display(estudiantes,x)



if __name__ == "__main__":
    test() 
"""



