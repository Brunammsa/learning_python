a = 2
b = 2

print(a/b)

#obs1: agora, se eu colocar um numero que não de para dividir ele vai dar erro, ai utiliza-se o try
c = 2
d = 0
try:
    print(c/d)
except:
    print("nao eh possivel por 0")
#duvida: é como se fosse o else?