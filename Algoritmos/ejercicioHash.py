tabla_tipo = {}
tabla_numero = [[]for _ in range (10)]
tabla_nivel = [[] for _ in range(10)]
def hash_tipo(tipo):
    return tipo.lower()
def hash_numero(numero):
    return numero % 10
def hash_nivel(nivel):
    return nivel % 10
def insertar_pokemon(numero, nombre, tipos, nivel):
    for tipo in tipos:
        key_tipo = hash_tipo(tipo)
        if key_tipo not in tabla_tipo:
            tabla_tipo[key_tipo] = []
        tabla_tipo[key_tipo].append((numero, nombre, tipos, nivel))
    key_numero = hash_numero(numero)
    tabla_numero[key_numero].append((numero, nombre, tipos, nivel))
    key_nivel = hash_nivel(nivel)
    tabla_nivel[key_nivel].append((numero, nombre, tipos, nivel))
def mostrar_pokemon_numero(tabla , digitos):
    resultado = []
    for digito in digitos:
        resultado.extend(tabla[digito])
    return resultado 
def mostrar_pokemon_nivel(tabla, multiples):
    resultado = []
    for i in range(10):
        if any(i % multiple == 0 for multiple in multiples):
            resultado.extend(tabla[i])
    return resultado
def mostrar_pokemon_tipo (tabla , tipos):
    resultado = []
    for tipo in tipos:
        key_tipo = hash_tipo(tipo)
        if key_tipo in tabla:
            resultado.extend(tabla[key_tipo])
    return resultado
insertar_pokemon(349,"Garchomp",["Dragon","Tierra"],30)
insertar_pokemon(49,"Charizard",["Fuego","Volador"],10)
insertar_pokemon(10,"Pidgey",["Volador"],28)
insertar_pokemon(2,"Squiertle",["Agua"],38)
insertar_pokemon(123, "Scyther", ["Bicho", "Volador"], 30)
insertar_pokemon(4, "Charmander", ["Fuego"], 10)
insertar_pokemon(25, "Pikachu", ["Eléctrico"], 15)
insertar_pokemon(150, "Mewtwo", ["Psíquico"], 100)
insertar_pokemon(7, "Squirtle", ["Agua"], 5)
insertar_pokemon(9, "Blastoise", ["Agua"], 35)
insertar_pokemon(8, "Wartortle", ["Agua"], 25)

print("Pokemons que terminan en 3, 7 y 9:")
for pokemon in mostrar_pokemon_numero(tabla_numero,[3, 7, 9]):
    print(pokemon)
print("Pokemon por nivel que son multiplo de 2 ,5 y 10:")
for pokemon in mostrar_pokemon_nivel(tabla_nivel, [2 , 5 , 10]):
    print(pokemon)
print("Pokemon de tipo acero, fuego , hielo , electrico , hielo")
for pokemon in mostrar_pokemon_tipo(tabla_tipo,["Acero","Fuego","Electrico","Hielo"]):
    print(pokemon)

