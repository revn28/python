class ListaDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, produto, valor, quantidade):
        total = valor * quantidade
        item = {
            'produto': produto,
            'valor': valor,
            'quantidade': quantidade,
            'total': total
        }
        self.itens.append(item)
        print(f'{quantidade}x {produto} adicionado à lista.')

    def remover_item(self, produto):
        for item in self.itens:
            if item['produto'] == produto:
                self.itens.remove(item)
                print(f'{produto} removido da lista.')
                return
        print(f'{produto} não encontrado na lista.')

    def atualizar_item(self, produto):
        for item in self.itens:
            if item['produto'] == produto:
                print(f'Atualizando informações para {produto}:')
                novo_nome = input('Novo nome do produto: ')
                nova_quantidade = int(input('Nova quantidade: '))
                novo_valor = float(input('Novo valor unitário: ').replace(',', '.'))

                item['produto'] = novo_nome
                item['quantidade'] = nova_quantidade
                item['valor'] = novo_valor
                item['total'] = novo_valor * nova_quantidade

                print(f'{produto} atualizado na lista.')
                return
        print(f'{produto} não encontrado na lista.')

    def exibir_lista(self):
        if not self.itens:
            print('A lista de compras está vazia.')
        else:
            print('Lista de compras:')
            total_compra = 0
            for item in self.itens:
                print(f"{item['quantidade']}x {item['produto']} - R${item['valor']:.2f} cada - Total: R${item['total']:.2f}")
                total_compra += item['total']
            print(f'Total da compra: R${total_compra:.2f}')

lista_compras = ListaDeCompras()

while True:
    print('\n1. Adicionar item')
    print('2. Remover item')
    print('3. Atualizar produto')
    print('4. Exibir lista de compras')
    print('5. Sair')

    escolha = input('Escolha uma opção (1/2/3/4/5): ')

    if escolha == '1':
        produto = input('Digite o nome do produto: ')
        valor = float(input('Digite o valor unitário do produto: ').replace(',', '.'))
        quantidade = int(input('Digite a quantidade a ser comprada: '))
        lista_compras.adicionar_item(produto, valor, quantidade)
    elif escolha == '2':
        produto = input('Digite o nome do produto a ser removido: ')
        lista_compras.remover_item(produto)
    elif escolha == '3':
        produto = input('Digite o nome do produto a ser atualizado: ')
        lista_compras.atualizar_item(produto)
    elif escolha == '4':
        lista_compras.exibir_lista()
    elif escolha == '5':
        print('Saindo do programa. Lista final de compras:')
        lista_compras.exibir_lista()
        break
    else:
        print('Opção inválida. Escolha novamente.')
