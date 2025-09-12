#REGISTROS
""" 
a1 = 1, "AED"
a2 = 2, "PRR"
a3 = 3, "TSB"

print('Asignatura 1 - Código:', a1[0], 'Nombre:', a1[1])
print('Asignatura 2 - Código:', a2[0], 'Nombre:', a2[1])
print('Asignatura 3 - Código:', a3[0], 'Nombre:', a3[1])
 """

""" 
#tipo de dato
class empleado:
    pass

e1 = empleado()
e1.legajo = 1
e1.nombre = "Juan"
e1.direccion = "Calle 1"
e1.sueldo = 10000
e1.antiguedad = 10

#Se puede tener campos diferentes en registros del mismo tipo...(rol)
e2 = empleado()
e2.legajo = 2
e2.nombre = "Luis"
e2.direccion = "Calle 2"
e2.sueldo = 30000
e2.antiguedad= 5
e2.cargo = "jefe de area" #-----> no existe en e1


#Registros: Operaciones
e1.legajo = 4
e1.antiguedad = e2.antiguedad
e2.sueldo = float(input("Ingrese nuevo sueldo de empleado 2:"))
print(f"Direccion del empleado 1: {e1.direccion}")
e2.antiguedad +=1 
"""


#REGISTROS: CREACION CON FUNCION DE INICIALIZACION
""" 
class empleado():
    pass

def init(empleado,leg,nom,direc,suel,ant):
    empleado = empleado()
    empleado.legajo = leg
    empleado.nombre = nom
    empleado.direccion = direc
    empleado.sueldo = suel
    empleado.antiguedad = ant
    return empleado

def test():
    e1 = init(e1,1,"Juan","Calle 1",5999,10)
    e2 = init(e2,1,"Pedro","Calle 2",80000,2)
    

#REGISTROS: CREACION CON FUNCION CONSTRUCTORA

class empleado:
    def __init__(self, leg,nom,direc,suel,ant):
        self.legajo = leg
        self.nombre = nom
        self.direccion = direc
        self.sueldo = suel
        self.antiguedad = ant

def test():
    e1 = empleado(1,"juan","calle 1",1000,10) 
"""







    
