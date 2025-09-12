""" 
import math

class point:
    def __init__(self,cx, cy,desc = "p"): #-----> metodo
        self.x = cx #----> atributos
        self.y = cy
        self.descripcion = desc


    def __str__(self):
        r = str(self.descripcion) + "(" + str(self.p.x) + "," + str(self.y) + ")"
        return r

    def distance(self):
        #pitagoras...
        return math.sqrt(pow(self.x,2) + pow(self.y,2))

    def grandient(self,p2):
        #Calcular delta x y delta y...
        dy = p2.y - self.y
        dx = p2.x - self.x

        #si los puntos no son colineales verticales, retornar la pendiente...
        if dx != 0:
            return dy/dx
        
        #de otro modo, la pendiente es indefinida...
        #este retorno deberia ser controlado al regresar...
        return None
 """
