class Alumno:
    __max_inasistencias = 10
    __total_clases = 50
    @classmethod
    def getMax(cls):
        return cls.__max_inasistencias
    @classmethod
    def getTotal(cls):
        return cls.__total_clases
    @classmethod
    def setMax(cls, max_i):
        cls.__max_inasistencias = max_i
    def __init__(self, nombre, año, division, inasistencias):
        self.__nombre = nombre
        self.__año = año
        self.__division = division
        self.__inasistencias = inasistencias
    def getNombre(self):
        return self.__nombre
    def getAño(self):
        return self.__año
    def getDiv(self):
        return self.__division
    def getInasistencias(self):
        return self.__inasistencias
    