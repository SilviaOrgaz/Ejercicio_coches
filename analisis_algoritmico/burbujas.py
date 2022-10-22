def burbuja_mejorado(lista):
    i=0
    control = True
    #while(i <= len(lista)-2) and control:
    while control:
        control = False
        for j in range(0, len(lista)-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1]= lista[j+1], lista[j]
                control = True
        i+=1
        print(i)
    return lista

print(burbuja_mejorado([20, 40, 80, 100, 90]))
