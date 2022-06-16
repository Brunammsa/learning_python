"""
Filter

filter() serve para filtrar dados de uma determinada coleção;

"""
# biblioteca para trabalhar com dados estatísticos
# import statistics (não quer pegar na minha versã)

dados = [1.2, 5.5, 9.2, 3.4]

# media = statistics.mean(dados) (precisa do import)
media = sum(dados)/len(dados)

# Assim como a função map(), o filter() recebe dois parâmetros (uma funçao e um iterável);
res = filter(lambda x: x > media, dados)
print(list(res))

# OBS.: Assim como na função map(), após serem utilizados os dados de filter() eles serão excluídos da memória;

paises = ["brasil", "EUA", "", "argentina", "", "", "colombia", ""]
# Jeito 01
res = filter(None, paises)
print(list(res))
# Jeito 02
res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))


"""
Diferenças entre map() e filter ()

map() -> recebe dois parâmetros, uma função e um iterável, e retorna um objeto mapeando a função para cada elemento do iterávl

filter() -> recebe dois parâmetros, uma função e um iterável, e retorna um objeto, filtrando apenas os elementos de acordo com a função
"""

# Exemplo complexo

usuarios = [
    {"usurname": "tenorio", "tweets": []},
    {"usurname": "bruna", "tweets": ["eu amo caranguejo", "amo dormir", "gosto de assistir pantanal"]},
    {"usurname": "felipe", "tweets": ["adoro diablo immortal", "e assistir anime"]},
    {"usurname": "bruno", "tweets": []},
    {"usurname": "vanessa", "tweets": ["bora tomar uma breja"]}
]

inativos = list(filter(lambda usuario: len(usuario["tweets"]) == 0, usuarios))
print(inativos)

# Combinando filter() e map()

nomes = ["Vanessa", "Julia", "Renata", "Ana", "tt"]

lista = list(map(lambda nome: "sua instrutora é {}".format(nome), filter(lambda nome: len(nome) < 5, nomes)))
print(lista)