'''
Classe Biblioteca:
A classe Biblioteca deve conter: 
0. Nome da biblioteca
1. um catálogo de livros disponíveis, 
2. um registro de membros
3. métodos para empréstimo, devolução e pesquisa de livros
'''
from livro import *
from membro import *

class Biblioteca:
    def __init__(self,nomebib):
        self.nome = nomebib
        self.catalogo = []
        self.membros = []
    
    def inc_livro(self,id,titulo,autor):
        lv = Livro(id,titulo,autor)
        self.catalogo.append(lv)
        return f'Livro {lv.titulo} incluido no catálogo'

    def inc_membro(self,num,nome):
        memb = Membro(num,nome)
        self.membros.append(memb)
        return f'Membro {memb.nome} incluido no catálogo'

    def emprestar_livro(self,id,num):
        resposta = ''
        for livro in self.catalogo:
            if livro.id == id:
                if livro.status == 'disponível':
                    livro.status = 'emprestado'
                    for membro in self.membros:
                        if membro.numero == num:
                            membro.historico.append(livro.titulo)
                            resposta = f'Livro "{livro.titulo}" emprestado com sucesso'
                        break
                else:
                    resposta = f'Livro "{livro.titulo}" está indisponível para emprestimo'
            return resposta

    def devolver_livro(self,id):
        resposta = ''
        for livro in self.catalogo:
            if livro.id == id:
                livro.status = 'disponível'
                resposta = f'Livro "{livro.titulo}" devolvido com sucesso'
                break
            else:
                resposta = f'Livro "{livro.titulo}" não estava emprestado'
        return resposta
    
    def pesquisar_livro(self,p_nome):
        resposta = ''
        for livro in self.catalogo:
            if livro.titulo == p_nome:
                 resposta = f'{livro.titulo} localizado, ID: {livro.id}'
                # if livro.status == 'disponível':
                #     livro.status = 'emprestado'
                #     for membro in self.membros:
                #         if membro.numero == num:
                #             membro.historico.append(livro.titulo)
                #             resposta = f'Livro "{livro.titulo}" emprestado com sucesso'
                #         break
            else:
                    resposta = f'Livro "{p_nome}" está indisponível'
            return resposta

if __name__ == '__main__':
    print('este arquivo não pode ser executado diretamente')
