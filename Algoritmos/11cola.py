from cola import Queue
pj = [{"name": "Luke Skywalker", "planet": "Tatooine"},
      {"name": "Anakin Skywalker" , "planet": "Tatooine"},
      {"name": "Leia Organa", "planet":"Alderaan"},
      {"name": "Yoda","planet":"Dagobah"},
      {"name": "Han solo", "planet": "Corellia"},
      {"name": "Jar Jar Binks", "planet":"Naboo"},
      {"name": "Padme Amidala", "planet": "Naboo"}]
personajes = Queue()
queue_aux = Queue()
lista_planetas = []
for personaje in pj:
    personajes.arrive(personaje)
#PUNTO A y B
for i in range(personajes.size()):
    aux = personajes.attention()
    if aux["name"] in ["Luke Skywalker"]:
        print("Planteas de luke : ",aux["planet"])
    if aux["name"] in ["Han solo"]:
        print("Planeta de Han Solo: ",aux["planet"])
    if aux["planet"] in ["Alderaan", "Endor","Tatooine"]:
        print(aux)
    queue_aux.arrive(aux)
for i in range(queue_aux.size()):
    a = queue_aux.attention()
    personajes.arrive(a)
#punto c 
nuevo_personaje = {"name": "Ahsoka Tano", "planet": "Shili"}
cola_aux = Queue()
insertado = False
for i in range(personajes.size()):
    personaje_actual = personajes.attention() 
    if personaje_actual["name"] == "Yoda" and not insertado:
        cola_aux.arrive(nuevo_personaje)  
        insertado = True
    cola_aux.arrive(personaje_actual)
for i in range(cola_aux.size()):
    personajes.arrive(cola_aux.attention())
#Punto D
cola_aux = Queue()
saltar_siguiente = False
for i in range(personajes.size()):
    personaje_actual = personajes.attention()  
    if saltar_siguiente:
        saltar_siguiente = False  
        continue
    if personaje_actual["name"] == "Jar Jar Binks":
        saltar_siguiente = True

    cola_aux.arrive(personaje_actual)  
for i in range(cola_aux.size()):
    personajes.arrive(cola_aux.attention())
print("Lista final de personajes en la cola:")
for i in range(personajes.size()):
    print(personajes.attention())
