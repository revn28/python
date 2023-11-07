print('CADASTRO')
print('_'*60)
cadastro_usuario = input('Cadastre seu usuario: ')
senha_cadastrada = input('cadastre uma senha: ')
senha_confirmacao = input('Digite a senha novamente para confirmar: ')

while senha_cadastrada != senha_confirmacao:
    senha_confirmacao = input('Senhas diferentes, tente novamente: ')
print('Usuario cadastrada!')

print('_'*60)
print('LOGIN')
usuario = input('Usuario: ')
senha_digitada = input('Senha: ')
while usuario != cadastro_usuario:
    print('usuario incorreto')
    usuario = input('Digite novamente, Usuario: ')
    senha_digitada = input('Senha: ')
if senha_digitada == senha_cadastrada:
      print('BEM-VINDO')
elif senha_digitada != senha_cadastrada:
 print('3 tentativas')
 for numero_tentativa in range(1, 4):
        senha_digitada = input(f'Senha incorreta, tentativa {numero_tentativa}, tente novamente: ')
        if senha_digitada == senha_cadastrada:
            print('BEM-VINDO')
            break
 else:
    print('Bloqueado')
 
