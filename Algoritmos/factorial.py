def factorialR (numero):
    if numero == 0:
        return 1
    else:
        return numero * factorialR(numero-1)
print(factorialR(5))