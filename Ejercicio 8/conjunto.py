class Conjunto:
    def __init__(self):
        self.__conj = []
    def agregar(self, elemento):
        self.__conj.append(elemento)
    def getConj(self):
        return self.__conj
    def __add__(self, otro):
        aux = Conjunto()
        for i in self.__conj:
            aux.agregar(i)
        otro_conj = otro.getConj()
        aux_conj = aux.getConj()
        for i in otro_conj:
            if i not in aux_conj:
                aux.agregar(i)
        return aux
    def __sub__(self, otro):
        aux = Conjunto()
        otro_conj = otro.getConj()
        for i in self.__conj:
            if i not in otro_conj:
                aux.agregar(i)
        return aux
    def __eq__(self, otro):
        otro_conj = otro.getConj()
        res = True
        if len(self.__conj) == len(otro_conj):
            for i in self.__conj:
                if i not in otro_conj:
                    res = False
        else:
            res = False
        return res