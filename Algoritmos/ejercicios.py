#!n + n -1 | n0=0
#ejercicio 2
def sumatoria (numero):
    if numero == 0:
        return 0
    else:
        return numero + sumatoria(numero-1)
    
print(sumatoria(10))
#! n1*n2 = n1 * (n1 * n2-1)
#ejercicio 3
def producto(n1,n2):
    if n2 == 1 :
        return n1 
    else :
        return n1 + producto(n1, n2-1)
print (producto(2, 10))
# 2 ^ 3 = 2 * 2 * 2 = B * (B * Ex-1)
#ejercicio 4
def potencia (base,exponente):
    if exponente== 0:
        return 1
    else:
        return base * potencia(base,exponente-1)
print (potencia(2,10))
#ejercicio 6
#cadena[-1] + cadena[-1]
def invertirsecuencia (caracteres):
    if len(caracteres)== 0:
        return caracteres
    else:
        return caracteres[-1] + invertirsecuencia(caracteres[:-1])
print(invertirsecuencia("hola"))
#ejercicio 8
#numero //2 + str(numero % 2)
def entero_decimal_a_binario(numero):
    if numero <= 1:
        return str(numero)
    else:
        return entero_decimal_a_binario(numero // 2 ) + str(numero % 2) 
print(entero_decimal_a_binario(10))
#ejercicio 10
def contar_digitos(numero):
    if numero < 10 :
        return 1
    else:
        return 1 + contar_digitos(numero // 10 )
print(contar_digitos(123456))
#ejercicio 7
# 1/n + (1/n-1....1)
def sumatoria_serie(numero):    
    if numero == 1 :
        return 1
    else :
        return 1/numero + sumatoria_serie(numero-1)

def invertir_numero(numero):
    if numero < 10:
        return numero
    else :
        return numero % 10 * 10 ** contar_digitos(numero // 10)  + invertir_numero(numero // 10)
a = 457
print(invertir_numero(a))
#ejercicio 14
def  sumar_digitos (numero):
    if numero < 10 :
        return numero
    else:
        return (numero % 10) +  sumar_digitos(numero//10)
    
#ejercicio 17
lista = ["juan","mauro","lucas","lautaro"]
def recorrer_vector(lista):
    if len(lista) == 1:
        print(lista[0])
    else:
        print(lista[-1])
        recorrer_vector(lista[0:-1])
recorrer_vector(lista)

