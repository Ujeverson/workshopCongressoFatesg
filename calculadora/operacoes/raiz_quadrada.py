import math

def raiz(numero):
    if numero < 0:
        raise ValueError("Raiz quadrada de número negativo não é real.")
    return math.sqrt(numero) 