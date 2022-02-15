arquivo = open("pastatestes.txt", "a") #criar pasta ou abrir existente

arquivo.write("aba daba du \n") #escreve dentro do arquivo
frases = list()
frases.append("Fred \n")
frases.append("Pedrita \n")
frases.append("Bambam \n")
frases.append("Barney \n")
arquivo.writelines(frases) #escreve várias linhas


arquivo = open("pastatestes.txt", "r") #ler caracteres
print(arquivo.readline(3)) #aqui pedi p ele ler 3, no caso, aba da primeira linha
print(arquivo.readlines())

arquivo.close()