def romano_a_decimal(romano):
    # diccionario con los valores romanos
    romano_a_decimal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # funcion recursiva
    def convertir(romano):
        #si la cadena romano está vacía el valor  es 0
        if not romano:
            return 0
        # Si la longitud de la cadena  es 1 devolvemos su valor decimal directamente
        if len(romano) == 1:
            return romano_a_decimal[romano[0]]
        # Si el valor decimal del primer símbolo es menor que el del siguiente, restamos
        if romano_a_decimal[romano[0]] < romano_a_decimal[romano[1]]:
            return romano_a_decimal[romano[1]] - romano_a_decimal[romano[0]] + convertir(romano[2:])
        # Si el valor decimal del primer símbolo es mayor o igual al del siguiente, sumamos
        else:
            return romano_a_decimal[romano[0]] + convertir(romano[1:])

    return convertir(romano)


numero_romano = "XI"
print(f"El número romano {numero_romano} es equivalente a {romano_a_decimal(numero_romano)} en decimal.")