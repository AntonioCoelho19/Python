# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

# a,b = pessoa.values()
# print(a,b)

# for chave, valor in pessoa.items():
#     print(chave, valor)

dados_pessoa = {
    'idade': 16,
    'altura': 1.80,
}

todos_dados = {**pessoa, **dados_pessoa}

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print("NÃO NOMEADOS:", args)

    for chave, valor in kwargs.items():
        print(chave, valor)
    print()

mostro_argumentos_nomeados(4, 6, nome = "Joelinton", overall = 69)
mostro_argumentos_nomeados(**todos_dados)