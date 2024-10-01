from cola import Queue
personajes_mcu = [
    {"nombre_personaje": "Tony Stark", "nombre_superheroe": "Iron Man", "genero": "M"},
    {"nombre_personaje": "Steve Rogers", "nombre_superheroe": "Capitán América", "genero": "M"},
    {"nombre_personaje": "Natasha Romanoff", "nombre_superheroe": "Black Widow", "genero": "F"},
    {"nombre_personaje": "Thor Odinson", "nombre_superheroe": "Thor", "genero": "M"},
    {"nombre_personaje": "Bruce Banner", "nombre_superheroe": "Hulk", "genero": "M"},
    {"nombre_personaje": "Wanda Maximoff", "nombre_superheroe": "Scarlet Witch", "genero": "F"},
    {"nombre_personaje": "Peter Parker", "nombre_superheroe": "Spider-Man", "genero": "M"},
    {"nombre_personaje": "Carol Danvers", "nombre_superheroe": "Captain Marvel", "genero": "F"},
    {"nombre_personaje": "T'Challa", "nombre_superheroe": "Black Panther", "genero": "M"},
    {"nombre_personaje": "Gamora", "nombre_superheroe": "Gamora", "genero": "F"},
    {"nombre_personaje":"Scott Lang","nombre_superheroe":"Ant-Man","genero":"M"}
]
cola = Queue()
cola_aux = Queue()
list_femenino = []
lista_masculino = []
lista_letras = []
for char in personajes_mcu:
    cola.arrive(char)
for i in range(cola.size()):
    aux = cola.attention()
    #punto a
    if aux["nombre_superheroe"] == "Captain Marvel":
        print("el nombre de la capitana marvel es: ",aux["nombre_personaje"])
    #punto b
    if aux["genero"] == "F" :
        list_femenino.append(aux)
    #punto c
    if aux["genero"] == "M":
        lista_masculino.append(aux)
    #punto d
    if aux["nombre_personaje"]== "Scott Lang":
        print("el nombre de superheroe de Scott Lang: ", aux["nombre_superheroe"])
    #punto e
    if aux["nombre_personaje"].startswith("S") == True:
        lista_letras.append(aux)
    #punto f
    if aux["nombre_personaje"]== "Carol Danvers":
        print("el nombre de superheroe de Carol Danvers es: ",aux["nombre_superheroe"])
    cola_aux.arrive(aux)
for i in range(cola_aux.size()):
    cola.arrive(cola_aux.attention())

print("personajes feminos: ",list_femenino)
print("personajes masculinos : ",lista_masculino)
print("personajes que empiezan con S: ", lista_letras)



    
    
        

