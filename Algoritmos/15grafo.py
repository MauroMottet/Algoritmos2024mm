from grafo import Graph
maravillas = [
    {"nombre": "Gran Muralla China", "pais": ["China"], "tipo": "arquitectonica"},
    {"nombre": "Petra", "pais": ["Jordania"], "tipo": "arquitectonica"},
    {"nombre": "Cristo Redentor", "pais": ["Brasil"], "tipo": "arquitectonica"},
    {"nombre": "Machu Picchu", "pais": ["Perú"], "tipo": "arquitectonica"},
    {"nombre": "Chichen Itza", "pais": ["México"], "tipo": "arquitectonica"},
    {"nombre": "Coliseo Romano", "pais": ["Italia"], "tipo": "arquitectonica"},
    {"nombre": "Taj Mahal", "pais": ["India"], "tipo": "arquitectonica"},
    {"nombre": "Amazonas", "pais": ["Brasil", "Perú", "Colombia", "Venezuela"], "tipo": "natural"},
    {"nombre": "Bahía de Ha Long", "pais": ["Vietnam"], "tipo": "natural"},
    {"nombre": "Cataratas del Iguazú", "pais": ["Argentina", "Brasil"], "tipo": "natural"},
    {"nombre": "Isla Jeju", "pais": ["Corea del Sur"], "tipo": "natural"},
    {"nombre": "Komodo", "pais": ["Indonesia"], "tipo": "natural"},
    {"nombre": "Río subterráneo de Puerto Princesa", "pais": ["Filipinas"], "tipo": "natural"},
    {"nombre": "Montaña de la Mesa", "pais": ["Sudáfrica"], "tipo": "natural"}
]
distancias_arquitectonicas = {
    ("Gran Muralla China", "Petra"): 6000,
    ("Gran Muralla China", "Cristo Redentor"): 17500,
    ("Gran Muralla China", "Machu Picchu"): 17100,
    ("Gran Muralla China", "Chichen Itza"): 12500,
    ("Gran Muralla China", "Coliseo Romano"): 8100,
    ("Gran Muralla China", "Taj Mahal"): 4200,
    ("Petra", "Cristo Redentor"): 12000,
    ("Petra", "Machu Picchu"): 11700,
    ("Petra", "Chichen Itza"): 12000,
    ("Petra", "Coliseo Romano"): 2300,
    ("Petra", "Taj Mahal"): 4000,
    ("Cristo Redentor", "Machu Picchu"): 3300,
    ("Cristo Redentor", "Chichen Itza"): 6600,
    ("Cristo Redentor", "Coliseo Romano"): 9500,
    ("Cristo Redentor", "Taj Mahal"): 14500,
    ("Machu Picchu", "Chichen Itza"): 4100,
    ("Machu Picchu", "Coliseo Romano"): 10500,
    ("Machu Picchu", "Taj Mahal"): 17000,
    ("Chichen Itza", "Coliseo Romano"): 9600,
    ("Chichen Itza", "Taj Mahal"): 14800,
    ("Coliseo Romano", "Taj Mahal"): 5700
}
distancias_naturales = {
    ("Amazonas", "Bahía de Ha Long"): 19000,
    ("Amazonas", "Cataratas del Iguazú"): 3000,
    ("Amazonas", "Isla Jeju"): 15500,
    ("Amazonas", "Komodo"): 17700,
    ("Amazonas", "Río subterráneo de Puerto Princesa"): 18300,
    ("Amazonas", "Montaña de la Mesa"): 7800,
    ("Bahía de Ha Long", "Cataratas del Iguazú"): 17600,
    ("Bahía de Ha Long", "Isla Jeju"): 3000,
    ("Bahía de Ha Long", "Komodo"): 4600,
    ("Bahía de Ha Long", "Río subterráneo de Puerto Princesa"): 1600,
    ("Bahía de Ha Long", "Montaña de la Mesa"): 12000,
    ("Cataratas del Iguazú", "Isla Jeju"): 18200,
    ("Cataratas del Iguazú", "Komodo"): 17500,
    ("Cataratas del Iguazú", "Río subterráneo de Puerto Princesa"): 19300,
    ("Cataratas del Iguazú", "Montaña de la Mesa"): 7800,
    ("Isla Jeju", "Komodo"): 4100,
    ("Isla Jeju", "Río subterráneo de Puerto Princesa"): 1800,
    ("Isla Jeju", "Montaña de la Mesa"): 13300,
    ("Komodo", "Río subterráneo de Puerto Princesa"): 2300,
    ("Komodo", "Montaña de la Mesa"): 12000,
    ("Río subterráneo de Puerto Princesa", "Montaña de la Mesa"): 12900
}
grafo = Graph(dirigido=False)
for maravilla in maravillas:
    grafo.insert_vertice(maravilla["nombre"])
for (origen, destino), distancia in distancias_arquitectonicas.items():
    grafo.insert_arista(origen, destino, distancia)
for (origen, destino), distancia in distancias_naturales.items():
    grafo.insert_arista(origen, destino, distancia)  
bosque_minimo_arquitectonicas = grafo.kruskal("Gran Muralla China")
bosque_minimo_naturales = grafo.kruskal("Amazonas")
total_cable_arquitectonicas = sum(
    int(arista.split('-')[-1]) for arbol in bosque_minimo_arquitectonicas for arista in arbol.split(';') if '-' in arista
)  
total_cable_naturales = sum(
    int(arista.split('-')[-1]) for arbol in bosque_minimo_naturales for arista in arbol.split(';') if '-' in arista
)
print("Árbol de expansión mínima (Arquitectónicas):", bosque_minimo_arquitectonicas)
print(f"Longitud total de cables para maravillas arquitectónicas: {total_cable_arquitectonicas} km")
print("Árbol de expansión mínima (Naturales):", bosque_minimo_naturales)
print(f"Longitud total de cables para maravillas naturales: {total_cable_naturales} km")
paises_tipos = {}
for maravilla in maravillas:
    for pais in maravilla["pais"]:
        if pais not in paises_tipos:
            paises_tipos[pais] = set()
        paises_tipos[pais].add(maravilla["tipo"])
paises_con_ambos_tipos = [pais for pais, tipos in paises_tipos.items() if len(tipos) > 1]
print("Países con maravillas arquitectónicas y naturales:", paises_con_ambos_tipos)
paises_maravillas = {}
for maravilla in maravillas:
    for pais in maravilla["pais"]:
        if pais not in paises_maravillas:
            paises_maravillas[pais] = {"arquitectonica": 0, "natural": 0}
        paises_maravillas[pais][maravilla["tipo"]] += 1
paises_con_multiples_maravillas_mismo_tipo = {
    pais: tipo for pais, tipo_cantidad in paises_maravillas.items() for tipo, cantidad in tipo_cantidad.items() if cantidad > 1
}
print("Países con múltiples maravillas del mismo tipo:", paises_con_multiples_maravillas_mismo_tipo)
