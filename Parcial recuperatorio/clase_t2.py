class Alumno:
    def __init__(self, legajo, nombre, apellido, curso, nota_final, observaciones):
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        self.nota_final = nota_final
        self.observaciones = observaciones

    def __str__(self):
        return f"Legajo: {self.legajo} - Nombre y apellido: {self.nombre} {self.apellido} - Curso: {self.curso} - Nota final: {self.nota_final} - Observaciones: {self.observaciones}"
    