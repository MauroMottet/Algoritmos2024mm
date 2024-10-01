from heap import HeapMax	

heap = HeapMax()


actividades = [
    (3, ("Líder Supremo Snoke", "Destruir la resistencia en Jakku", "10:00", 50)),
    (3, ("Kylo Ren", "Buscar mapa de Skywalker", "11:00", None)),
    (2, ("Capitán Phasma", "Revisión de disciplina", "12:00", 10)),
    (2, ("Capitán Phasma", "Inspeccionar armas", "13:00", 5)),
    (2, ("Capitán Phasma", "Organizar patrullas", "14:00", 15)),
    (2, ("Capitán Phasma", "Entrenamiento de Stormtroopers", "15:00", 20)),
    (1, ("General Hux", "Revisión de sistemas", "16:00", None)),
    (1, ("General Hux", "Supervisión de prisioneros", "17:00", None))
]

#PUNTO A
for actividad in actividades:
    heap.add(actividad)

#PUNTO B
def mostrar_actividad(actividad):
    encargado, descripcion, hora, stormtroopers = actividad
    stormtroopers_str = f", Stormtroopers: {stormtroopers}" if stormtroopers else ", Stormtroopers: No requeridos"
    return f"Encargado: {encargado}, Descripción: {descripcion}, Hora: {hora}{stormtroopers_str}"

#PUNTO E y F
for i in range(5):
    actividad_atendida = heap.remove()[1]
    print(f"Atendiendo operación {i+1}: {mostrar_actividad(actividad_atendida)}")


heap.add((2, ("Capitán Phasma", "Revisión de intrusos en el hangar B7", "18:00", 25)))

#PUNTO G
actividad_atendida = heap.remove()[1]
print(f"Atendiendo operación 6: {mostrar_actividad(actividad_atendida)}")


heap.add((3, ("Líder Supremo Snoke", "Destruir el planeta Takodana", "19:00", None)))


contador = 7
while heap.elements:
    actividad_atendida = heap.remove()[1]
    print(f"Atendiendo operación {contador}: {mostrar_actividad(actividad_atendida)}")
    contador += 1