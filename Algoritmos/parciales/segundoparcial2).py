from grafo import Graph
starwars_grafo = Graph(dirigido=False)
#vertices
starwars_grafo.insert_vertice("Yoda")
starwars_grafo.insert_vertice("Luke Skywalker")
starwars_grafo.insert_vertice("Darth Vader")
starwars_grafo.insert_vertice("Leia Organa")
#aristas
starwars_grafo.insert_arista("Yoda","Luke Skywalker",3)
starwars_grafo.insert_arista("Yoda","Darth Vader",1)
starwars_grafo.insert_arista("Luke Skywalker","Leia Organa",5)
#mostrar grafo
starwars_grafo.show_graph()
#arbol expansión minimo y si incluye a yoda
bosque = starwars_grafo.kruskal("Yoda")
contiene_a_yoda = False
for arbol in bosque:
    if "Yoda" in arbol:
        contiene_a_yoda = True
        break
print("Arbol de expansión de minimo: ")
print(bosque)
if contiene_a_yoda == False:
    print("el arbol de expansión minimo no contiene a yoda")
else:
    print("el arbol de expansión minimo  contiene a yoda")
#arista con el peso maximo 
maxep = 0
personaje = None
for nodo in starwars_grafo.elements:
    for arista in nodo["aristas"]:
        if arista["peso"] > maxep:
            maxep = arista["peso"]
            personaje = (nodo["value"],arista["value"])
print(f"Los personajes que más episodios comparten son {personaje[0]} y {personaje[1]} con {maxep} episodios.")
#CARGAR LOS PERSONAJES SOLICITADOS EN EL PUNTO D
starwars_grafo.insert_vertice("Boba Fett")
starwars_grafo.insert_vertice("C-3PO")
starwars_grafo.insert_vertice("Rey")
starwars_grafo.insert_vertice("Kylo Ren")
starwars_grafo.insert_vertice("Chewbacca")
starwars_grafo.insert_vertice("Han Solo")
starwars_grafo.insert_vertice("R2-D2")
starwars_grafo.insert_vertice("BB-8")