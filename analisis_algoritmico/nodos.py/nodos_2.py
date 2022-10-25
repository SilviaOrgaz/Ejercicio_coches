class Nodo(object):
    info, sig = None, None

class datoPolinomio(object):

    def __init__(self, valor, termino):
        self.valor = valor
        self.termino = termino

class Polinomio(object):

    def __init__(self):
        self.termino_mayor = None
        self.grado = -1
    
    def agregar_termino(polinomio, termino, valor):
        aux = Nodo()
        dato = datoPolinomio(valor, termino)
        aux.info = dato
        if(termino > polinomio.grado):
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = termino
        else:
            actual = polinomio.termino_mayor
            while(actual.sig is not None and termino < actual.sig.info.termino):
                actual = actual.sig
            aux.sig = actual.sig
            actual.sig = aux
    def obtener_valor(polinomio, termino):
        aux = polinomio.termino_mayor
        while(aux is not None and aux.info.termino > termino):
            aux = aux.sig
        if(aux is not None and aux.info.termino == termino):
            return aux.info.valor
        else:
            return 0

    def restar(polinomio1, polinomio2):
        aux = Polinomio()
        menor = polinomio1 if (polinomio1.grado < polinomio2.grado) else polinomio2
        for i in range(0, menor.grado+1):
            total = Polinomio.obtener_valor(polinomio2, i) - Polinomio.obtener_valorobtener_valor(polinomio1, i)
            if (total != 0):
                Polinomio.agregar_termino(aux, i, total)

A =  Polinomio()
Polinomio1 = A.agregar_termino(2, 3)
Polinomio2= A.agregar_termino(4, 5)
restar_polinomio = A.restar(Polinomio2, Polinomio1)
print(restar_polinomio)