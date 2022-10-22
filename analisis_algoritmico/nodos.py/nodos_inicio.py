
class Nodo(object):
    info, sig = None, None

    def __str__(self):
        return self.info
        
    
aux = Nodo()
aux.info = "Primer nodo"
palabra = input("Ingrese una palabra: ")
naux = aux
while (palabra != ""):
    nodo = Nodo()
    nodo.info = palabra
    naux.sig = nodo
    naux = nodo
    palabra = input("Ingrese una palabra: ")
while (aux is not None):
    print(aux.info)
    aux = aux.sig

lista = []
for i in range(2):
    nodo = Nodo()
    palabra = input("Ingrese una palabra: ")
    nodo.info = palabra
    lista.append(nodo)

for i in lista:
    print(i)
