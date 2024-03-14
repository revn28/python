from biblioteca import *

class Aplicacao:
    def __init__(self,nome_bib):
        self.bib = Biblioteca(nome_bib)
        while True:
            print(f'''
=======================
Biblioteca {self.bib.nome}
=======================
1. Incluir um livro
2. Incluir um membro
3. Listar livros
4. Listar membros
5. Emprestar livro
6. Devolver livro
7. pesquisar livro
x. Fim
=======================
          ''')
        
            opcao = input('Escolha uma  das opções: ')

            if opcao == '1':
                self.incluir_livro()
            elif opcao == '2':
                self.incluir_membro()
            elif opcao == '3':
                self.lista_livros()
            elif opcao == '4':
                self.lista_membros()
            elif opcao == '5':
                self.emprestimo()
            elif opcao == '6':
                self.devolucao()
            elif opcao == '7':
                self.pesquisar()    
            elif opcao == 'x':
                break
    
    def incluir_livro(self):
        print('==== Incluir Livro ====')
        liv_id = int(input('Informe o ID do livro: '))
        liv_titulo = input('Informe o Titulo do livro: ')
        liv_autor = input('Informe o Autor do livro: ')
        retorno = self.bib.inc_livro(liv_id,liv_titulo,liv_autor)
        print(retorno)

    def incluir_membro(self):
        print('==== Incluir Membro ====')
        mem_num = int(input('Informe o Numero do membro: '))
        mem_nome = input('Informe o Nome do membro: ')
        retorno = self.bib.inc_membro(mem_num,mem_nome)
        print(retorno)

    def lista_livros(self):
        print('==== Listar Livros =====')
        for livro in self.bib.catalogo:
            print(livro.id,livro.titulo,livro.autor,livro.status)
        print('==== Fim da lista ====')

    def lista_membros(self):
        print('==== Listar Membros ====')
        for membro in self.bib.membros:
            print(membro.numero, membro.nome)
        print('==== Fim do lista ====')
    
    def emprestimo(self):
        self.lista_livros()
        self.lista_membros()
        print('==== Emprestar Livro ====')
        liv_id = int(input('Informe o ID do livro:'))
        mem_num = int(input('Informe o Numero do membro:'))
        retorno = self.bib.emprestar_livro(liv_id,mem_num)
        print(retorno)

    def devolucao(self):
        self.lista_livros()
        print('===== Devolver Livro =====')
        liv_id = int(input('Informe o ID do livro:'))
        retorno = self.bib.devolver_livro(liv_id)
        print(retorno)
    
    def pesquisar(self):
        print('==== Pesquisar Livro ====')
        p_nome = input('Informe o titulo do livro: ')
        retorno = self.bib.pesquisar_livro(p_nome)
        print(retorno)



if __name__ == '__main__':
    biblioteca = Aplicacao('Vieira Books')
else:
    print('este arquivo DEVE ser executado diretamente')

