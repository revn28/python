import datetime 


livros_ficçao_cientifica = {'Kindred – laços de sangue': {"emprestados": 0, "disponiveis": 3},'Neuromancer':{"emprestados": 0, "disponiveis": 3},'Eu, robô':{"emprestados": 0, "disponiveis": 3}, 'O fim da infância':{"emprestados": 0, "disponiveis": 2}, 'O Homem do castelo alto':{"emprestados": 0, "disponiveis": 5}, 'A paixão da nova eva':{"emprestados": 0, "disponiveis": 5}, 'A máquina do tempo':{"emprestados": 0, "disponiveis": 5}, 'O guia do mochileiro das galáxias':{"emprestados": 0, "disponiveis": 5},'As crônicas marcianas':{"emprestados": 0, "disponiveis": 4}, 'Fundação – trilogia':{"emprestados": 0, "disponiveis": 1}}

livros_fantasia = {'A sociedade do anel':{"emprestados": 0, "disponiveis": 6}, 'A guerra dos tronos':{"emprestados": 0, "disponiveis": 5}, 'Deuses americanos':{"emprestados": 0, "disponiveis": 5},'As brumas de avalon':{"emprestados": 0, "disponiveis": 5},'O Nnome do vento':{"emprestados": 0, "disponiveis": 5},'O leão':{"emprestados": 0, "disponiveis": 5},' A feiticeira e o guarda-roupa':{"emprestados": 0, "disponiveis": 5},'O maravilhoso mágico de oz':{"emprestados": 0, "disponiveis": 3},'Eragon':{"emprestados": 0, "disponiveis": 2}, 'Harry potter e a pedra filosofal':{"emprestados": 0, "disponiveis": 4},'A cor da magia ':{"emprestados": 0, "disponiveis": 1}}

livros_romance = {'Orgulho e preconceito':{"emprestados": 0, "disponiveis": 4}, 'Os miseráveis':{"emprestados": 0, "disponiveis": 6},'Dom casmurro':{"emprestados": 0, "disponiveis": 8},'Anna karenina':{"emprestados": 0, "disponiveis": 8},'Os catadores de conchas':{"emprestados": 0, "disponiveis": 3},'O morro dos ventos uivantes':{"emprestados": 0, "disponiveis": 5},'O amor nos tempos de cólera':{"emprestados": 0, "disponiveis": 3},'O retrato de dorian Gray':{"emprestados": 0, "disponiveis": 1}, 'Cem anos de solidão':{"emprestados": 0, "disponiveis": 3},'Crime e castigo':{"emprestados": 0, "disponiveis": 7}}

livros_psicologia = {'Introdução à psicologia':{"emprestados": 0, "disponiveis": 4},'O poder do hábito':{"emprestados": 0, "disponiveis": 2},'O mal-estar na civilização':{"emprestados": 0, "disponiveis": 2},'O animal social':{"emprestados": 0, "disponiveis": 3},'Inteligência emocional':{"emprestados": 0, "disponiveis": 1},'O homem que confundiu sua esposa com um chapéu':{"emprestados": 0, "disponiveis": 3},'Mulheres que amam demais':{"emprestados": 0, "disponiveis": 2},'Teoria das personalidades':{"emprestados": 0, "disponiveis": 3},'O livro vermelho':{"emprestados": 0, "disponiveis": 2},'Poderosa mente':{"emprestados": 0, "disponiveis": 4}}

livros_terror = {'O exorcista':{"emprestados": 0, "disponiveis": 2},'It-a coisa ':{"emprestados": 0, "disponiveis": 4},'Cemiterio':{"emprestados": 0, "disponiveis": 2},'Dracula':{"emprestados": 0, "disponiveis": 3},'O iluminado':{"emprestados": 0, "disponiveis": 3},'A casa infernal':{"emprestados": 0, "disponiveis": 4},'o desfiladeiro do medo':{"emprestados": 0, "disponiveis": 4},'A noiva fantasma':{"emprestados": 0, "disponiveis": 2},'As ruinas':{"emprestados": 0, "disponiveis": 3},'O bebe de rosimery':{"emprestados": 0, "disponiveis": 2}}

livros_devolvidos = {}
livros_emprestados = {}
genero = str
while genero != 'fechar':
 genero = input(f"""Temos de: 
    Terror 
    Psicologia
    Ficção cientifica
    Fantasia                       
    Romance
      ou devolver 
     : """).lower()  
 match genero:
     case 'terror':
        print(livros_terror)
        nome = input('Digite o nome do livro: ').capitalize()
        for x in livros_terror:
            if nome in x:
             print(nome)
            emprestimo = input(f'Registar emprestimo do livro {nome} s/n: ')
            if emprestimo == 's':        
             #data_hora_emprestimo = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
             if nome in livros_terror:
               if livros_terror[nome]["disponiveis"] > 0:
                  livros_terror[nome]["disponiveis"] -= 1
                  livros_terror[nome]["emprestados"] += 1
                  print(f"O livro {livros_terror[nome]} foi emprestado com sucesso!")
               elif livros_terror[livros_terror]["disponiveis"] == 0:
                     print(f"Desculpe, o livro {livros_terror[nome]} não está disponível no momento.")
               elif livros_terror[livros_terror]:
                  print(f"Desculpe, o livro {livros_terror[nome]} não foi encontrado.")
            elif emprestimo == 'n':
               print('Menu principal')
            print('-'*40)      
#      case 'fantasia':
#         print(livros_fantasia)
#         nome = input('Digite o nome do livro: ').capitalize()
#         for x in livros_fantasia:
#              if nome in x:
#               emprestimo = input(f'Registar emprestimo do livro {x} s/n: ')
#               if emprestimo == 's':
#                  data_hora_emprestimo = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
#                  livros_emprestados.append([nome,data_hora_emprestimo])
#               elif emprestimo == 'n':
#                     print('Menu principal')
#                     print('-'*40)       
#      case 'psicologia':
#       print(livros_psicologia)
#       nome = input('Digite o nome do livro: ').capitalize()
#       for x in livros_psicologia:
#              if nome in x:
#               emprestimo = input(f'Registar emprestimo do livro {x} s/n: ')
#               if emprestimo == 's':
#                  data_hora_emprestimo = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
#                  livros_emprestados.append([nome,data_hora_emprestimo])
                
#               elif emprestimo == 'n':
#                     print('Menu principal')   
#      case 'ficção cientifica':
#       print(livros_ficçao_cientifica)
#       nome = input('Digite o nome do livro: ').capitalize()
#       for x in livros_ficçao_cientifica:
#              if nome in x:
#               emprestimo = input(f'Registar emprestimo do livro {x} s/n: ')
#               if emprestimo == 's':
#                  data_hora_emprestimo = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
#                  livros_emprestados.append([nome,data_hora_emprestimo])
#               elif emprestimo == 'n':
#                     print('Menu principal')
#                     print('-'*40)   
#      case 'romance':
#       print(livros_romance)
#       nome = input('Digite o nome do livro: ').capitalize()
#       for x in livros_romance:
#              if nome in x:
#               emprestimo = input(f'Registar emprestimo do livro {x} s/n: ')
#               if emprestimo == 's':
#                  data_hora_emprestimo = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
#                  livros_emprestados.append([nome,data_hora_emprestimo])
#               elif emprestimo == 'n':
#                     print('Menu principal')
#                     print('-'*40)
#      case 'devolver':
#       dev = input('Qual livro sera devolvido: ').capitalize()
#       data_hora_devolução = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
#       livros_devolvidos.append([dev,data_hora_devolução])              
# else:
#      print('-'*40)
#      ver = input('Digite "e"(emprestados) "d" (devolvidos): ')
#      match ver:
#          case 'e':
#             print(livros_emprestados)
#             print(livros_terror)                                
#          case 'd':
#              print(livros_devolvidos)                     

# livros = {"Sapiens": {"emprestados": 0, "disponiveis": 3},
#           "Homo Deus": {"emprestados": 0, "disponiveis": 3},
#           "21 Lições para o Século 21": {"emprestados": 0, "disponiveis": 3}}

# livro = input("Digite o nome do livro: ")

# if livro in livros:
#     if livros[livro]["disponiveis"] > 0:
#         livros[livro]["disponiveis"] -= 1
#         livros[livro]["emprestados"] += 1
#         print(f"O livro {livro} foi emprestado com sucesso!")
#     else:
#         print(f"Desculpe, o livro {livro} não está disponível no momento.")
# else:
#     print(f"Desculpe, o livro {livro} não foi encontrado.")