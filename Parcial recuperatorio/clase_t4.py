class Curso:
    def __init__(self, id, cod_tematica, nombre, costo):
        self.id = id
        self.cod_tematica = cod_tematica
        self.nombre = nombre
        self.costo = costo

    def __str__(self):
        return f"Codigo identificador: {self.id} | Codigo tematica: {self.cod_tematica} | Nombre: {self.nombre} | Costo: {self.costo}"
    