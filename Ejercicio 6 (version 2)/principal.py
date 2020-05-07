from fechahora import FechaHora

#Validacion

def bisiesto(anio):
    return anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0

def validar(dia, mes, anio, hora, minutos, segundos):
    res = False
    if anio in range(1000, 10000):
        if mes in (1, 3, 5, 7, 8, 10, 12):
            if dia in range(1, 32):
                if hora in range(24) and minutos in range(60) and segundos in range(60):
                    res = True
                else:
                    print('Error en la hora. Los valores validos son: \nHora: 0-23 \nMinutos: 0-59 \nSegundos: 0-59')
            else:
                print('Error en el dia. Los valores validos para el mes ingresado son: 1-31')
        elif mes in (4, 6, 9, 11):
            if dia in range(1, 31):
                if hora in range(24) and minutos in range(60) and segundos in range(60):
                    res = True
                else:
                    print('Error en la hora. Los valores validos son: \nHora: 0-23 \nMinutos: 0-59 \nSegundos: 0-59')
            else:
                print('Error en el dia. Los valores validos para el mes ingresado son: 1-30')
        elif mes == 2:
            if bisiesto(anio):
               if dia in range(1, 30):
                   if hora in range(24) and minutos in range(60) and segundos in range(60):
                       res = True
                   else:
                       print('Error en la hora. Los valores validos son: \nHora: 0-23 \nMinutos: 0-59 \nSegundos: 0-59')
               else:
                    print('Error en el dia. Los valores validos para el mes ingresado en un anio bisiesto son: 1-29')
            else:
               if dia in range(1, 29):
                   if hora in range(24) and minutos in range(60) and segundos in range(60):
                       res = True
                   else:
                       print('Error en la hora. Los valores validos son: \nHora: 0-23 \nMinutos: 0-59 \nSegundos: 0-59')
               else:
                    print('Error en el dia. Los valores validos para el mes ingresado en un anio no-bisiesto son: 1-28')
        else:
            print('Error en el mes. Los valores validos son: 1-12')
    else:
        print('Error en el año. Los valores permitidos son: 1000-9999')
    return res

#Opciones del menu

def salir():
    pass
def sumarHoras():
    resultado = f[0] + f[1]
    print('El resultado es', resultado.mostrar())
def restarHoras():
    resultado = f[0] - f[1]
    print('El resultado es', resultado.mostrar())
def compararHoras():
    resultado = f[0] > f[1]
    if resultado == 1:
        print(f[0].mostrar(), 'es mayor que', f[1].mostrar())
    elif resultado == -1:
        print(f[0].mostrar(), 'es menor que', f[1].mostrar())
    else:
        print(f[0].mostrar(), 'es igual a', f[1].mostrar())
        
switcher = {
    0:salir,
    1:sumarHoras,
    2:restarHoras,
    3:compararHoras,
}

#Main

if __name__ == '__main__':
    f = []
    i = 0
    salir = False
    
    while i<2 and not salir:
        print('\nFecha ', i+1)
        d = int(input('Ingrese dia: '))
        mes = int(input('Ingrese mes: '))
        a = int(input('Ingrese año: '))
        h = int(input('Ingrese hora: '))
        m = int(input('Ingrese minutos: '))
        s = int(input('Ingrese segundos: '))
        if validar(d, mes, a, h, m, s):
            f.append(FechaHora(d, mes, a, h, m, s))
            i += 1
        else:
            salir = True
        
    while not salir:
        print("""
              0 Salir
              1 Sumar horas
              2 Restar horas
              3 Comparar fechas/horas""")
        op = int(input('Ingrese una opcion: '))
        func = switcher.get(op, lambda: print("Opción no válida"))
        func()
        salir = op == 0