livros = []
dados_livros = {}

def cadastrar():
    titulo = input('Digite o título do livro: ')
    autor = input('Digite o nome do autor: ')
    qtde = int(input('Digite a quantidade do livro: '))
    preco = float(input('Digite o preço do livro: '))
    if titulo == '' or autor == '':
         print('Valor cadastrado inválido... Retornando ao menu')
         return
    elif qtde < 0 or preco <= 0:
        print('Quantidade ou preço não podem ser negativo')
    else:
        livros.append(titulo)
        dados_livros[titulo] = autor, qtde, preco
        print(' ')
        print('Livro cadastrado com sucesso!')
        return
def venda():
    titulo_venda = input('Título do livro vendido: ')
    qtde_venda = int(input('Digite a quantidade vendida: '))
    if titulo_venda in dados_livros:
        autor, qtde_estoque, preco = dados_livros[titulo_venda]
        if qtde_estoque >= qtde_venda:
            preco_venda = preco*qtde_venda
            qtde_estoque -= qtde_venda
            dados_livros[titulo_venda] = autor, qtde_estoque, preco
            print(' ')
            print(f'Venda realizada!! Total: R${preco_venda}')
            return
        else:
            print('Estoque insuficiente. Venda cancelada')
            return
    else:
        print('Livro não encontrado')
        return
def relatorio():
    print('Estoque:')
    for titulo, (autor, qtde, preco) in dados_livros.items():
        total_estoque = preco*qtde
        print(f'{titulo} - {qtde} unidades - Preço: R${preco}')
        print('Valor Total do Estoque: R$',total_estoque)
        print('')
        

while True:
    print(' ')
    print('=== MENU ===')
    print('1 - Cadastrar livro')
    print('2 - Vender Livro')
    print('3 - Relátorio')
    print('4 - Sair')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        venda()
    elif opcao == 3:
        relatorio()
    elif opcao == 4:
        break
    else:
        print('Opção Inválida')