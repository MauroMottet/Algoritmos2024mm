#Formula Lista[1:] + [Lista[0]] si la lista no esta vacia se llama recursivamente
#con la lista que excluye el primer elemento (Lista[1:]) despues concatena el primer
#elemento de la lista original (lista[0]) al final de la llamada recursiva
def invertir(lista):
    #si la lista esta vacia
    if not lista:
        return []
    else:
        return invertir(lista[1:]) + [lista[0]]
lista = [1,2,3,4,5,6,7,8,9,10]
lista_invertida = invertir(lista)
print(lista)
print(lista_invertida)