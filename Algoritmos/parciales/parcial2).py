from pila import Stack
dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": "7000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": "6000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": "15 kg",
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": "56000 kg",
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": "5000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": "10000 kg",
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": "2000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": "23000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": "15000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": "6000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": "2500 kg",
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": "1500 kg",
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": "2700 kg",
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": "5000 kg",
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": "25 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": "200 kg",
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": "450 kg",
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": "15000 kg",
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },

  ]
dinosaurios_pila = Stack()
for dinosaurio in dinosaurios:
    dinosaurios_pila.push(dinosaurio)
def especies(pila):
    especies = []
    pila_aux = Stack()
    while pila.size() > 0:
        dino = pila.pop()
        if dino["especie"] not in especies:
            especies.append(dino["especie"])
        pila_aux.push(dino)
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    return len(especies)
def descubridores(pila):
    descubridores = []
    pila_aux = Stack()
    while pila.size() > 0:
        dino = pila.pop()
        if dino["descubridor"] not in descubridores:
            descubridores.append(dino["descubridor"])
        pila_aux.push(dino)
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    return len(descubridores)
def dinosauriosT(pila):
    resultado = []
    pila_aux = Stack()
    while pila.size() > 0:
        dino = pila.pop()
        if dino["nombre"].startswith("T"):
            resultado.append(dino)
        pila_aux.push(dino)
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    return resultado
def dino275kg(pila):
    resultado= []
    pila_aux = Stack()
    while pila.size() > 0:
        dino = pila.pop()
        if int(dino["peso"].split()[0]) < 275:
            resultado.append(dino)
        pila_aux.push(dino)
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    return resultado
def dinoAQS(pila):
    pilaRes = Stack()
    pila_aux = Stack()
    while pila.size() > 0:
        dino = pila.pop()
        if dino["nombre"][0] in ["A","Q","S"]:
            pilaRes.push(dino)
        pila_aux.push(dino)
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    return pilaRes
numeros_especies = especies(dinosaurios_pila)
numeros_descubridores = descubridores(dinosaurios_pila)
dinosaurios_con_t= dinosauriosT(dinosaurios_pila)
dinosaurios_menos_275= dino275kg(dinosaurios_pila)
dinosaurios_AQS=dinoAQS(dinosaurios_pila)
print(f"Cantidad de especies: {numeros_especies}")
print(f"Cantidad de descubridores distintos: {numeros_descubridores}")
print(f"Dinosaurios que empiezan con 'T': {[d["nombre"] for d in dinosaurios_con_t]}")
print(f"Dinosaurios que pesan menos de 275 kg: {[d["nombre"] for d in dinosaurios_menos_275]}")
print("Dinosaurios que empiezan con A Q S")
while dinosaurios_AQS.size() > 0 :
    asd = dinosaurios_AQS.pop()
    print(asd["nombre"])