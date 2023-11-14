import datetime 


livros_ficçao_cientifica = [('Kindred – laços de sangue',),('Neuromancer',),('Eu, robô',), ('O fim da infância',), ('O Homem do castelo alto',), ('A paixão da nova eva',), ('A máquina do tempo',), ('O guia do mochileiro das galáxias',),('As crônicas marcianas',), ('Fundação – trilogia',)]

livros_fantasia = [('A sociedade do anel',), ('A guerra dos tronos',), ('Deuses americanos',), ('As brumas de avalon',),('O Nnome do vento',),('O leão',),(' A feiticeira e o guarda-roupa',),('O maravilhoso mágico de oz',),('Eragon',), ('Harry potter e a pedra filosofal',),('A cor da magia ',)]

livros_romance = [('Orgulho e preconceito',), ('Os miseráveis'),('Dom casmurro'),('Anna karenina'),('Os catadores de conchas'), ('O morro dos ventos uivantes'), ('O amor nos tempos de cólera'), ('O retrato de dorian Gray'), ('Cem anos de solidão'),('Crime e castigo')]

livros_psicologia = [('Introdução à psicologia',),('O poder do hábito',),('O mal-estar na civilização',),('O animal social',),('Inteligência emocional',),('O homem que confundiu sua esposa com um chapéu',),('Mulheres que amam demais',),('Teoria das personalidades',),('O livro vermelho',),('Poderosa mente',)]

livros_terror = [('O exorcista',),('It-a coisa ',),('Cemiterio',),('Dracula',),('O iluminado',),('A casa infernal',),('o desfiladeiro do medo',),('A noiva fantasma',),('As ruinas',),('O bebe de rosimery',)]

livros_devolvidos = []
livros_emprestados = []
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
             data_hora_emprestimo = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
             livros_emprestados.append([nome,data_hora_emprestimo])
             break
            elif emprestimo == 'n':
                    print('Menu principal')
                    print('-'*40)      
   #   case 'fantasia':
   #      print(livros_fantasia)
   #      nome = input('Digite o nome do livro: ').capitalize()
   #      for x in livros_fantasia:
   #           if nome in x:
   #            emprestimo = input(f'Registar emprestimo do livro {x} s/n: ')
   #            if emprestimo == 's':
   #               data_hora_emprestimo = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
   #               livros_emprestados.append([nome,data_hora_emprestimo])
   #            elif emprestimo == 'n':
   #                  print('Menu principal')
   #                  print('-'*40)       
   #   case 'psicologia':
   #    print(livros_psicologia)
   #    nome = input('Digite o nome do livro: ').capitalize()
   #    for x in livros_psicologia:
   #           if nome in x:
   #            emprestimo = input(f'Registar emprestimo do livro {x} s/n: ')
   #            if emprestimo == 's':
   #               data_hora_emprestimo = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
   #               livros_emprestados.append([nome,data_hora_emprestimo])
   #            elif emprestimo == 'n':
   #                  print('Menu principal')   
   #   case 'ficção cientifica':
   #    print(livros_ficçao_cientifica)
   #    nome = input('Digite o nome do livro: ').capitalize()
   #    for x in livros_ficçao_cientifica:
   #           if nome in x:
   #            emprestimo = input(f'Registar emprestimo do livro {x} s/n: ')
   #            if emprestimo == 's':
   #               data_hora_emprestimo = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
   #               livros_emprestados.append([nome,data_hora_emprestimo])
   #            elif emprestimo == 'n':
   #                  print('Menu principal')
   #                  print('-'*40)   
   #   case 'romance':
   #    print(livros_romance)
   #    nome = input('Digite o nome do livro: ').capitalize()
   #    for x in livros_romance:
   #           if nome in x:
   #            emprestimo = input(f'Registar emprestimo do livro {x} s/n: ')
   #            if emprestimo == 's':
   #               data_hora_emprestimo = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
   #               livros_emprestados.append([nome,data_hora_emprestimo])
   #            elif emprestimo == 'n':
   #                  print('Menu principal')
   #                  print('-'*40)
   #   case 'devolver':
      # dev = input('Qual livro sera devolvido: ').capitalize()
      # data_hora_devolução = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
      # livros_devolvidos.append([dev,data_hora_devolução])              
else:
     print('-'*40)
     ver = input('Digite "e"(emprestados) "d" (devolvidos): ')
     match ver:
         case 'e':
            print(livros_emprestados)
            #print(livros_terror)                                
         case 'd':
             print(livros_devolvidos)                     

