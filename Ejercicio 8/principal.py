import csv

from conjunto import Conjunto

#Opciones del menu

def salir():
    pass
def unionConjuntos():
    resultado = c[0] + c[1]
    print('El conjunto resultante es', resultado.getConj())
def diferenciaConjuntos():
    resultado = c[0] - c[1]
    print('El conjunto resultante es', resultado.getConj())
def igualdadConjuntos():
    resultado = c[0] == c[1]
    if resultado:
        print('Los conjuntos son iguales')
    else:
        print('Los conjuntos son desiguales')
        
switcher = {
    0:salir,
    1:unionConjuntos,
    2:diferenciaConjuntos,
    3:igualdadConjuntos,
}


if __name__ == '__main__':
    
    archivo = open('conjuntos.csv')
    reader = csv.reader(archivo, delimiter = ',')
    c = []
    i = 0
    for fila in reader:
        c.append(Conjunto())
        for j in fila:
            c[i].agregar(j)
        i += 1
    print('Conjunto 1: ', c[0].getConj())
    print('Conjunto 2: ', c[1].getConj())
    salir = False
    while not salir:
        print("""
              0 Salir
              1 Union de dos conjuntos
              2 Diferencia de dos conjuntos
              3 Igualdad entre dos conjuntos""")
        op = int(input('Ingrese una opcion: '))
        func = switcher.get(op, lambda: print("Opción no válida"))
        func()
        salir = op == 0