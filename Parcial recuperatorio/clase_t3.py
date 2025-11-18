class Contacto:
    def __init__(self, nombre, cod_pais, num_telefonico, tipo_contacto, campo_de_notas):
        self.nombre = nombre
        self.cod_pais = cod_pais
        self.num_telefonico = num_telefonico
        self.tipo_contacto = tipo_contacto
        self.campo_de_notas = campo_de_notas

    def __str__(self):
        return f"Nombre: {self.nombre} | Codigo de pais: {self.cod_pais} | Numero telefonico: {self.num_telefonico} | Tipo contacto: {self.tipo_contacto} | Campo de notas: {self.campo_de_notas}"