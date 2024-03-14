'''
Classe Membro:
A classe Membro deve conter atributos como nome,
número de membro e histórico de livros emprestados.
'''
class Membro:
    def __init__(self,nummemb,nomememb):
        self.numero = nummemb
        self.nome = nomememb
        self.historico = []

if __name__ == '__main__':
    print('este arquivo não pode ser executado diretamente')
