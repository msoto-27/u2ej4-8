def bisiesto(anio):
    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        return True
    else:
        return False

        
class FechaHora:
    __dia = 0
    __mes = 0
    __anio = 0
    __hora = 0
    __minutos = 0
    __segundos = 0
    
    def __init__(self, dia = 1, mes = 1, anio = 2020, hora = 0, minutos = 0, segundos = 0):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
        self.__hora = hora
        self.__minutos = minutos
        self.__segundos = segundos
    def mostrar(self):
        return '{}/{}/{} {}:{}:{}'.format(self.__dia, self.__mes, self.__anio, self.__hora, self.__minutos, self.__segundos)
    def getDia(self):
        return self.__dia
    def getMes(self):
        return self.__mes
    def getAnio(self):
        return self.__anio
    def getHora(self):
        return self.__hora
    def getMinutos(self):
        return self.__minutos
    def getSegundos(self):
        return self.__segundos
    def PonerEnHora(self, hora = 0, mins = 0, seg = 0):
        self.__hora = int(hora)
        self.__minutos = int(mins)
        self.__segundos = int(seg)
    def actualizar(self):
        if self.__segundos > 59:
            self.__segundos -= 60
            self.__minutos += 1
        if self.__minutos > 59:
            self.__minutos -= 60
            self.__hora += 1
        if self.__hora > 23:
            self.__hora -= 24
            self.__dia += 1
        if self.__dia > 31 and self.__mes in (1, 3, 5, 7, 8, 10, 12):
            self.__dia -= 31
            self.__mes += 1
        elif self.__dia > 30 and self.__mes in (4, 6, 9, 11):
            self.__dia -= 30
            self.__mes += 1
        elif self.__mes == 2:
            if bisiesto(self.__anio):
                if self.__dia > 29:
                    self.__dia -= 29
                    self.__mes += 1
            elif self.__dia > 28:
                    self.__dia -= 28
                    self.__mes += 1
        if self.__mes > 12:
            self.__mes -= 12
            self.__anio += 1
    def AdelantarHora(self, hora = 0, mins = 0, seg = 0):
        self.__hora += int(hora)
        self.__minutos += int(mins)
        self.__segundos += int(seg)
        self.actualizar()
    def __add__(self, otro):
        aux = FechaHora(self.__dia, self.__mes, self.__anio)
        h = self.getHora()+otro.getHora()
        m = self.getMinutos()+otro.getMinutos()
        s = self.getSegundos()+otro.getSegundos()
        aux.PonerEnHora(h, m, s)
        aux.actualizar()
        return aux
    def __sub__(self, otro):
        aux = FechaHora(self.__dia, self.__mes, self.__anio)
        h = self.getHora()-otro.getHora()
        m = self.getMinutos()-otro.getMinutos()
        s = self.getSegundos()-otro.getSegundos()
        aux.PonerEnHora(h, m, s)
        if aux.__segundos < 0:
            aux.__segundos += 60
            aux.__minutos -= 1
        if aux.__minutos < 0:
            aux.__minutos += 60
            aux.__hora -= 1
        if aux.__hora < 0:
            aux.__hora += 24
            aux.__dia -= 1
        if aux.__dia < 1:
            aux.__mes -= 1
            if aux.__mes < 1:
                aux.__anio -= 1
                aux.__mes += 12
            if aux.__mes in (1, 3, 5, 7, 8, 10, 12):
                aux.__dia += 31
            elif aux.__mes in (4, 6, 9, 11):
                aux.__dia += 30
            elif aux.__mes == 2 and bisiesto(aux.__anio):
                aux.__dia += 29
            else:
                aux.__dia += 28
        return aux

    def __gt__(self, otro):
        if self.__anio > otro.getAnio():
            res = 1
        elif self.__anio < otro.getAnio():
            res = -1
        else:
            if self.__mes > otro.getMes():
                res = 1
            elif self.__mes < otro.getMes():
                res = -1
            else:
                if self.__dia > otro.getDia():
                    res = 1
                elif self.__dia < otro.getDia():
                    res = -1
                else:
                    if self.__hora > otro.getHora():
                        res = 1
                    elif self.__hora < otro.getHora():
                        res = -1
                    else:
                        if self.__minutos > otro.getMinutos():
                            res = 1
                        elif self.__minutos < otro.getMinutos():
                            res = -1
                        else:
                            if self.__segundos > otro.getSegundos():
                                res = 1
                            elif self.__segundos < otro.getSegundos():
                                res = -1
                            else:
                               res = 0
        return res