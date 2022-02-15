arquivo = open("testes0x.txt", "a")

arquivo = open("testes0x.txt", "w")
frases = list()
frases.append("bruno barros, 28 \n")
frases.append("bruna melo, 28 \n")
frases.append("vanessa morais, 28 \n")

arquivo.writelines(frases)

arquivo = open("testes0x.txt", "r")
linha = arquivo.readline()
while(linha):
    valores = linha.split(" ")
    primeiro_nome = valores[0]
    idade = valores[len(valores) -1].strip()
    print(primeiro_nome + "tem" + idade + "anos")

    linha = arquivo.readline()

    arquivo.close()



