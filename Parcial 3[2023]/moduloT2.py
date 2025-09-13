class Ticket:
    def __init__(self, codigo,numero_id, destino,numero_asiento, importe):
        self.codigo = codigo
        self.numero_id = numero_id
        self.destino = destino
        self.numero_asiento = numero_asiento
        self.importe = importe


    def __str__(self):
        res = "Codigo de vuelo: " + str(self.codigo) + " - Numero de identificion: " + str(self.numero_id) + " - Destino: " + str(self.destino) + " - Numero de asiento: " + str(self.numero_asiento) + " - Importe: " + str(self.importe)
        return res
    
    