#programa que registra nome e valor do produto
print('Caixa')
print('Digite -1 para fechar o caixa')
print('-'*40)
nome = str(input('Nome do produto: '))
preco = float(input('Digite o valor: '))
nomes = []
valor = []

while nome != '-1':
  nome = str(input('Nome do produto: '))
  nomes.append(nome)
  preco = float(input('Digite o valor: '))
  valor.append(f'R$ {preco:.2f}')
  lista_produto = zip(nomes,valor)
   
if preco == -1:
 for produto in lista_produto:
    print(produto)


