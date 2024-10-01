from arbol_avl import BinaryTree

tree = BinaryTree()


criaturas = [
    ('Cerbero', {'derrotado_por': 'Heracles', 'descripcion': 'Perro de tres cabezas', 'capturada': None}),
    ('Toro de Creta', {'derrotado_por': 'Heracles', 'descripcion': 'Toro gigante', 'capturada': None}),
    ('Cierva Cerinea', {'derrotado_por': 'Heracles', 'descripcion': 'Cierva dorada', 'capturada': None}),
    ('Jabalí de Erimanto', {'derrotado_por': 'Heracles', 'descripcion': 'Jabalí feroz', 'capturada': None}),
    ('Aves del Estínfalo', {'derrotado_por': 'Heracles', 'descripcion': 'Aves de metal', 'capturada': None}),
    ('Sirenas', {'derrotado_por': None, 'descripcion': 'Criaturas del mar', 'capturada': None}),
    ('Talos', {'derrotado_por': 'Medea', 'descripcion': 'Gigante de bronce', 'capturada': None}),
    ('Basilisco', {'derrotado_por': None, 'descripcion': 'Reptil mortal', 'capturada': None}),
    ('Ladón', {'derrotado_por': 'Heracles', 'descripcion': 'Dragón de cien cabezas', 'capturada': None})
]


for criatura, info in criaturas:
    tree.insert_node(criatura, info)
def listar_inorden_con_derrotador(tree):
    def __inorden_con_info(root):
        if root is not None:
            __inorden_con_info(root.left)
            derrotador = root.other_value['derrotado_por'] or 'Nadie'
            print(f"Criatura: {root.value}, Derrotado por: {derrotador}")
            __inorden_con_info(root.right)

    if tree.root is not None:
        __inorden_con_info(tree.root)

listar_inorden_con_derrotador(tree)
talos = tree.search('Talos')
if talos:
    print(f"Criatura: {talos.value}, Derrotado por: {talos.other_value['derrotado_por']}, Descripción: {talos.other_value['descripcion']}")
from collections import defaultdict

def contar_derrotas(tree):
    derrotas = defaultdict(int)

    def __contar_derrotas(root):
        if root is not None:
            if root.other_value['derrotado_por']:
                derrotas[root.other_value['derrotado_por']] += 1
            __contar_derrotas(root.left)
            __contar_derrotas(root.right)

    if tree.root is not None:
        __contar_derrotas(tree.root)
    return derrotas

derrotas = contar_derrotas(tree)
top_3_heroes = sorted(derrotas.items(), key=lambda x: x[1], reverse=True)[:3]
print(f"Top 3 héroes que derrotaron más criaturas: {top_3_heroes}")
def listar_derrotados_por(tree, heroe):
    def __listar_derrotados(root, heroe):
        if root is not None:
            if root.other_value['derrotado_por'] == heroe:
                print(f"Criatura: {root.value}")
            __listar_derrotados(root.left, heroe)
            __listar_derrotados(root.right, heroe)

    if tree.root is not None:
        __listar_derrotados(tree.root, heroe)

listar_derrotados_por(tree, 'Heracles')
def listar_no_derrotadas(tree):
    def __listar_no_derrotadas(root):
        if root is not None:
            if root.other_value['derrotado_por'] is None:
                print(f"Criatura: {root.value}")
            __listar_no_derrotadas(root.left)
            __listar_no_derrotadas(root.right)

    if tree.root is not None:
        __listar_no_derrotadas(tree.root)

listar_no_derrotadas(tree)
capturar_criaturas = ['Cerbero', 'Toro de Creta', 'Cierva Cerinea', 'Jabalí de Erimanto']
for criatura in capturar_criaturas:
    nodo = tree.search(criatura)
    if nodo:
        nodo.other_value['capturada'] = 'Heracles'
tree.delete_node('Basilisco')
tree.delete_node('Sirenas')
aves = tree.search('Aves del Estínfalo')
if aves:
    aves.other_value['derrotado_por'] = 'Heracles (varias veces)'
ladon = tree.search('Ladón')
if ladon:
    ladon.value = 'Dragón Ladón'
tree.by_level()
def listar_capturadas_por(tree, heroe):
    def __listar_capturadas(root, heroe):
        if root is not None:
            if root.other_value['capturada'] == heroe:
                print(f"Criatura: {root.value}")
            __listar_capturadas(root.left, heroe)
            __listar_capturadas(root.right, heroe)

    if tree.root is not None:
        __listar_capturadas(tree.root, heroe)

listar_capturadas_por(tree, 'Heracles')