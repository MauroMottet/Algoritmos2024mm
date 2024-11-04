from arbol_avl import BinaryTree
pokemons = [
    {"name": "Bulbasaur", "number": 1, "type": ["planta", "veneno"]},
    {"name": "Ivysaur", "number": 2, "type": ["planta", "veneno"]},
    {"name": "Charmander", "number": 4, "type": ["fuego"]},
    {"name": "Squirtle", "number": 7, "type": ["agua"]},
    {"name": "Pikachu", "number": 25, "type": ["eléctrico"]},
    {"name": "Jolteon", "number": 135, "type": ["eléctrico"]},
    {"name": "Lycanroc", "number": 745, "type": ["roca"]},
    {"name": "Tyrantrum", "number": 697, "type": ["roca", "dragón"]},
]
tree_nombre = BinaryTree()
tree_numero = BinaryTree()
tree_tipo = BinaryTree()
for pokemon in pokemons:
    tree_nombre.insert_node(pokemon["name"], pokemon)
    tree_numero.insert_node(pokemon["number"],pokemon)
    for pokemontipo in pokemon['type']:
        node = tree_tipo.search(pokemontipo)
        if node:
            node.other_value.append(pokemon)
        else:
            tree_tipo.insert_node(pokemontipo, [pokemon])
#mostrar datos pokemon x numero
resultado = tree_numero.search(int(input("ingrese el numero de su pokemon")))
if resultado:
    print(resultado.other_value)
else:
    print("no se encontro el pokemon")
#proximidad de nombre
nombre_buscar= input("ingrese el nombre del pokemon a buscar")
print(f"Búsqueda por proximidad con '{nombre_buscar}':")
tree_nombre.proximity_search(nombre_buscar)
#mostrar todos los pokemons de un determinado tipo
tipo = input("ingrese el tipo de pokemon: ")
print(f"Búsqueda por proximidad con '{tipo}':")
tree_tipo.proximity_search(tipo)
#listado ascendente por numero y nombre
tree_numero.inorden()
tree_nombre.inorden()
#mostrar pokemons por nivel
tree_nombre.by_level()
#mostrar los datos de jolteon , lycanroc y Tyrantrum
nombres= ["Jolteon", "Lycanroc","Tyrantrum"]
for nombre in nombres:
    resultado = tree_nombre.search(nombre)
    if resultado:
        print(resultado.other_value)
    else:
        print(f"{nombre}no fue encontrado")
tipo_a_buscar = input("ingrese el tipo de pokemon que desea buscar: ")
nodo = tree_tipo.search(tipo_a_buscar)
if nodo and nodo.other_value:
    contador = len(nodo.other_value)
else:
    contador = 0
print(f"Total de Pokémon de tipo {tipo_a_buscar}: {contador}")