#Para realizar el for in range hay que tener en cuenta que coje hasta el penúlimo elemento por eso hay que añar un +1
def numero_impares(numero):
    cont_imp = 0
    for i in range(1, numero+1):
        if (i%2 == 0):
            print(i, "Es par")
        else:
            print(i, "Es impar")
            cont_imp+=1
    print("Cantidad de números impares", cont_imp)
    return cont_imp

var = numero_impares(5)
