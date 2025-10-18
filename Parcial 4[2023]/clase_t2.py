class Libro:
    def __init__(self, isbn, titulo, autor, cod_idioma, precio):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.cod_idioma = cod_idioma
        self.precio = precio


    def __str__(self):
        r = ""
        r += "{:<20}".format("ISBN: " + str(self.isbn))
        r += "{:<35}".format("Titulo: " + str(self.titulo))
        r += "{:<35}".format("Autor: " + str(self.autor))
        r += "{:<10}".format("Codigo de idioma: " + str(self.cod_idioma))
        r += "{:<17}".format(" Precio: " + str(self.precio))

        return r