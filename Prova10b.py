
cadastros = {}
def adcionar(registro, nome):
 cadastros[registro] = nome

def remover(registro):
 if registro in cadastros:
  del cadastros[registro]
 else:
  print(f"Aluno {registro} nâo encontrado")
 
def atualizar(registro,novo_nome):
 if registro in cadastros:
  cadastros[registro] = novo_nome  
 else:
  print(f"{registro} matricula nâo localizada.")

