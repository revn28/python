import random

lista_de_nome = [] 
lista_de_endereco = [] 
lista_de_telefone = [] 

nome=input("digite o seu nome: ") 
lista_de_nome.append(nome) 
endereco=input("digite o seu endereço: ") 
lista_de_endereco.append(endereco) 
telefone=input("digite o seu telefone: ") 
lista_de_telefone.append(telefone) 



while nome != 'fim':
    nome=input("digite o seu nome: ") 
    if nome =="fim": 
        break 
    lista_de_nome.append(nome) 
    endereco=input("digite o seu endereço: ") 
    lista_de_endereco.append(endereco) 
    telefone=input("digite o seu telefone: ") 
    lista_de_telefone.append(telefone) 
      
sorteio = random.randint(0,len(lista_de_nome)) 

print("Cliente sorteado foi:") 
print(f'{lista_de_nome[sorteio]}, de telefone {lista_de_telefone[sorteio]}, endereço {lista_de_endereco[sorteio]}.') 

