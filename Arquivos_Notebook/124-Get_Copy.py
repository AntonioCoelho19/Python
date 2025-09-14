p1 = {
    'nome': 'Luiz',
    'sobrenome' : 'Miranda'
}

print(p1['nome'])
print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
p1.update({
    'nome' : 'novo valor',
    'idade' : 20
})
# print(p1)
p1.update(sexo='Masculino', idade = 40)

tupla = ('nome', 'Rogerio'), ('idade', 65)
p1.update(tupla)
