'''
Classe Livro:
A classe Livro deve conter atributos como título, autor, ID,
estatus de empréstimo (disponível ou emprestado)
'''
class Livro:
    def __init__(self,idlivro,titulolivro,autorlivro):
        self.id = idlivro
        self.titulo = titulolivro
        self.autor = autorlivro
        self.status = 'disponível'

if __name__ == '__main__':
    print('este arquivo não pode ser executado diretamente')
