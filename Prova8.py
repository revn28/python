from functools import reduce
notas = []
while True:
    menu = input(""" 
    1 - Adcionar nota
    2 - Calcular media
    3 - Verificar situação
    4 - Fechar                                        
    """)
    match menu:
        case '1':
            nota = float(input('Digite a nota: '))
            notas.append(nota)
            print(notas)
        case '2':
            def calcular_media():
                return reduce(lambda x,y: x + y, notas)/len(notas) if notas else 0
            print(f'Sua media é: {calcular_media()}')
        case '3':
         def verificar_situação():
            media = calcular_media()    
            if media >= 7 and media <=9:
             print(f'Aprovado com: {media}')
            elif media == 10:
             print("Parabéns, sua média é 10")   
            else:
               print('Reprovado')
         verificar_situação()
        case '4':
          print('-'*50)
          break       

            

            
              
             
               
                 