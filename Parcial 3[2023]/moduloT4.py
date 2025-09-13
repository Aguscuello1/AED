class Juicio:
    def __init__(self, codigo, desc, tipo, nombre, monto):
        self.codigo = codigo
        self.descripcion = desc
        self.tipo = tipo
        self.nombre = nombre
        self.monto = monto

    def __str__(self):
        res = "Codigo: ", str(self.codigo), " - Descripcion: ", str(self.descripcion), " - Tipo: ", str(self.descripcion), " - Nombre: ", str(self.nombre), " - Monto: ", str(self.monto)
        return res