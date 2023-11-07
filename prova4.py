num = 1
list_num = []
while num != 0:
    num = int(input('Digite um numero: '))
    list_num.append(num)
    if num == 0:
     list_num.remove(0)
     print(f'Numeros digitados {list_num}')
soma_das_notas =sum(list_num)
quantidade_de_numeros = len(list_num)
media = soma_das_notas / quantidade_de_numeros
print(f'Foram digitados {quantidade_de_numeros} numeros.')
print(f'A soma de todos os numeros digitados: {soma_das_notas}')
print(f'A media aritimetica: {media:.2f}')

