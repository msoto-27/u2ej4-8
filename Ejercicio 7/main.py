from fechahora import FechaHora

from hora import Hora

#Validacion

def bisiesto(anio):
    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        return True
    else:
        return False

def validarHora(hora, minutos, segundos):
    if hora in range(24):
        if minutos in range(60):
            if segundos in range(60):
                res = True
            else:
                print('Error en los segundos. Los valores validos son: 0-59')
                res = False
        else:
            print('Error en los minutos. Los valores validos son: 0-59')
            res = False
    else:
        print('Error en la hora. Los valores validos son: 0-23')
        res = False
    return res

def validarFechaHora(dia, mes, anio, hora, minutos, segundos):
    if anio in range(1000, 10000):
        if mes in (1, 3, 5, 7, 8, 10, 12):
            if dia in range(1, 32):
                if validarHora(hora, minutos, segundos):
                    res = True
                else:
                    res = False
            else:
                print('Error en el dia. Los valores validos para el mes ingresado son: 1-31')
                res = False
        elif mes in (4, 6, 9, 11):
            if dia in range(1, 31):
                if validarHora(hora, minutos, segundos):
                    res = True
                else:
                    res = False
            else:
                print('Error en el dia. Los valores validos para el mes ingresado son: 1-30')
                res = False
        elif mes == 2:
            if bisiesto(anio):
               if dia in range(1, 30):
                   if validarHora(hora, minutos, segundos):
                       res = True
                   else:
                       res = False
               else:
                    print('Error en el dia. Los valores validos para el mes ingresado en un anio bisiesto son: 1-29')
                    res = False
            else:
               if dia in range(1, 29):
                   if validarHora(hora, minutos, segundos):
                       res = True
                   else:
                       res = False
               else:
                    print('Error en el dia. Los valores validos para el mes ingresado en un anio no-bisiesto son: 1-28')
                    res = False
        else:
            print('Error en el mes. Los valores validos son: 1-12')
            res = False
    else:
        print('Error en el año. Los valores permitidos son: 1000-9999')
        res = False
    return res

if __name__ == '__main__':

   d = int(input("Ingrese Dia: "))

   mes = int(input("Ingrese Mes: "))

   a = int(input("Ingrese Año: "))

   h = int(input("Ingrese Hora: "))

   m = int(input("Ingrese Minutos: "))

   s = int(input("Ingrese Segundos: "))

   if validarFechaHora(d, mes, a, h, m, s):
       f = FechaHora(d,mes,a,h, m, s)

   f.Mostrar()

   input()

   h1 = int(input("Ingrese Hora: "))

   m1 = int(input("Ingrese Minutos: "))

   s1 = int(input("Ingrese Segundos: "))

   if validarHora(h1, m1, s1):
       r = Hora(h1, m1, s1)

   r.Mostrar()

   input()

   f2 = f +r

   f2.Mostrar()

   input()

   f3 = r + f

   f3.Mostrar()

   input()

   f4 = f3 - 1 # Al restar un número entero a un objeto FechaHora se debe restar la cantidad de

                   # días indicada por el número entero

   f4.Mostrar()

   f4 = 1 + f2 # suma un día a un objeto FechaHora

   f4.Mostrar()

   input()        