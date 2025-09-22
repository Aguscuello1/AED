class Ticket:
    def __init__(self, numero,tipo,descripcion,estado):
        self.numero= numero
        self.tipo = tipo
        self.descripcion = descripcion
        self.estado = estado

def write(ticket):
    print("Numero de identificacion: ", ticket.numero, end = "- ")
    print("Tipo de ticket: ", ticket.tipo, end ="- ")
    print("Descripcion: ", ticket.descripcion, end= "- ")
    print("Estado: ", ticket.estado)
