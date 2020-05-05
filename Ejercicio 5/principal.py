import csv

from alumno import Alumno

def salir():
    pass

def listado():
    año = input('Ingrese año: ')
    div = input('Ingrese division: ')
    div = div.upper() #Coloca la division ingresada en mayusculas
    total_clases = Alumno.getTotal()
    max_i = Alumno.getMax()
    print('    Alumno     Porcentaje de inasistencia')
    for i in lista_alumnos:
        if i.getAño() == año and i.getDiv() == div:
            inas = i.getInasistencias()
            if inas > max_i:
                porcentaje = float(inas * 100 / total_clases) 
                print('%10s %28d %%' %(i.getNombre(), porcentaje))
    
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
    lista_alumnos = []
    archivo = open('alumnos.csv')
    reader = csv.reader(archivo, delimiter = ',')
    for fila in reader:
        lista_alumnos.append(Alumno(fila[0], fila[1], fila[2], int(fila[3])))
    bandera = False
    while not bandera:
        print("""
              0: Salir
              1: Listado de alumnos que superan la cantidad maxima de inasistencias permitidas
              2: Modificar cantidad maxima de inasistencias permitidas""")
        opcion = int(input('Ingrese una opcion: '))
        switch(opcion)
        bandera = opcion == 0