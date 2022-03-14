"""
Continuação de Dicts

{}
"""
meses = {'jan': 1, 'fev': 2, 'mar':3}

# Aqui, aprenderemos a iterar um dict com loops

for mes in meses:
    print(mes) # imprime chave

for mes in meses:
    print(meses[mes]) # imprime valor

for mes in meses:
    print('{} : {}'.format(mes, meses[mes])) # imprime chave e valor

# Acessando as chaves // modo pythonico
print(meses.keys()) # imprime apenas chaves

for mes in meses.keys():
    print(meses[mes])

# Acessando valores // modo pythonico

print(meses.values())

for mes in meses.values():
    print(mes)

# Desempacotamento de dicts
print(meses.items()) # lê-se uma tuplas cm chaves e valores
for chave, valor in meses.items():
    print('chave: {} valor: {}'.format(chave, valor))

# Soma*, valor máximo, valor mínimo, tamanho
# *Se os valores forem int ou reais

print(sum(meses.values()))
print(max(meses.values()))
print(min(meses.values()))
print(len(meses))
