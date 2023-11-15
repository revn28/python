lista_numeros = []
lista_numeros_pares = []
lista_numeros_impares = [] 
for n in range(10):
    numero = float(input('digite um numero: '))
    lista_numeros.append(numero)            
for i in lista_numeros:
   if i % 2 == 0:
        lista_numeros_pares.append(i)   
   else:
        lista_numeros_impares.append(i)   

listas_tuplas_impar = tuple(lista_numeros_impares)
listas_tuplas_par = tuple(lista_numeros_pares)
print(listas_tuplas_impar)
print(listas_tuplas_par)
print(f'A lista tem {len(lista_numeros_impares)} numeros imparese e {len(lista_numeros_pares)} numeros pares.')
print(f'A soma de todos os numeros é: {sum(lista_numeros)}')
