#prova 2 Python
carro = int(input('Digite a velociade do veículo: '))
print(f'{carro} km/h' )
base = 80
excesso = carro - base
multa = 20
print(f'{excesso} Km/h')
if carro:
    valor = excesso * multa
    print(f'O condutor passou {excesso}Km/h a cima da velocidade permitida da via.\nPara cada km/h ultrapassado sera aplicado um valor de R$20,00 reias.\nCalculo da multa: {excesso} x R$20,00 = R${valor:.2f}')
    
