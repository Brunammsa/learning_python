"""
Dicionários

São coleções do tipo chave:valor

São representados por chaves {}

print(type({}))

OBS: São representados por dois pontos ":", chave:valor
    - tanto a chave quanto o valor podem ser representados por qualquer tipo de dado;
    - podemos misturas tipos de dados;
"""
# Criação de dicionários: mais comum

paises = {'br': 'brasil', 'eua': 'Estados Unidos'}
print(paises)
print(type(paises))

# menos comum
paises = dict(br='brasil', eua='estados unidos')
print(paises)
print(type(paises))

# Acessando elementos

print(paises['br']) # é necessário acessar pela chave, assim, ele retornará o valor

# acessando elementos (forma recomendada) via get

print(paises.get('br'))

russia = paises.get('ru')

if russia:
    print('encontrei')
else:
    print('não encontrei')

# Outra forma de usar o get sem utilizar o if/else é:

pais = paises.get('ru', 'Não encontrei o país') # pega o país do dict 'br', e caso não encontre, imprime o próximo valor
print(pais)

print('br' in paises) # - True
print('ru' in paises) # não existe chave ru na variável - False
print('brasil' in paises) # brasil não é chave, e sim valor - False

if 'ru' in paises:
    russia = paises['ru'] # aqui não irá dar KeyError, se não tiver a chave ele simplesmente irá ignorar

# OBS.: quando ele não encontra a chave, ele retorna "none", na forma anterior ele retorna "keyerror"
# OBS.: o tipo None sempre é considerado false

numeros = None # sempre N maiúsculo
print(numeros)
print(type(numeros))
# OBS.: quando criamos uma variável None, queremos criar e iniciar uma variável sem tipo, para posteriormente acrescentar, quando não se sabe ainda com o que irá preencher

numeros = 1.23, 1.4, 1.567 # agora ele foi preenchido por uma tupla
print(numeros)
print(type(numeros)) # e seu tipo retorna tupla

# Podemos utilizar qualquer tipo de dado como chaves para o dict.

localidades = {
    (122.223, 1234): 'Piedade',
    'rec': 'boa viagem',
    23.1: 'olinda'
}
print(localidades)
print(type(localidades))

# no exemplo acima, utilizamos como chaves uma tupla, uma str e um float, então, literalmente, podemos utilizar qualquer dado para representar chaves

# Adicionar elementos em um dict

brownie_de_caneca = {
    'chocolate em pó': 'uma colher de sopa',
    'leite': '2 colheres de sopa',
    'açúcar': '1 colher de sopa',
    'manteiga': '1 colher de sopa de manteiga derretida',
    'fermento': '1/2 colher de chá',
    'farinha': '2 colheres',
}

print(brownie_de_caneca)
brownie_de_caneca['baunilha'] = 'a gosto' # forma 1 (mais comum)
print(brownie_de_caneca)

novo_ingrediente = {'aveia flocos finos(substituição)': 'mesma quantidade da farinha'}
brownie_de_caneca.update(novo_ingrediente) # não está selecionando o update mas está pegando // forma 2 // ou ainda: brownie_de_caneca.update({chave:valor})
print(brownie_de_caneca)

# Atualizando dados em um dict

brownie_de_caneca['aveia flocos finos(substituição)'] = 'igual farinha' # forma 1
print(brownie_de_caneca)

brownie_de_caneca.update({'manteiga':'1 c/s derretida'})
print(brownie_de_caneca)

# OBS.: em dicts não podemos ter chaves repetidas

# Como remover dados de um dict

brownie_de_caneca.pop('chocolate em pó') # forma 1 // precisamos sempre informar a chave ou então um KeyError será retornado
print(brownie_de_caneca)

retirar = brownie_de_caneca.pop('manteiga')
print(retirar) # aqui estamos printando o valor de manteiga
print(brownie_de_caneca) # e aqui já esta printando ele sem a chave manteiga

del brownie_de_caneca['açúcar'] # forma 2
print(brownie_de_caneca)

# Formas de utilizar o dict:

carrinho = []

produto1 = {'nome':'PlayStation', 'quantidade': 1, 'preço': 2300.00}
protudo2 = {'nome':'Mortal Combat', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(protudo2)
print(carrinho)

# OBS.: desta forma, facilmente adc ou removemos produtos do carrinho e em cada produto podemos ter a certeza sobre cada info

# Métodos de dict

d = dict(a=1,b=2,c=3)
print(d)
print(type(d))

# Limpando um dict

d.clear() # limpamos
print(d)

# Copiando um dict
d = dict(a=1, b=2, c=3)

novo_d = d.copy() # deep copy // forma 1
print(novo_d)

novo_d['d'] = 4 # acrescentei
print(novo_d)

d = dict(a=1, b=2, c=3)

novo_d = d
print(novo_d)

novo_d['d'] = 4 # forma 1 // shallow copy
print(d)
print(novo_d)

# Forma não usual de criação de dicts

outro = {}.fromkeys('a','b') # respectivamente chave:valor // 'a':'b'
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'salario', 'ferias'], 'desconhecido') # aqui ele irá gerar para cada valor iterável uma chave, e irá atribuir a esta chave o valor informado
print(usuario)
print(type(usuario))

nome = {}.fromkeys('bruna','melo') # para cada elemento de 'bruna' ele vai iterar o melo, e se tiver letra repetida ele irá ignorar
print(nome)
# OBS.: o método fromkeys irá gerar uma chave e um valor

nome = {}.fromkeys(range(1,6),'nome') # para cada elemento da range, será atribuido o novo valor "nome"
print(nome)
