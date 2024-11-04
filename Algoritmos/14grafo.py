from grafo import Graph
grafo = Graph(False)
ambientes = ["Cocina", "Comedor", "Cochera", "Quincho", "Baño 1", "Baño 2", 
             "Habitación 1", "Habitación 2", "Sala de estar", "Terraza", "Patio"]
aristas = [
    ("Cocina", "Comedor", 4), ("Cocina", "Baño 1", 3), ("Cocina", "Habitación 1", 7),
    ("Comedor", "Sala de estar", 6), ("Comedor", "Terraza", 5), ("Comedor", "Cochera", 8),
    ("Cochera", "Patio", 10), ("Cochera", "Quincho", 12), ("Cochera", "Habitación 1", 9),
    ("Quincho", "Patio", 7), ("Quincho", "Terraza", 11),
    ("Baño 1", "Baño 2", 2), ("Baño 1", "Habitación 2", 5),
    ("Baño 2", "Habitación 1", 6), ("Baño 2", "Habitación 2", 3),
    ("Habitación 1", "Habitación 2", 4), ("Habitación 1", "Sala de estar", 8),
    ("Sala de estar", "Terraza", 9), ("Terraza", "Patio", 4),
]
#a
for ambiente in ambientes:
    grafo.insert_vertice(ambiente)
#b
for origen , destino , peso in aristas:
    grafo.insert_arista(origen , destino , peso)
#c
bosque_minimo = grafo.kruskal("Cocina")
total_cable =(sum([int(arista.split('-')[-1]) for arbol in bosque_minimo for arista in arbol.split(';') if '-' in arista]))
print("Árbol de expansión mínima (Kruskal):", bosque_minimo)
print(f"Longitud total de cables necesaria para conectar todos los ambientes: {total_cable} metros")
#d
camino_minimo = grafo.dijkstra("Habitación 1")
camino = []
distancia_total = None
while camino_minimo.size() > 0:
    paso = camino_minimo.pop()
    camino.append(paso)
camino_final = []
for paso in camino:
    if paso[1][0] == "Sala de estar":  # Buscar la sala de estar en el camino
        distancia_total = paso[0]
        while paso:
            camino_final.insert(0, paso[1][0])  # Insertar al inicio para tener el orden correcto
            paso = next((p for p in camino if p[1][0] == paso[1][2]), None)
        break
camino_final_nombres = [paso[1][0] for paso in camino_final]
print("Camino más corto de 'Habitación 1' a 'Sala de estar':", " -> ".join(camino_final_nombres))
print(f"Longitud del cable de red necesario para conectar el router con el Smart TV: {distancia_total} metros")
