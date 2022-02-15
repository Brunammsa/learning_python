import sys
nome_do_comando = sys.argv[1]

if (nome_do_comando == "cd"):
    print("O comando '"+ nome_do_comando + "' muda de diretório, só preciso dizer para qual pasta devo ir cd Desktop ou cd C:\\")
elif(nome_do_comando == "dir"):
    print("O '" + nome_do_comando + "' mostra o conteúdo da pasta(diretório) atual")
elif(nome_do_comando == "cls"):
    print(nome_do_comando + " eu conheço sim, ele apaga tudo no cmd")
else:
    print("Bruna ainda não conheceu esse comando '" + nome_do_comando+"'")