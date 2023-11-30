
usuarios = {}
while True:
 inicio = input('Digite (C) para cadastro ou (L) para loguin: ')
 match inicio:
    case 'c':
     print('CADASTRO')
     print('_'*60)
     cadastro_usuario = input('Cadastre seu usuario: ')
     senha_cadastrada = input('cadastre uma senha: ')
     senha_confirmacao = input('Digite a senha novamente para confirmar: ')

     while len(senha_cadastrada) <=3 or senha_cadastrada != senha_confirmacao:
      print('A senha deve conter mais de 3 caracteres')
      senha_cadastrada = input('cadastre uma senha: ')
      senha_confirmacao = input('confirme a senha: ')
       
      if senha_confirmacao == senha_cadastrada and len(senha_cadastrada) >=3:
         print(f'{cadastro_usuario} senha cadastrada')   
       
     else:
        usuarios[cadastro_usuario] = senha_cadastrada  
        # print('senha cadastrada')
        print(usuarios)
        continue
           
    case 'l':
     print('_'*60)
     print('LOGIN')
     print(usuarios)
     usuario = input('Usuario: ')
     senha_digitada = input('Senha: ')
     buscar_usuario = [usuario for x in usuarios if usuario == x]
     while buscar_usuario != [usuario]:
      print('Usuario incorreto')
      usuario = input('Digite novamente, Usuario: ')
      senha_digitada = input('Senha: ')
      buscar_usuario = [usuario for x in usuarios if usuario == x]
     if senha_digitada == usuarios[cadastro_usuario]:
      print('BEM-VINDO')
     elif senha_digitada != usuarios[cadastro_usuario]:
        print('3 tentativas')
        for numero_tentativa in range(1, 4):
         senha_digitada2 = input(f'Senha incorreta, tentativa {numero_tentativa}, tente novamente: ')
         if senha_digitada2 == usuarios[cadastro_usuario]:
            print('BEM-VINDO')
            break
     else:
      print('Bloqueado')
 
