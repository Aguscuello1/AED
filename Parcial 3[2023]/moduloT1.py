
class Empleo:
    #funcion para cargar los valores a los campos...
    def __init__(self, numero, descripcion, tipo, sueldo):
        self.numero = numero
        self.descripcion = descripcion
        self.tipo = tipo
        self.sueldo = sueldo

    #funcion que retorne un string con los datos del trabajo...
    def __str__(self):
        r = "Numero: " + str(self.numero) + " - Descripcion: " + str(self.descripcion) + " - Tipo: " + str(self.tipo) + " - Sueldo: " + str(self.sueldo)
        return r
    

