from pila import Stack
from cola import Queue
from random import randint
cola_char = Queue()
pila = Stack()
for i in range(10):
    letra = chr(randint(65,90))
    cola_char.arrive(letra)


for i in range (cola_char.size()):
    print(cola_char.on_front())
    pila.push(cola_char.attention())
print()
print()
print()
for i in range(pila.size()):
    pop = pila.pop()
    cola_char.arrive(pop)
for i in range(cola_char.size()):
    print(cola_char.on_front())
    cola_char.move_to_end()