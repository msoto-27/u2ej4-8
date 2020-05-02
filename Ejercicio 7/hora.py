from fechahora import FechaHora

class Hora:
    __hora = 0
    __minutos = 0
    __segundos = 0
    def __init__(self, hora, minutos, segundos):
        self.__hora = hora
        self.__minutos = minutos
        self.__segundos = segundos
    def Mostrar(self):
        return print('{}:{}:{}'.format(self.__hora, self.__minutos, self.__segundos))
    def __add__(self, otro):
        h = self.__hora + otro.getHora()
        m = self.__minutos + otro.getMinutos()
        s = self.__segundos + otro.getSegundos()
        aux = FechaHora(otro.getDia(), otro.getMes(), otro.getAnio(), h, m, s)
        aux.actualizar()
        return aux
    def __radd__(self, otro):
        h = otro.getHora() + self.__hora
        m = otro.getMinutos() + self.__minutos
        s = otro.getSegundos() + self.__segundos
        aux = FechaHora(otro.getDia(), otro.getMes(), otro.getAnio(), h, m, s)
        aux.actualizar()
        return aux