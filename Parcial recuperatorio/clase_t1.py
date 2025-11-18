class Comercio:
    def __init__(self, id, nombre, direccion, cant_empleados, monto):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.cant_empleados = cant_empleados
        self.monto = monto

    def __str__(self):
        return f"Identificador: {self.id} - Nombre: {self.nombre} - Direccion: {self.direccion} - Cantidad de empleados: {self.cant_empleados} - Monto anual de impuestos: {self.monto}"
    
