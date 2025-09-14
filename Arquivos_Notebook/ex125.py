import os
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()
    print("Opções:")
    
    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i}){opcao}')
    
    entrada = input("Escolha uma opção: ")
    print()
    
    acertou = False
    resposta = None
    qtd_opcoes = len(opcoes)

    if entrada.isdigit():
        resposta = int(entrada)
        
    else:
        print('Digite um número animal')
        
    
    if resposta is not None:
        if resposta >= 0 and resposta < qtd_opcoes:
            if opcoes[resposta] == pergunta['Resposta']:
                acertou  = True
    if acertou:
        print("Acertou Miseravi")
        print()
        acertos+=1
    else:
        print('Errou burro')
        print()

os.system('cls')
if acertos == 3:
    print('Parabéns acertou tudo')
elif acertos == 2:
    print('Você acertou 2 questões')
elif acertos == 1:
    print('Você acertou uma questão')
else:
    print('Precisa estudar')


    
    
