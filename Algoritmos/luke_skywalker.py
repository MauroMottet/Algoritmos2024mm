def usar_la_fuerza(mochila,posicion=0,objetos=0):
    if posicion >= len(mochila):
        return print("Mochila vacia/ya revisaste toda la mochila")
    if mochila[posicion] == "sable de luz":
        return print("En horabuena encontraste el sable de luz! despues de haber sacado", objetos +1 , "objetos")
    else:
        return usar_la_fuerza(mochila,posicion +1 ,objetos+1)
mochila = ["comida","agua","medkit","ropa","sable de luz","viales"]
usar_la_fuerza(mochila)