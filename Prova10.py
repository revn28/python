from Prova10b import *
print("====Menu====")
while True:
    print(""" 
    1 - Adcionar novos alunos
    2 - remover aluno
    3 - Atualizar cadastro
    4 - Vizualizar todos os cadastros
    0 - Sair                                  
     """)
    menu = int(input("Digite 1,2,3 ou 4: "))
    match menu:
        case 1:
         matricula = int(input("Digite o numero da matricula: "))
         aluno = input("Digite o nome: ")
         adcionar(matricula,aluno)
         print("-"*100)
         print(cadastros)
         print("-"*100)
        case 2:
          print(cadastros)
          matricula = int(input("Digite o numero da matricula: "))
          print(f"{cadastros[matricula]} removido com sucesso")
          remover(matricula)
          print("-"*100)
          print(cadastros)
          print("-"*100)
        case 3:
          print(cadastros)  
          atulaização = int(input('Digite a matricula: '))
          if atulaização in cadastros:
           novo_nome = input("Digite o novo nome: ")
           atualizar(atulaização,novo_nome)
           print("-"*100)
           print(cadastros)
           print("-"*100)
          else: 
            print('Matricula nao encontrada!')
        case 4:
          print("-"*100)
          print(cadastros)
          print("-"*100)
        case 0 :
          print("-"*100)
          print(cadastros)
          print("-"*100)
          print("Programa encerrado.")
          break  
    

   