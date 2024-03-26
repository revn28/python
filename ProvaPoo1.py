class Elevador:
    def __init__(self, total_andares, capacidade):
        self.total_andares = total_andares
        self.capacidade = capacidade
        self.andar_atual = 0 
        self.destinos = set()
        self.pessoas_presentes = 0
    
    def ir_para(self, destino):
        self.destinos.add(destino)
    
    def subir(self):
        if self.andar_atual < self.total_andares - 1:
            self.andar_atual += 1
            print("Subindo")
        else:
            print("VOCÊ ESTÁ NO ANDAR MAIS ALTO!")
    
    def descer(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
            print("Descendo")
        else:
            print("VOCÊ JÁ ESTÁ NO TÉRREO!")
    
    def entrar(self):
        if self.pessoas_presentes < self.capacidade:
            self.pessoas_presentes += 1
            print("Entrando uma pessoa")
        else:
            print("O ELEVADOR ESTÁ CHEIO!")
    
    def sair(self):
        if self.pessoas_presentes > 0:
            self.pessoas_presentes -= 1
            print("Saindo uma pessoa")
        else:
            print("NÃO TEM NINGUÉM")
    
    def mover(self):
        if self.destinos:
            proximo_andar = min(self.destinos)
            self.destinos.remove(proximo_andar)
            self.andar_atual = proximo_andar
            print(f"Elevador chegou ao andar {self.andar_atual}")
        else:
            print("Não há destinos pendentes.")


elevador = Elevador(total_andares=5, capacidade=7)
elevador.subir()
elevador.subir()
elevador.subir()
elevador.subir()
elevador.subir()
elevador.subir()
elevador.descer()
elevador.descer()
elevador.descer()
elevador.descer()
elevador.descer()
elevador.descer()
elevador.entrar()
elevador.entrar()
elevador.entrar()
elevador.entrar()
elevador.entrar()
elevador.entrar()
elevador.entrar()
elevador.entrar()
elevador.sair()
elevador.sair()
elevador.sair() 
elevador.sair()
elevador.sair()
elevador.sair()
elevador.sair()
elevador.sair()

