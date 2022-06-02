
def quantidade(habitantes):
    soma = 0

    for habitante in habitantes:
        if habitante[0] == "f" and habitante[1] == "a" and habitante[2] == "l" and habitante[3] > 18 and habitante[3] < 35  :
            soma += 1

    return soma

def maior_idade_habitantes(habitantes):
    maior_idade = float("-inf")

    for habitante in habitantes:
        if habitante[3] > maior_idade:
            maior_idade = habitante[3]
        
    return maior_idade


def media_idade_habitantes(habitantes):
    soma_idade = 0

    for habitante in habitantes:
        soma_idade += habitante[3]

    media_hab = soma_idade/len(habitantes)

    return media_hab


def pergunta_com_alternativa(texto_pergunta, respostas_validas):
    resposta = None

    while resposta not in respostas_validas:
        if resposta != None:
            print('resposta inválida')
        resposta = input(texto_pergunta)

    return resposta


def pergunta_ibge():
    resposta_sexo = pergunta_com_alternativa("qual o seu sexo? ", ["f", "m"])
    resposta_olhos = pergunta_com_alternativa("qual a cor dos seus olhos? ", ["a", "c"])
    resposta_cabelo = pergunta_com_alternativa("qual a cor do seu cabelo? ", ["l", "p", "c"])
    resposta_idade = int(input("qual sua idade? "))

    return [resposta_sexo, resposta_olhos, resposta_cabelo, resposta_idade]

quantidade_de_habitantes = 2
habitantes = []

for pessoa in range(1, quantidade_de_habitantes + 1):
    print("agora é a vez da {}ª pessoa".format(pessoa))

    habitantes.append(pergunta_ibge())

print(habitantes)

media = media_idade_habitantes(habitantes)
print(media)

maior = maior_idade_habitantes(habitantes)
print(maior)

quantidade_individuos = quantidade(habitantes)
print(quantidade_individuos)