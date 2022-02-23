valor_de_a = int(input("Escolha um número de 1 a 100: "))
valor_de_b = int(input("Escolha outro número de 1 a 100: "))

pergunta1 = input("Qual é o resultado da soma dos números escolhidos:{} + {}: ?\n".format(valor_de_a, valor_de_b))
pergunta2 = input("Qual é o resultado da divisão dos números escolhidos:{} / {}: ?\n".format(valor_de_a, valor_de_b))
pergunta3 = input("Qual é o resultado da multiplicação dos números escolhidos:{} x {}: ?\n".format(valor_de_a, valor_de_b))
pergunta4 = input("Digite a diferença entre os números escolhidos:\n")
pergunta5 = input("Quem é o menor dos números escolhidos:{} ou {}: ?\n".format(valor_de_a, valor_de_b))

if valor_de_a < 0 and valor_de_a > 100 and valor_de_b < 0  and valor_de_b > 100:
    print("Valor inválido, por favor, digite um número de 1 a 100")
    if pergunta1 == valor_de_a+valor_de_b:
        print("Parabéns, você acertou a primeira questão!")
    else:
        print("Você errou, tente novamente")
    if pergunta2 == valor_de_a/valor_de_b:
        print("Parabéns, você acertou a segunda questão!")
    else:
        print("Você errou, tente novamente")
    if pergunta3 == valor_de_a*valor_de_b:
        print("Parabéns, você acertou a terceira questão!")
    else:
        print("Você errou, tente novamente")
    if pergunta4  == valor_de_a-valor_de_b:
        print("Parabéns, você acertou a quarta questão!")
    else:
        print("Você errou, tente novamente")
    if pergunta5 == valor_de_a < valor_de_b:
        print("o número {} é o maior é do que {}".format(valor_de_a, valor_de_b))
    else:
        print("o número {} é o maior é maior do que {}".format(valor_de_b, valor_de_a))
else:
    print("")

#tudo errado, não to conseguindo fazer