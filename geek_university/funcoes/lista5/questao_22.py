def linha_de_exclamacao(n=5):
    for i in range(1, n + 1):
        linha = i * '!'
    return linha
print(linha_de_exclamacao())

for i in range(1, 5 + 1):
    linha = i * '!'
    print(linha)
