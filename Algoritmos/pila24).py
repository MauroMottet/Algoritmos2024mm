from pila import Stack
mcu_characters = [
    ("Iron Man", 10), ("Captain America", 9), ("Thor", 8), ("Hulk", 7),
    ("Black Widow", 8), ("Hawkeye", 5), ("Groot", 5), ("Rocket Raccoon", 6),
    ("Doctor Strange", 4), ("Black Panther", 3), ("Spider-Man", 5),
    ("Scarlet Witch", 4), ("Ant-Man", 3), ("Vision", 3), ("Falcon", 3)
]
pila_mcu = Stack()
for personaje in mcu_characters:
    pila_mcu.push(personaje)
posicion_groot = -1
posicion_rocket = -1
posicion_actual = 1
pila_temporal = Stack()
while pila_mcu.size() > 0:
    personaje = pila_mcu.pop()
    pila_temporal.push(personaje)
    if personaje[0] == "Rocket Raccoon":
        posicion_rocket = posicion_actual
    if personaje[0] == "Groot":
        posicion_groot = posicion_actual
    posicion_actual += 1
while pila_temporal.size() > 0:
    pila_mcu.push(pila_temporal.pop())
print("La posicion de Rocket es: ", posicion_rocket)
print("La posicion de Groot es: ", posicion_groot)
mas_de_5 = []
while pila_mcu.size() > 0:
    personaje = pila_mcu.pop()
    pila_temporal.push(personaje)
    if personaje[1] > 5:
        mas_de_5.append(personaje)
while pila_temporal.size() > 0:
    pila_mcu.push(pila_temporal.pop())
print("Los personajes con mas de 5 peliculas son: ",mas_de_5)
black_widow_peliculas = 0
while pila_mcu.size() > 0:
    personaje = pila_mcu.pop()
    pila_temporal.push(personaje)
    if personaje[0] == "Black Widow":
        black_widow_peliculas= personaje[1]
while pila_temporal.size() > 0:
    pila_mcu.push(pila_temporal.pop())
print("Las pelis en las que participio Black Widow son: ", black_widow_peliculas)
personajescdg = []
while pila_mcu.size() > 0:
    personaje = pila_mcu.pop()
    pila_temporal.push(personaje)
    if personaje[0][0] in "CDG":
        personajescdg.append(personaje[0])
while pila_temporal.size() > 0:
    pila_mcu.push(pila_temporal.pop())
print("Los personajes que empiezan con C , D Y G son: ",personajescdg)