from alumno import Alumno

from listaalumnos import ListaAlumnos

def salir():
    pass

def listado():
    año = input('Ingrese año: ')
    div = input('Ingrese division: ')
    div = div.upper() #Coloca la division ingresada en mayusculas
    lista_alumnos.mostrarListado(año, div)
    
def modificar():
    maximo = int(input('Ingrese el nuevo maximo de inasistencias permitido: '))
    Alumno.setMax(maximo)
    
switcher = {
    0: salir,
    1: listado,
    2: modificar
}

def switch(arg):
    func = switcher.get(arg, lambda: print("Opción no válida"))
    func()

if __name__ == '__main__':
    lista_alumnos = ListaAlumnos('alumnos.csv')
    
    bandera = False
    while not bandera:
        print("""
              0: Salir
              1: Listado de alumnos que superan la cantidad maxima de inasistencias permitidas
              2: Modificar cantidad maxima de inasistencias permitidas""")
        opcion = int(input('Ingrese una opcion: '))
        switch(opcion)
        bandera = opcion == 0