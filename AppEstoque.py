import sqlite3
from datetime import datetime

class Produto:
    def __init__(self, id, nome, descricao, quantidade, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Quantidade: {self.quantidade}, Preço: R${self.preco}"

class Venda:
    def __init__(self, id_venda, produto_id, quantidade, data_venda):
        self.id_venda = id_venda
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.data_venda = data_venda

    def __str__(self):
        return f"ID da Venda: {self.id_venda}, Produto ID: {self.produto_id}, Quantidade: {self.quantidade}, Data da Venda: {self.data_venda}"

class GerenciadorEstoque:
    def __init__(self):
        self.conexao = sqlite3.connect('estoque.db')
        self.cursor = self.conexao.cursor()

    def criar_tabelas(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                            id INTEGER PRIMARY KEY,
                            nome TEXT NOT NULL,
                            descricao TEXT,
                            quantidade INTEGER NOT NULL,
                            preco REAL NOT NULL
                            )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS vendas (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            produto_id INTEGER NOT NULL,
                            quantidade INTEGER NOT NULL,
                            data_venda DATE NOT NULL,
                            FOREIGN KEY (produto_id) REFERENCES produtos(id)
                            )''')
        self.conexao.commit()

    def converter_preco(self, preco_input):
    # Encontra a posição do último ponto na string
        last_dot_index = preco_input.rfind('.')
    # Substitui todas as ocorrências de '.' exceto a última por uma string vazia
        preco_input = preco_input.replace('.', '', last_dot_index)
    # Substitui ',' por '.' se presente
        preco_input = preco_input.replace(',', '.')
        return float(preco_input)

    def adicionar_produto(self, id, produto):
        self.cursor.execute('INSERT INTO produtos (id, nome, descricao, quantidade, preco) VALUES (?, ?, ?, ?, ?)', (id, produto.nome, produto.descricao, produto.quantidade, produto.preco))
        self.conexao.commit()


    def atualizar_produto(self, id, nome, descricao, quantidade, preco):
        self.cursor.execute('UPDATE produtos SET nome=?, descricao=?, quantidade=?, preco=? WHERE id=?', (nome, descricao, quantidade, preco, id))
        self.conexao.commit()

    def buscar_produto_por_id(self, id):
        self.cursor.execute('SELECT * FROM produtos WHERE id=?', (id,))
        produto = self.cursor.fetchone()
        if produto:
            return Produto(produto[0], produto[1], produto[2], produto[3], produto[4])
        else:
            return None

    def registrar_venda(self, venda):
        # Atualizar a quantidade disponível do produto no estoque
        produto = self.buscar_produto_por_id(venda.produto_id)
        if produto:
            nova_quantidade = produto.quantidade - venda.quantidade
            self.atualizar_produto(produto.id, produto.nome, produto.descricao, nova_quantidade, produto.preco)
        # Registrar a venda
        self.cursor.execute('INSERT INTO vendas (produto_id, quantidade, data_venda) VALUES (?, ?, ?)', (venda.produto_id, venda.quantidade, venda.data_venda))
        self.conexao.commit()
    
    def registrar_venda_usuario(self):
        id_produto = int(input("Digite o ID do produto vendido: "))
        quantidade = int(input("Digite a quantidade vendida: "))
        data_venda = datetime.now().strftime('%Y-%m-%d')
        venda = Venda(None,id_produto, quantidade, data_venda)
        self.registrar_venda(venda)
        

    def obter_produtos(self):
        self.cursor.execute('SELECT * FROM produtos')
        produtos = self.cursor.fetchall()
        lista_produtos = []
        for produto in produtos:
            lista_produtos.append(Produto(produto[0], produto[1], produto[2], produto[3], produto[4]))
        return lista_produtos

    def obter_vendas(self):
        self.cursor.execute('SELECT * FROM vendas')
        vendas = self.cursor.fetchall()
        lista_vendas = []
        for venda in vendas:
            lista_vendas.append(Venda(venda[0], venda[1], venda[2], venda[3]))
        return lista_vendas

    def exibir_estoque(self):
        produtos = self.obter_produtos()
        print("\nEstoque atual:")
        for produto in produtos:
            print(produto)

    def exibir_vendas(self):
        vendas = self.obter_vendas()
        print("\nVendas realizadas:")
        for venda in vendas:
            print(venda)

    def fechar_conexao(self):
        self.conexao.close()

# Criar um objeto do Gerenciador de Estoque
gerenciador = GerenciadorEstoque()

# Criar as tabelas caso não existam
gerenciador.criar_tabelas()



while True:
    print('------------------------Menu-----------------------')
    print("""
          1 - Registrar Venda
          2 - Adicionar produto
          3 - Atualizar produto
          4 - Vendas realizadas
          5 - Rastrear produto em estoque
          6 - Exibir estoque
          7 - Finalizar programa
          """)
    menu = input('Digite uma das opções: ')
    match menu:
        case '1':
            gerenciador.registrar_venda_usuario()
            print("="*50)
        case '2':

            id_produto = int(input("Digite o ID do produto: "))
            nome_produto = input("Digite o nome do produto: ")
            descricao_produto = input("Digite a descrição do produto: ")
            quantidade_produto = int(input("Digite a quantidade do produto: "))
            preco_input = input("Digite o preço do produto: ")
            preco_produto = gerenciador.converter_preco(preco_input)
            novo_produto = Produto(id_produto, nome_produto, descricao_produto, quantidade_produto, preco_produto)
            gerenciador.adicionar_produto(id_produto, novo_produto)

            print("="*50)
        case '3':
            id_produto = int(input("Digite o ID do produto a ser atualizado: "))
            nome_novo = input("Digite o novo nome do produto: ")
            descricao_nova = input("Digite a nova descrição do produto: ")
            quantidade_nova = int(input("Digite a nova quantidade do produto: "))
            preco = input("Digite o novo preço do produto: ")
            preco_novo = gerenciador.converter_preco(preco)
            gerenciador.atualizar_produto(id_produto, nome_novo, descricao_nova, quantidade_nova, preco_novo)
            print("="*50)
        case '4':
            gerenciador.exibir_vendas()
            print("="*50)
        
        case '5':
            id_produto = int(input("Digite o ID do produto a ser buscado: "))
            produto_encontrado = gerenciador.buscar_produto_por_id(id_produto)
            if produto_encontrado:
                print("\nProduto encontrado:")
                print(produto_encontrado)
            else:
                print("\nProduto não encontrado.")
        case '6':
            gerenciador.exibir_estoque()
            print("="*50)
        case '7':
            print("="*50)
            print("Programa finalizado.")
            print("="*50)
            break


