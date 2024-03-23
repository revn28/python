import sqlite3
import tkinter as tk
import random
from tkinter import messagebox
import datetime

# Conexão com o banco de dados
conn = sqlite3.connect('rpg.db')
c = conn.cursor()

# Criação da tabela para personagens
c.execute('''CREATE TABLE IF NOT EXISTS personagens
             (id INTEGER PRIMARY KEY, nome TEXT, classe TEXT, nivel INTEGER, pontos_vida INTEGER,  xp INTEGER)''')

c.execute('''CREATE TABLE IF NOT EXISTS historico_jogos
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             data_hora_salvamento TEXT,
             personagem TEXT,
             inimigo TEXT,
             vencedor TEXT,
             batalha TEXT)''')


# Adicionando coluna "xp" à tabela "personagens"
# c.execute("ALTER TABLE personagens ADD COLUMN xp INTEGER")
# Commit da transação e fechamento da conexão
conn.commit()



# Classe para representar personagens
class Personagem:
    def __init__(self, nome, classe, nivel=1, pontos_vida=100,xp=0):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.pontos_vida = pontos_vida
        self.xp = xp

    def salvar(self):
        c.execute("INSERT INTO personagens (nome, classe, nivel, pontos_vida, xp) VALUES (?, ?, ?, ?, ?)",
                  (self.nome, self.classe, self.nivel, self.pontos_vida, self.xp))
        conn.commit()

    @staticmethod
    def carregar(nome):
        c.execute("SELECT * FROM personagens WHERE nome=?", (nome,))
        data = c.fetchone()
        if data:
            return Personagem(data[1], data[2], data[3], data[4])
        else:
            return None

#comandos de batalha do personagem
    def atacar(self, alvo):
        dano = random.randint(5, 15)  # Dano aleatório entre 5 e 15
        alvo.defender(dano)

    def defender(self, dano):
        self.pontos_vida -= dano
        if self.pontos_vida <= 0:
            print(f"{self.nome} foi derrotado!")
    
    def ganhar_xp(self, xp):
        self.xp += xp
        print(f"{self.nome} ganhou {xp} pontos de experiência!")
        c.execute("UPDATE personagens SET xp = ? WHERE nome = ?", (self.xp, self.nome))
        conn.commit()

# Criação da tabela para inimigos
c.execute('''CREATE TABLE IF NOT EXISTS inimigos
             (id INTEGER PRIMARY KEY, nome TEXT, nivel INTEGER, pontos_vida INTEGER)''')
conn.commit()

# Classe para representar inimigos
class Inimigo:
    def __init__(self, nome, nivel, pontos_vida):
        self.nome = nome
        self.nivel = nivel
        self.pontos_vida = pontos_vida

    def salvar(self):
        c.execute("INSERT INTO inimigos (nome, nivel, pontos_vida) VALUES (?, ?, ?)",
                  (self.nome, self.nivel, self.pontos_vida))
        conn.commit()

    @staticmethod
    def carregar(nome):
        c.execute("SELECT * FROM inimigos WHERE nome=?", (nome,))
        data = c.fetchone()
        if data:
            return Inimigo(data[1], data[2], data[3])
        else:
            return None
    
    
    def atacar(self, alvo):
        dano = random.randint(3, 10)  # Dano aleatório entre 3 e 10
        alvo.defender(dano)

    def defender(self, dano):
        self.pontos_vida -= dano
        if self.pontos_vida <= 0:
            print(f"{self.nome} foi derrotado!")

# Interface gráfica
class GameInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("RPG Game")

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.label_nome = tk.Label(self.frame, text="Nome do Personagem:")
        self.label_nome.grid(row=0, column=0)
        self.entry_nome = tk.Entry(self.frame)
        self.entry_nome.grid(row=0, column=1)

        self.label_classe = tk.Label(self.frame, text="Classe do Personagem:")
        self.label_classe.grid(row=1, column=0)
        self.entry_classe = tk.Entry(self.frame)
        self.entry_classe.grid(row=1, column=1)

        self.button_criar = tk.Button(self.frame, text="Criar Personagem", command=self.criar_personagem)
        self.button_criar.grid(row=2, columnspan=2)
        # self.button_inimigo = tk.Button(self.frame, text="Mostrar Inimigo", command=self.mostrar_inimigo)
        # self.button_inimigo.grid(row=8, columnspan=2)

        self.label_nome_inimigo = tk.Label(self.frame, text="Nome do Inimigo:")
        self.label_nome_inimigo.grid(row=4, column=0)
        self.entry_nome_inimigo = tk.Entry(self.frame)
        self.entry_nome_inimigo.grid(row=4, column=1)

        self.label_nivel_inimigo = tk.Label(self.frame, text="Nível do Inimigo:")
        self.label_nivel_inimigo.grid(row=5, column=0)
        self.entry_nivel_inimigo = tk.Entry(self.frame)
        self.entry_nivel_inimigo.grid(row=5, column=1)

        self.label_pontos_vida_inimigo = tk.Label(self.frame, text="Pontos de Vida do Inimigo:")
        self.label_pontos_vida_inimigo.grid(row=6, column=0)
        self.entry_pontos_vida_inimigo = tk.Entry(self.frame)
        self.entry_pontos_vida_inimigo.grid(row=6, column=1)

        self.button_adicionar_inimigo = tk.Button(self.frame, text="Adicionar Inimigo", command=self.adicionar_inimigo)
        self.button_adicionar_inimigo.grid(row=7, columnspan=2)

        
        self.button_listar_inimigos = tk.Button(self.frame, text="Listar Inimigos", command=self.listar_inimigos)
        self.button_listar_inimigos.grid(row=12, columnspan=3)

        # self.entry_nome_inimigo = tk.Entry(self.frame)
        # self.entry_nome_inimigo.grid(row=8, columnspan=2)
        # self.entry_nome_inimigo.insert(0, "")

        # self.button_mostrar_inimigo = tk.Button(self.frame, text="Mostrar Inimigo", command=self.mostrar_inimigo)
        # self.button_mostrar_inimigo.grid(row=9, columnspan=2)

        self.button_selecionar_confronto = tk.Button(self.frame, text="Selecionar Confronto", command=self.selecionar_confronto)
        self.button_selecionar_confronto.grid(row=13, columnspan=2)

        self.button_fechar_e_salvar = tk.Button(self.frame, text="Fechar e Salvar", command=self.fechar_e_salvar)
        self.button_fechar_e_salvar.grid(row=3, columnspan=2)

    def fechar_e_salvar(self):
        # Implementar lógica para salvar o jogo
        data_hora_salvamento = datetime.datetime.now()
                # Salvar batalha no histórico de jogos
        if len(personagens_salvos) >= 2:
            batalha_info = f"Batalha entre {personagens_salvos[0]} e {personagens_salvos[1]}"
        else:
            batalha_info = "Nenhuma batalha registrada"  # Exemplo de informação da batalha

        c.execute("INSERT INTO historico_jogos (data_hora_salvamento, personagem, inimigo, vencedor, batalha) VALUES (?, ?, ?, ?, ?)",
        (data_hora_salvamento, nome_personagem, nome_inimigo, vencedor, batalha_info))
        conn.commit()

        # Fechar a aplicação
        self.root.destroy()

    def adicionar_inimigo(self):
        nome = self.entry_nome_inimigo.get()
        nivel = self.entry_nivel_inimigo.get()
        pontos_vida = self.entry_pontos_vida_inimigo.get()

        if nome and nivel and pontos_vida:
            try:
                nivel = int(nivel)
                pontos_vida = int(pontos_vida)
                inimigo = Inimigo(nome, nivel, pontos_vida)
                inimigo.salvar()
                messagebox.showinfo("Sucesso", "Inimigo adicionado com sucesso!")
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira um número válido para o nível e pontos de vida.")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    # def mostrar_inimigo(self):
    #     nome_inimigo = self.entry_nome_inimigo.get()
    #     if nome_inimigo:
    #         inimigo = Inimigo.carregar(nome_inimigo)
    #         if inimigo:
    #             messagebox.showinfo("Inimigo", f"Nome: {inimigo.nome}\nNível: {inimigo.nivel}\nPontos de Vida: {inimigo.pontos_vida}")
    #         else:
    #             messagebox.showerror("Erro", "Inimigo não encontrado.")
    #     else:
    #         messagebox.showerror("Erro", "Por favor, insira o nome do inimigo.")
    
    def listar_inimigos(self):
        c.execute("SELECT nome FROM inimigos")
        inimigos = c.fetchall()
        if inimigos:
            messagebox.showinfo("Inimigos Disponíveis", "\n".join([f"- {inimigo[0]}" for inimigo in inimigos]))
        else:
            messagebox.showinfo("Inimigos Disponíveis", "Nenhum inimigo encontrado.")
    
    def criar_personagem(self):
        nome = self.entry_nome.get()
        classe = self.entry_classe.get()
        if nome and classe:
            personagem = Personagem(nome, classe)
            personagem.salvar()
            messagebox.showinfo("Sucesso", "Personagem criado com sucesso!")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
    
    def selecionar_confronto(self):
        confronto_window = tk.Toplevel(self.root)
        confronto_window.title("Selecionar Confronto")

        label_personagem = tk.Label(confronto_window, text="Selecione o Personagem:")
        label_personagem.grid(row=0, column=0)
        entry_personagem = tk.Entry(confronto_window)
        entry_personagem.grid(row=0, column=1)

        label_inimigo = tk.Label(confronto_window, text="Selecione o Inimigo:")
        label_inimigo.grid(row=1, column=0)
        entry_inimigo = tk.Entry(confronto_window)
        entry_inimigo.grid(row=1, column=1)

        confirm_button = tk.Button(confronto_window, text="Confirmar", command=lambda: self.confirmar_confronto(entry_personagem.get(), entry_inimigo.get(), confronto_window))
        confirm_button.grid(row=2, columnspan=2)

    def confirmar_confronto(self, nome_personagem, nome_inimigo, confronto_window):
        confronto_window.destroy()
        self.iniciar_batalha(nome_personagem, nome_inimigo)
    
    def iniciar_batalha(self,nome_personagem,nome_inimigo):
        # Carregar personagem do jogador
        nome_personagem = nome_personagem  
        c.execute("SELECT * FROM personagens WHERE nome=?", (nome_personagem,))
        dados_personagem = c.fetchone()
        if dados_personagem:
            personagem = Personagem(dados_personagem[1], dados_personagem[2], dados_personagem[3], dados_personagem[4],dados_personagem[5])
        else:
            messagebox.showerror("Erro", "Personagem não encontrado!")
            return

        # Carregar inimigo da batalha
        nome_inimigo = nome_inimigo    
        c.execute("SELECT * FROM inimigos WHERE nome=?", (nome_inimigo,))
        dados_inimigo = c.fetchone()
        if dados_inimigo:
            inimigo = Inimigo(dados_inimigo[1], dados_inimigo[2], dados_inimigo[3])
        else:
            messagebox.showerror("Erro", "Inimigo não encontrado!")
            return

        # Lógica de batalha
        print(f"Começou a batalha entre {personagem.nome} e {inimigo.nome}!")
        while personagem.pontos_vida > 0 and inimigo.pontos_vida > 0:
            print(f"{personagem.nome} ataca {inimigo.nome}!")
            personagem.atacar(inimigo)
            print(f"{inimigo.nome} ataca {personagem.nome}!")
            inimigo.atacar(personagem)
            print(f"{personagem.nome}: {personagem.pontos_vida} HP")
            print(f"{inimigo.nome}: {inimigo.pontos_vida} HP")

        if personagem.pontos_vida == 0:
            print(f"{personagem.nome} foi derrotado!")
            vencedor = nome_inimigo
        else:
            print(f"{inimigo.nome} foi derrotado!")
            xp_ganho = random.randint(10, 20)  # XP aleatório entre 10 e 20
            personagem.ganhar_xp(xp_ganho)
            vencedor = nome_personagem  # Alterado para nome do personagem

            data_hora_batalha = datetime.datetime.now()
            batalha_info = f"Batalha entre {nome_personagem} e {nome_inimigo}"
            c.execute("INSERT INTO historico_jogos (data_hora_salvamento, personagem, inimigo, vencedor, batalha) VALUES (?, ?, ?, ?, ?)",
              (data_hora_batalha, nome_personagem, nome_inimigo, vencedor, batalha_info))
            self.fechar_e_salvar(nome_personagem,nome_inimigo,vencedor)

            personagens_salvos.append(vencedor)

personagens_salvos = []  # Lista dos nomes dos personagens salvos, preencher conforme necessário
# Inicialização da interface
root = tk.Tk()
app = GameInterface(root)
root.mainloop()
