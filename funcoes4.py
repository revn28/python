# def notas(a,b,c):
#     return a + b + c / 3
# a = float(input('Digite a primeira nota: '))
# b = float(input('Digite a segunda nota: '))
# c = float(input('Digite a terceira nota: '))
# print(f'Sua media é: {notas(a,b,c):.2f}')
#_________________________________________________________
# def calcula_area_retangulo(a,b):
#     return (a * b) / 2
# a = float(input('Digite a altura: '))
# b = float(input('Digite o comprimento: '))
# print(f"A area do triangulo: {calcula_area_retangulo(a,b):.2f}")  
# _____________________________________________________________________
# def mostrar_info(**kwargs):
#                                 #items = listar valores da biblioteca   
#     for chave, valor in kwargs.items():
#         print(f'`{chave}: {valor} ')
# mostrar_info(Nome = 'Roberto', Idade = 28, Cidade = 'Salvador')
#___________________________________________________________________
# quadrado = lambda x: x ** 2
# print(quadrado(2))
# #____________________________________________________________________
# par_impar = lambda x: f'{x} é par' if x % 2 == 0 else f'{x} é impar'
# x = int(input('Digite um numero: '))
# print(par_impar(x))
#________________________________________________________________________
# valida_usuario = lambda user: 'Erro: usuario precisa ser definido'if user == '' else('usuario não pode ter menos de 4 digitos' if len(user)< 4 else'usurio definido com sucesso!')
# print(valida_usuario(''))
# print(valida_usuario('zé'))
# print(valida_usuario('José'))
#__________________________________________________________________________
numeros = [1,2,3,4,5]
# quadrado = list(map(lambda x: x **2,numero))
#                 #map percorre os itens da lista e aplica a lambda
# print(quadrado)                
#_____________________________________________________________________
# filtroPares = list(filter(lambda x: x % 2 == 0, numeros))
# print(filtroPares)
#__________________________________________________________________   
# from functools import reduce

# numeros = [1,2,3,4,5]
# soma = reduce(lambda x,y: x + y, numeros)
#         # 1+2,3,4,5
#         # 3+3,4,5
#         # 6+4,5
#         # 10+5
#         # 15
# print(soma)
#_______________________________________
#PRATICA 3

from functools import reduce

# def concatenar_strings (*args):
#     soma = reduce(lambda x,y:x+y,args)
    
#     return soma

# print(concatenar_strings("R","P","G"))
#______________________________________________
#PRATICA 4
# def dobro_numeros(*args):
#     lista_dobro = list(map(lambda x: x*2,lista))
    
#     return lista_dobro 

# lista = [1,2,3,4,5]
# print(dobro_numeros(lista))
#_____________________________________________________
#Pratica 5
#numeros = [1,2,3,4,5]
# filtroPares = list(filter(lambda x: x % 2 == 0, numeros))
# print(filtroPares)
#_________________________________________________________
# Pratica 6
