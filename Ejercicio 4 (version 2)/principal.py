from fechahora import FechaHora

def bisiesto(anio):
    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        return True
    else:
        return False

def validar(dia, mes, anio, hora, minutos, segundos):
    if anio in range(1000, 10000):
        if mes in (1, 3, 5, 7, 8, 10, 12):
            if dia in range(1, 32):
                if hora in range(24) and minutos in range(60) and segundos in range(60):
                    return True
                else:
                    print('Error en la hora. Los valores validos son: \nHora: 0-23 \nMinutos: 0-59 \nSegundos: 0-59')
                    return False
            else:
                print('Error en el dia. Los valores validos para el mes ingresado son: 1-31')
                return False
        elif mes in (4, 6, 9, 11):
            if dia in range(1, 31):
                if hora in range(24) and minutos in range(60) and segundos in range(60):
                    return True
                else:
                    print('Error en la hora. Los valores validos son: \nHora: 0-23 \nMinutos: 0-59 \nSegundos: 0-59')
                    return False
            else:
                print('Error en el dia. Los valores validos para el mes ingresado son: 1-30')
                return False
        elif mes == 2:
            if bisiesto(anio):
               if dia in range(1, 30):
                   if hora in range(24) and minutos in range(60) and segundos in range(60):
                       return True
                   else:
                       print('Error en la hora. Los valores validos son: \nHora: 0-23 \nMinutos: 0-59 \nSegundos: 0-59')
                       return False
               else:
                    print('Error en el dia. Los valores validos para el mes ingresado en un anio bisiesto son: 1-29')
                    return False
            else:
               if dia in range(1, 29):
                   if hora in range(24) and minutos in range(60) and segundos in range(60):
                       return True
                   else:
                       print('Error en la hora. Los valores validos son: \nHora: 0-23 \nMinutos: 0-59 \nSegundos: 0-59')
                       return False
               else:
                    print('Error en el dia. Los valores validos para el mes ingresado en un anio no-bisiesto son: 1-28')
                    return False
        else:
            print('Error en el mes. Los valores validos son: 1-12')
            return False
    else:
        print('Error en el anio. Los valores permitidos son: 1000-9999')
        return False

if __name__ == '__main__':

    d=int(input("Ingrese Dia: "))

    mes=int(input("Ingrese Mes: "))

    a=int(input("Ingrese Año: "))

    h=int(input("Ingrese Hora: "))

    m=int(input("Ingrese Minutos: "))

    s=int(input("Ingrese Segundos: "))
    if validar(d, mes, a, h, m, s):
        r = FechaHora () #  inicilizar día, mes, año con 1/1/2020, y hora, minutos y 

                              #  segundos con 0h, 0m, 0s.

        r1 = FechaHora(d,mes,a); # inicializar con 0h 0m 0s

        r2= FechaHora(d,mes,a,h, m, s)

        r.Mostrar()

        r1.Mostrar()

        r2.Mostrar()

        input()

        r.PonerEnHora(5) # solamente la hora

        r.Mostrar()

        input()

        r2.PonerEnHora(13,30) #hora y minutos

        r2.Mostrar()

        input()

        r.PonerEnHora(14, 30, 25) #hora, minutos y segundos

        r.Mostrar()

        input()

        r.AdelantarHora(3) #sumar 3 horas a la hora actual

        r.Mostrar()

        input()

        r1.AdelantarHora(1,15) #sumar 1 hora y 15 minutos a la hora actual

        r1.Mostrar()

        input()
    