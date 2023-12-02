print('Matriculas e consultas')
print('-'*60)
ficha_aluno ={}
while True:
    inicio = input('''
    Digite (c) para cadastro de novos alunos
    Digite (r) para remover alunos
    Digite (v) para visualizar todas as matrículas:  ''').lower()
    match inicio:
        case 'c':
            aluno = (input('Informe o nome do aluno: ')).capitalize()
            matricula = int(input('Numero da matrícula: '))
            ficha_aluno[aluno] = matricula
            print('-'*60)
        case 'r':
            print(f'Alunos inscritos: {ficha_aluno}')
            matricula2 = int(input('Digite o numero da matrícula: '))
            remover_matricula = None
            for chave,valor in ficha_aluno.items():
                if valor == matricula2:
                   remover_matricula = chave
                   break
            if remover_matricula is not None:
                    del ficha_aluno[remover_matricula]
                    print(f'Aluno {remover_matricula} foi removido.')
                    print('-'*60)
            else:
                  print(f'Aluno: {matricula2} não encontrado.')   
        case 'v':
         print(f'''
               Alunos cadastrados:
               {ficha_aluno}
               ''')
         print('-'*60)



