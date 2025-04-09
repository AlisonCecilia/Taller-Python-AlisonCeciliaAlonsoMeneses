#Desarrolla un programa en Python que utilce
#la POO para registrar un libro (ISBN,TITULO
#y AUTOR
#Los atributos deben estar en privado
#debes tener un contrustor para el registro
#Debes tener solo getters de cada atributo

#En otra clase debera registrar una coleccion
#de libros
#En esta clase debes tener add, delete y show

class libro:
    def __init__(self, isbn, titulo, autor):
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor

    def getIsbn(self):
        return self.__isbn

    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

class RegistrarLibros:
    def __init__(self):
        self.libros = []

    def add(self, isbn,titulo,autor):
        self.libros.append(libro(isbn,titulo,autor))
        print(f"Libro '{getTitulo()}' agregado.")

    def delete(self, isbn):
        for libro in self.libros:
            if libro.get_isbn() == isbn:
                self.libros.remove(libro)
                print(f"Libro con ISBN {isbn} eliminado.")
            else:
                print(f"No se encontró ningún libro con ISBN {isbn}.")

    def show(self):
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            print("Biblioteca:")
            for libro in self.libros:
                print(f"ISBN: {libro.get_isbn()}, Título: {libro.get_titulo()}, Autor: {libro.get_autor()}")

if __name__ == "__main__":
    biblioteca = RegistrarLibros()
    biblioteca.add("00101", "Metamorfosis", "Franz Kafka")
    biblioteca.add("00102", "Metamorfosis", "Franz Kafka")
    biblioteca.add("00103", "Metamorfosis", "Franz Kafka")
    biblioteca.add("00104", "Metamorfosis", "Franz Kafka")
    biblioteca.add("00105", "Metamorfosis", "Franz Kafka")
    biblioteca.add("00106", "Metamorfosis", "Franz Kafka")
    biblioteca.add("00107", "Metamorfosis", "Franz Kafka")

    biblioteca.show()

    biblioteca.delete("00105")
    biblioteca.show()










