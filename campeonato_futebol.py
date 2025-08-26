import sqlite3

conexao = sqlite3.connect('fut.db')
conexao.execute('''
        CREATE TABLE IF NOT EXISTS campeonato(
        id INTEGER PRIMARY KEY AUTOINCREMENT, clube text, pontos integer, vitorias integer, empates integer,
        derrotas integer, jogos integer, gols_marcados integer, gols_sofridos integer, saldo_gols integer,
        aproveitamento decimal)
        ''')

def inserir_clube():
    clube = input("Digite o nome do time: ")
    vitorias = int(input("Número de vitorias: "))
    empates = int(input("Número de empates: "))
    derrotas = int(input("Número de derrotas: "))
    gols_marcados = int(input("Quantidade de gols marcados: "))
    gols_sofridos = int(input("Quantidade de gols sofridos: "))
    pontos = (vitorias*3) + empates
    jogos = vitorias + empates + derrotas
    saldo_gols = gols_marcados - gols_sofridos
    aproveitamento = (pontos / (jogos*3))*100
    conexao.execute('INSERT INTO campeonato VALUES(NULL,?,?,?,?,?,?,?,?,?,?)',(clube, pontos, vitorias, empates, derrotas, jogos, gols_marcados, gols_sofridos, saldo_gols, aproveitamento))
    conexao.commit()
    print("Time adicionado")
    menu()

def pesquisa_clube():
    cursor = conexao.cursor()
    clube = input("Entre com o nome do time: ")
    cursor.execute('SELECT * FROM campeonato WHERE clube = ?',(clube,))
    resultado = cursor.fetchone()

    if resultado:
        print("\nDados do clube:")
        print(resultado)
    else:
        print("Clube não encontrado.\n")
    menu()
    
def pontuacao():
    cursor = conexao.cursor()
    pontuacao = int(input('Digite o valor da pontuação mínima: '))
    cursor.execute('SELECT * FROM campeonato WHERE pontos >= ?',(pontuacao,))
    lista = cursor.fetchall()
    for x in lista:
        print(x,)
    menu()

def aproveitamento():
    cursor = conexao.cursor()
    pontuacao = int(input('Digite o valor do aproveitamento mínimo: '))
    cursor.execute('SELECT * FROM campeonato WHERE aproveitamento >= ?',(pontuacao,))
    lista = cursor.fetchall()
    for x in lista:
        print(x,)
    menu()
    
def menu():
    print("\nMenu:")
    print("1. Inserir clube")
    print("2. Pesquisar clube")
    print("3. Listar por pontuação")
    print("4. Listar por aproveitamento")
    print("5. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        inserir_clube()
    elif opcao == 2:
        pesquisa_clube()
    elif opcao == 3:
        pontuacao()
    elif opcao == 4:
        aproveitamento()
    elif opcao == 5:
        print("Encerrando o programa...")

menu()