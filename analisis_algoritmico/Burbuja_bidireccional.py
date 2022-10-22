def coctel(lista):
    izquierda = 0
    derecha = len(lista)-1
    control = True
    while (izquierda < derecha) and control:
        control = False
        for i in range(izquierda, derecha):
            if(lista[i] > lista[i+1]):
                control = True
                lista[i], lista[i+1] = lista[i+1], lista[i]
        print("buble uno",lista)
        #El último elemto ya esta colocado
        derecha -=1
        # -1 porque va para atrás
        for j in range(derecha, izquierda, -1):
            if(lista[j] < lista[j-1]):
                control = True
                lista[j], lista[j-1] = lista[j-1], lista[j]
        print("bucle dos", lista)
        izquierda +=1
    return lista
print(coctel([100, 90, 40, 10]))