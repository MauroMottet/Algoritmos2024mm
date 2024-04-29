from pila import Stack
from random import randint
pila = Stack()
pila_aux = Stack()
for i in range(5):
    num = randint(1,99)
    print(num)
    pila.push(num)
arem = int(input("que numero desea remplazar?: "))
remplazo= int(input("por que numero desea remplazarlo: "))
while pila.size() > 0:
    data = pila.pop()
    pila_aux.push(data)
while pila_aux.size() > 0:
    data2 = pila_aux.pop()
    if data2 == arem:
        pila.push(remplazo)
        print(remplazo)
    else:
        pila.push(data2)
        print(data2)

    