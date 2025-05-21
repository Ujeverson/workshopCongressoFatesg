# Função que recebe uma lista de números e retorna a média
def media(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma / len(numeros)

# Refatore usando list comprehension
def media(numeros):
    return sum(numeros) / len(numeros)

