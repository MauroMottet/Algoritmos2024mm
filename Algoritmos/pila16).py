from pila import Stack
def intersección (pila1,pila2):
    list1=[]
    list2=[]
    while pila1.size() > 0:
        list1.append(pila1.pop())
    while pila2.size() > 0:
        list2.append(pila2.pop())
    for element in reversed(list1):
        pila1.push(element)
    for element in reversed(list2):
        pila2.push(element)
    intersección_pilas = list(set(list1) & set(list2))
    #no sabia bien como hacerlo asi que busque en internet una ayuda para como encontrar las intersecciónes
    return intersección_pilas

episode_v_characters = ["Luke Skywalker", "Darth Vader", "Leia Organa", "Han Solo", "Chewbacca", "Yoda"]
episode_vii_characters = ["Rey", "Finn", "Kylo Ren", "Leia Organa", "Han Solo", "Chewbacca", "Luke Skywalker"]
pila_ep_v = Stack()
pila_ep_vii = Stack()
for personajes in episode_v_characters:
    pila_ep_v.push(personajes)
for personajes in episode_vii_characters:
    pila_ep_vii.push(personajes)
personajes_en_comun = intersección(pila_ep_v,pila_ep_vii)
print("Los personajes en comun entre ambos episodios son: ", personajes_en_comun)
