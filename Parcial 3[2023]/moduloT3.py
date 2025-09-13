class Servicio:
    def __init__(self,codigo_id, nombre_cliente, tipo, importe):
        self.codigo_id = codigo_id
        self.nombre_cliente = nombre_cliente
        self.tipo = tipo
        self.importe = importe

    def __str__(self):
        res = "El codigo identificatorio es: " + str(self.codigo_id) + " - Nombre: " + str(self.nombre_cliente) + " - Tipo de servicio: " + str(self.tipo) + " - Importe: " + str(self.importe)
        return res
    
    