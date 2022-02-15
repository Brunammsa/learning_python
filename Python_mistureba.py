print("oi, gatinho!")
print ("olha o que eu to escrevendo rumrum")
print ("aprendi a usar o coisa embaixo")
#aqui é comentário, não aparece embaixo
print ("mas aqui continua")
"""
blablabla
blablabla
blablabla
"""
print ("hihihih")
#-*- coding: utf-8 -*-
print ("água")
print (2+2)
print (10%3)
minha_variavel = "mensagem repetida"

print (minha_variavel)
print (minha_variavel)
print (minha_variavel)

var1 = 1 # variável inteira
var2 = 1.1 # variável flutuante
var3 = "sou string" # variável string
var4 = "true" # verdadeiro
var4 = "false" #falso

print (var1)
print (var2)
print (var3)
print (var4)

x = 1
y = 3

y == x
print (y == x)

x = 2
y = 2
z = 2

x == y
print (x == y)

var5 = x + y
print(var5 == x)
print(x == y and y == z)
print(y == z or y == x)


a = 1
b = 1000000000
if a > b:
	print ("a é maior do que b")

if b > a:
	print ("b é maior do que a")

r = 3
s = 5
if r > s:
	print("r é maior do que s")
elif s < r:
	print("s é maior do que r")
else:
	print("são diferentes")



teletubbies = "cor de burro qnd foge"
if (teletubbies == "roxo"):
	print ("tinky-winky")
elif (teletubbies == "verde"):
	print ("dipsy")
elif (teletubbies == "vermelho"):
	print ("poo")
elif (teletubbies == "amarelo"):
	print ("lala")
else:
	print ("não tem essa cor")

x = 10
while(x < 20):
	print(x)
	x +=1 # x = x + 1

lista1 = ["bruna", "renata", "vanessa"]

lista2 = [1, 2, 3]
lista3 = ["bruna", 5]
for i in lista1:
	print(i)

for i in range(10,20):
	print(i)

	#como verificar atributos a objetos e métodos:
	#objeto.atributo
	#objeto.método()

x = "Bruna de Melo"
b = "felipe"

contatenar = x + " "+ "e" + " " + b
print(contatenar) #junção de strings

tamanho = len(contatenar)
print(tamanho) #por quê o print ta sem identação?

print(x[2]) #contagem de posição
print(b[5])

print(x[3:]) #printar partido, exclui até a posição 3 até o final

print(x.lower()) #p imprimir tudo minúsculo
print(x.upper()) #p deixar tudo maiúsculo
#tem que ter .função() parênteses vazio msm

concatenar = x + " " + b + "\n"
print(concatenar)

#se eu quiser remove o espaço que dei com o \n é só usar strip
print(concatenar.strip())

teste_string = "roupa suja chão sujo"

minha_lista = teste_string.split("a") 

#separa as palavras e o (" ") coloca espaço entre elas (" " é opcional, pode ser só ())
#se eu quiser tirar alguma letra, fazer uma quebra, só por a letra que quero entre ("x")
print(minha_lista)

minha_lista = teste_string.find("chão")
print(minha_lista)
#find procura a posição que se inicia a palavra escolhida

print(teste_string[minha_lista:])
#ele vai imprimir sua busca até o final, a busca começou com o chão, na linha 133 onde o find selecionou

minha_lista = teste_string.find("parede")
print(minha_lista)
#quando ele não encontra, ele coloca -1

minha_lista = teste_string.replace("chão", "parede")
print(minha_lista)
#esse comando do replace substitui a palavra por outra

def soma(x, y):
	return x+y
def multi(x, y):
	return x*y
s = soma(2, 3)
m = multi(2, 3)
print(s)
print(m)
print(soma(s,m))
#muito confuso função...

arquivo = open("arquivo.txt")
linhas = arquivo.readlines() 
for linha in linhas:
	print(linha)
#le o arquivo que eu importei com open, linha a linha, retorna array de linhas, da um espaço

linhas = arquivo.read()
print(linhas)
#quebra espaço como o \n


arq = open("exemplo.txt", "w")
arq.write("algo aqui dentro")
arq.close()