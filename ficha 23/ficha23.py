#ARCHIVOS

""" 
#ARCHIVOS BINARIOS
m1 = open("datos.dat","w") #lo busca en la carpeta donde tenemos el archivo, modo de apertura(escritura) (grabamos datos)
m2 = open("c:\\datos.dat","r") #(modo de lectura) 

m1.close()
m2.close() 
"""


#GRABACION Y LECTURA DE ARCHIVO BINARIO
#dump() load()

""" 
import pickle

edad, nombre = 23, "Ana"
m1 = open("datos.dat", "wb") 
pickle.dump(edad,m1)
pickle.dump(nombre,m1)
m1.close()


import pickle

m1 = open("datos.dat", "rb") 
edad = pickle.load(m1)
nombre = pickle.load(m1)
m1.close()
print(nombre, edad) 
"""

#EJEMPLO

import pickle

class Libro:
    def __init__(self, cod, tit):
        self.isbn = cod
        self.titulo = tit

def display(libro):
    print("ISBN: ", libro.isbn, end="")
    print("- Titulo: ", libro.titulo)

def test():
    lib1 = Libro(2134,"Funddacion")
    lib2 = Libro(4567,"Fundacion salud")
    lib3 = Libro(1245,"Segunda Fundacion")

    fd = "libros.dat"
    m = open(fd,"wb")

    pickle.dump(lib1,m) #se graban los archivos
    pickle.dump(lib2,m)
    pickle.dump(lib3,m)
    m.close()

    m = open(fd,"rb")
    lib1 = pickle.load(m) #se abren en modo de lectura
    lib2 = pickle.load(m)
    lib3 = pickle.load(m)
    m.close()

    print("Registros de libros: ")
    display(lib1)
    display(lib2)
    display(lib3)

if __name__ == "__main__":
    test()

