#clase libro con object
import os

class Libro(object):
    def __init__(self, id, titulo, autor, editorial):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
    
    def __str__(self):
        return '%s - %s - %s - %s ' %\
        (self.id, self.titulo, self.autor, self.editorial)
    
    def __getattribute__(self, atrib):
        return object.__getattribute__(self, atrib)

class LibroAdmin():
    def __init__(self):
        self.arregloLibros = []

    def agregar(self, id, titulo, autor, editorial):
        lib = Libro(id, titulo, autor, editorial)
        self.arregloLibros.append(lib)

    def __str__(self):
        s = ''
        for lib in self.arregloLibros:
            s += str(lib) + '\n'
        return s

    def buscar(self, clave , por = 'id'):
         for indice, libro in enumerate(self.arregloLibros):
            if libro.__getattribute__ (por) == clave:
                return indice

    def remover(self, clave, por = 'id'):
        indice = self.buscar(clave)
        if indice != None:
            self.arregloLibros.pop(indice)
            return indice
    

def menuPrincipal():
    while True:
        print('=====================================================')
        print('                      OPCIONES                       ')
        print('=====================================================')

        print('|1| Ingresar un libro')
        print('|2| Buscar un elemento por ID')
        print('|3| Remover un elemento por ID ')
        print('|4| Listar ')
        print('|5| Salir \n')
        eleccion = input('Seleccione una opcion. ')

        if eleccion == '1':
            insertar()
        
        elif eleccion == '2':
            buscar()

        elif eleccion == '3':
            eliminar()

        elif eleccion == '4':
            listar()
        
        elif eleccion == '5':
            os.system('cls')
            print('\n Saliendo... ')
            break
        
        else:
            os.system('cls')
            print('Selecciona una opcion valida... \n ')


def insertar():
    os.system('cls')
    nLibros = int(input('¿Cuantos libros deseas ingresar? => '))
    for i in range(nLibros):
            print('\n INGRESE UN LIBRO. \n ')
            id = input('ID => ')
            titulo = input('\nTitulo => ')
            autor = input('\nAutor => ')
            editorial = input('\nEditorial => ')
            os.system('cls')
            arreglo.agregar(id, titulo, autor, editorial)
            print('\n', arreglo)

def eliminar():
    os.system('cls')
    remover = input("ID del elemento a eliminar: ")
    indexRemover = arreglo.remover(remover)
    if indexRemover is not None:
        print("\nElemento a remover de ls posicion: {0}".format(indexRemover))
    else:
        print("\nEste ID no se encuentra en el registro.")

def buscar():
    os.system('cls')
    buscado = input("ID del elemento a buscar: ")
    indexBuscado = arreglo.buscar(buscado)
    if indexBuscado is not None:
        print("\n Elemento encontrado en posicion: {0}".format(indexBuscado))
    else:
        print("\n Este ID no se encuentra en el registro.")

def listar():
    os.system('cls')
    print(arreglo)
    input('Presiona ENTER para continuar >>> ')

# Programa principal.

os.system('cls')
arreglo = LibroAdmin()

menuPrincipal()



