def raiz(numero,valor=1):
    if numero == 0 or numero == 1:
        return numero
    elif valor**2 > numero :
         return valor -1 
    else:
        return raiz(numero,valor+1)
print(raiz(4))