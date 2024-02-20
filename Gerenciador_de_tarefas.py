tarefas = []

def adicionar_tarefa(nome, descricao, prioridade, categoria):
    tarefa = {
        'nome': nome,
        'descricao': descricao,
        'prioridade': prioridade,
        'categoria': categoria,
        'concluida': False
    }
    tarefas.append(tarefa)
    print(f'Tarefa "{nome}" adicionada com sucesso!')

def listar_tarefas():
    print("Lista de Tarefas:")
    tarefas_ordenadas = sorted(tarefas, key=lambda x: x['prioridade'], reverse=True)
    for i, tarefa in enumerate(tarefas_ordenadas, 1):
        status = "Concluída" if tarefa['concluida'] else "Pendente"
        print(f"{i}. {tarefa['nome']} - {status} - Prioridade: {tarefa['prioridade']} - Categoria: {tarefa['categoria']}")

def marcar_tarefa_concluida(indice_tarefa):
    if 1 <= indice_tarefa <= len(tarefas):
        tarefa = sorted(tarefas, key=lambda x: x['prioridade'], reverse=True)[indice_tarefa - 1]
        tarefa['concluida'] = True
        print(f'Tarefa "{tarefa["nome"]}" marcada como concluída!')
    else:
        print('Índice de tarefa inválido.')

def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas por Prioridade")
        print("3. Marcar Tarefa como Concluída")
        print("4. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            nome = input("Digite o nome da tarefa: ")
            descricao = input("Digite a descrição da tarefa: ")
            prioridade = int(input("Digite a prioridade da tarefa (1 a 5): "))
            categoria = input("Digite a categoria da tarefa: ")
            prioridade = max(1, min(prioridade, 5))

            adicionar_tarefa(nome, descricao, prioridade, categoria)
        elif escolha == '2':
            listar_tarefas()
        elif escolha == '3':
            indice_tarefa = int(input("Digite o número da tarefa a ser marcada como concluída: "))
            marcar_tarefa_concluida(indice_tarefa)
        elif escolha == '4':
            print("Saindo do gerenciador de tarefas. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
