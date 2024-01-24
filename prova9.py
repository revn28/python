from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrado = list(map(lambda x: x**2, numeros))
print(quadrado)

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

def soma(x,y):
    return x + y

total = reduce(soma,numeros)
print(total)