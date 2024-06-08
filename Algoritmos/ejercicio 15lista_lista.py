from random import choice
from lista import search , by_name , show_list_list
trainers =[
    {"nombre":"Ash","Ligas":1,"BP":43,"BG":160},
    {"nombre":"Misty","Ligas":0,"BP":39,"BG":23},
    {"nombre":"Brook","Ligas":0,"BP":64,"BG":2},
    {"nombre":"Cynthia","Ligas":4,"BP":1,"BG":400},
    {"nombre":"Rinmei","Ligas":4,"BP":4,"BG":270},
    {"nombre":"Serena","Ligas":0,"BP":4,"BG":16}
]
names = ["Serena","Rinmei","Cynthia","Brook","Misty","Ash"]
lista_entrenadores = []
pokemons=[
    {"nombre":"Gardevoird","Nivel": 90,"Tipo":"Psiquico","Subtipo":"Hada"},
    {"nombre":"Ponyta","Nivel": 90,"Tipo":"Fuego","Subtipo":None},
    {"nombre":"Metapod","Nivel": 16,"Tipo":"Bicho","Subtipo":None},
    {"nombre":"Gyarados","Nivel": 96,"Tipo":"Agua/Dragon","Subtipo":"Dragon"},
    {"nombre":"Charizard","Nivel": 79,"Tipo":"Fuego/Volador","Subtipo":"Volador"},
    {"nombre":"Wingull","Nivel": 20,"Tipo":"Agua/Volador","Subtipo":"Volador"},
    {"nombre":"Terrakion","Nivel": 76,"Tipo":"Roca/Lucha","Subtipo":"Lucha"},
    {"nombre":"Tyrantrum","Nivel": 90,"Tipo":"Roca/Dragon","Subtipo":"Dragon"},
    {"nombre":"Garchomp","Nivel": 120,"Tipo":"Dragon/Tierra","Subtipo":"Tierra"},
    {"nombre":"Pikachu","Nivel": 100,"Tipo":"Electrico","Subtipo":None},
    {"nombre":"Pidgeot","Nivel": 48,"Tipo":"Normal","Subtipo":"Volador"},
    {"nombre":"Blastoise","Nivel": 60,"Tipo":"Agua","Subtipo":None},
]
for trainer in trainers :
    trainer.update({'sublist': []})
    lista_entrenadores.append(trainer)
for pokemon in pokemons:
    pos = search(lista_entrenadores, "nombre", choice(names))
    if pos is not None:
        lista_entrenadores[pos]["sublist"].append(pokemon)
lista_entrenadores.sort(key=by_name)
show_list_list("Entrenadores y sus Pokémons", "Pokémons", lista_entrenadores)
#a
def cantidad_pokemons(entrenadores, nombre_entrenador):
    pos = search(entrenadores, 'nombre', nombre_entrenador)
    if pos is not None:
        return len(entrenadores[pos]['sublist'])
    return 0
print("Cantidad de Pokémons de Ash:", cantidad_pokemons(lista_entrenadores, "Ash"))
#b
def entrenadores_mas_de_tres_torneos(entrenadores):
    return [entrenador['nombre'] for entrenador in entrenadores if entrenador['Ligas'] > 3]
print("Entrenadores con más de tres torneos ganados:", entrenadores_mas_de_tres_torneos(lista_entrenadores))
#c
def pokemon_mayor_nivel_mejor_entrenador(entrenadores):
    mejor_entrenador = max(entrenadores, key=lambda x: x['Ligas'])
    return max(mejor_entrenador['sublist'], key=lambda x: x['Nivel'], default=None)
print("Pokémon de mayor nivel del entrenador con más torneos ganados:", pokemon_mayor_nivel_mejor_entrenador(lista_entrenadores))
#d
def mostrar_datos_entrenador(entrenadores, nombre_entrenador):
    pos = search(entrenadores, 'nombre', nombre_entrenador)
    if pos is not None:
        entrenador = entrenadores[pos]
        print(f"Entrenador: {entrenador['nombre']}")
        print(f"Ligas: {entrenador['Ligas']}")
        print(f"Batallas Perdidas: {entrenador['BP']}")
        print(f"Batallas Ganadas: {entrenador['BG']}")
        print("Pokémons:")
        for pokemon in entrenador['sublist']:
            print(f"  Nombre: {pokemon['nombre']}, Nivel: {pokemon['Nivel']}, Tipo: {pokemon['Tipo']}, Subtipo: {pokemon['Subtipo']}")
    else:
        print(f"Entrenador {nombre_entrenador} no encontrado.")
print("Datos del entrenador Ash y sus Pokémons:")
mostrar_datos_entrenador(lista_entrenadores, "Ash")
#e
def entrenadores_porcentaje_victorias_mayor_79(entrenadores):
    return [entrenador['nombre'] for entrenador in entrenadores if (entrenador['BG'] / (entrenador['BG'] + entrenador['BP'])) > 0.79]
print("Entrenadores con porcentaje de victorias mayor al 79%:", entrenadores_porcentaje_victorias_mayor_79(lista_entrenadores))
#f
def entrenadores_con_pokemons_especiales(entrenadores):
    especiales = []
    for entrenador in entrenadores:
        for pokemon in entrenador['sublist']:
            if (pokemon['Tipo'] == 'Fuego' and pokemon['Subtipo'] == 'Planta') or (pokemon['Tipo'] == 'Agua' and pokemon['Subtipo'] == 'Volador'):
                especiales.append(entrenador['nombre'])
                break
    return especiales
print("Entrenadores con Pokémons de tipo fuego/planta o agua/volador:", entrenadores_con_pokemons_especiales(lista_entrenadores))
#g
def promedio_nivel_pokemons(entrenadores, nombre_entrenador):
    pos = search(entrenadores, 'nombre', nombre_entrenador)
    if pos is not None:
        pokemons = entrenadores[pos]['sublist']
        if pokemons:
            return sum(pokemon['Nivel'] for pokemon in pokemons) / len(pokemons)
    return 0
print("Promedio de nivel de los Pokémons de Ash:", promedio_nivel_pokemons(lista_entrenadores, "Ash"))
#h
def entrenadores_con_pokemon(entrenadores, nombre_pokemon):
    return sum(1 for entrenador in entrenadores if any(pokemon['nombre'] == nombre_pokemon for pokemon in entrenador['sublist']))
print("Cantidad de entrenadores que tienen a Pikachu:", entrenadores_con_pokemon(lista_entrenadores, "Pikachu"))
#i
def entrenadores_con_pokemons_repetidos(entrenadores):
    repetidos = []
    for entrenador in entrenadores:
        nombres_pokemons = [pokemon['nombre'] for pokemon in entrenador['sublist']]
        if len(nombres_pokemons) != len(set(nombres_pokemons)):
            repetidos.append(entrenador['nombre'])
    return repetidos
print("Entrenadores con Pokémons repetidos:", entrenadores_con_pokemons_repetidos(lista_entrenadores))
#j
def entrenadores_con_pokemons_especificos(entrenadores):
    pokemons_especificos = {"Tyrantrum", "Terrakion", "Wingull"}
    return [entrenador['nombre'] for entrenador in entrenadores if any(pokemon['nombre'] in pokemons_especificos for pokemon in entrenador['sublist'])]
print("Entrenadores con Tyrantrum, Terrakion o Wingull:", entrenadores_con_pokemons_especificos(lista_entrenadores))
#k
def entrenador_tiene_pokemon(entrenadores, nombre_entrenador, nombre_pokemon):
    pos = search(entrenadores, 'nombre', nombre_entrenador)
    if pos is not None:
        entrenador = entrenadores[pos]
        for pokemon in entrenador['sublist']:
            if pokemon['nombre'] == nombre_pokemon:
                print(f"Entrenador: {entrenador['nombre']}")
                print(f"Ligas: {entrenador['Ligas']}")
                print(f"Batallas Perdidas: {entrenador['BP']}")
                print(f"Batallas Ganadas: {entrenador['BG']}")
                print("Pokémon:")
                print(f"  Nombre: {pokemon['nombre']}, Nivel: {pokemon['Nivel']}, Tipo: {pokemon['Tipo']}, Subtipo: {pokemon['Subtipo']}")
                return True
    print(f"El entrenador {nombre_entrenador} no tiene al Pokémon {nombre_pokemon}.")
    return False
print("¿Ash tiene a Pikachu?:")
entrenador_tiene_pokemon(lista_entrenadores, "Ash", "Pikachu")