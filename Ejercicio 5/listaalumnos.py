import csv

from alumno import Alumno

class ListaAlumnos:
    def __init__(self, nombre_archivo):
        self.__lista = []
        archivo = open(nombre_archivo)
        reader = csv.reader(archivo, delimiter = ',')
        for fila in reader:
            self.__lista.append(Alumno(fila[0], fila[1], fila[2], int(fila[3])))
    def mostrarListado(self, año, div):
        total_clases = Alumno.getTotal()
        max_i = Alumno.getMax()
        print('    Alumno     Porcentaje de inasistencia')
        for i in self.__lista:
            if i.getAño() == año and i.getDiv() == div:
                inas = i.getInasistencias()
                if inas > max_i:
                    porcentaje = float(inas * 100 / total_clases) 
                    print('%10s %28d %%' %(i.getNombre(), porcentaje))
    