import sys

valor_de_a = int(input("Escolha um número de 1 a 100: "))

if valor_de_a <= 0 or valor_de_a >= 100:
    print("Número inválido")
    sys.exit()

valor_de_b = int(input("Escolha outro número de 1 a 100: "))

if valor_de_b <= 0 or valor_de_b >= 100:
    print("Número inválido")
    sys.exit()

# usar isso p não precisar encher de if
def verifica_resposta(resposta_da_questao, resposta_do_usuario, quantidade_de_acertos):
    if resposta_da_questao == resposta_do_usuario:
        print("Parabéns, você acertou!")
        quantidade_de_acertos = quantidade_de_acertos + 1
    else:
        print("Resposta errada")

    return quantidade_de_acertos

quantidade_acertos = 0

pergunta1 = int(input("Qual é o resultado da soma {} + {}?\n".format(valor_de_a, valor_de_b)))
resposta1 = valor_de_a + valor_de_b

quantidade_acertos = verifica_resposta(resposta1, pergunta1, quantidade_acertos)


pergunta2 = int(input("Qual é o resultado da soma {} + {}²?\n".format(valor_de_a, (valor_de_b))))
resposta2 = valor_de_a + (valor_de_b**2)

quantidade_acertos = verifica_resposta(resposta2, pergunta2, quantidade_acertos)


pergunta3 = int(input("Qual é o resultado da soma {} + ({}-{}?)\n".format(valor_de_a, valor_de_a, valor_de_b)))
resposta3 = valor_de_a + (valor_de_a - valor_de_b)

quantidade_acertos = verifica_resposta(resposta3, pergunta3, quantidade_acertos)


pergunta4 = int(input("Qual o resultado da soma {}³ + {}²?\n".format(valor_de_a, valor_de_b)))
resposta4 = (valor_de_a**3) + (valor_de_b**2)

quantidade_acertos = verifica_resposta(resposta4, pergunta4, quantidade_acertos)


pergunta5 = int(input("Qual o resultado da soma {} x {} + {} x {}?\n".format(valor_de_a, valor_de_b, valor_de_b, valor_de_a)))
resposta5 = (valor_de_a*valor_de_b) + (valor_de_b * valor_de_a)

#função com parâmetros nomeados
quantidade_acertos = verifica_resposta(quantidade_de_acertos = quantidade_acertos, resposta_da_questao = pergunta5, resposta_do_usuario = resposta5)


print("O aluno acertou {} questões".format(quantidade_acertos))

