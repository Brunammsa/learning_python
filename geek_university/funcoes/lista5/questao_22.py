def linha_de_exclamacao_sem_return(n=5):
    for i in range(1, n + 1):
        linha = i * '!'
        print(linha)

linha_de_exclamacao_sem_return()


def linha_de_exclamacao_com_return(n=5):
    bloco_de_exclamacoes = ''
    for i in range(1, n + 1):
        linha = i * '!'
        linha += '\n'
        bloco_de_exclamacoes += linha
    return bloco_de_exclamacoes

print(linha_de_exclamacao_com_return())
