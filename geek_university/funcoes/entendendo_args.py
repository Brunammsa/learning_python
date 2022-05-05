"""
O args é um argumento como outro qualquer. Isso significa que você poderá chamar de qualquer coisa, desde que comece com um arterísco.
"""
# normal
def soma(num1, num2, num3):
    return num1 + num2 + num3

print(soma(1, 3, 4)) # se colocar mais ou menos argumentos dará TypeError

# com *args
def soma_todos_os_numeros(*args): # apenas para int, se quiser entrar com uma strg, abra outro argumento por ex. (nome, *arg) ai pode retornar ('bruna', 1)
    return sum(args)

print(soma_todos_os_numeros())
print(soma_todos_os_numeros(1))
print(soma_todos_os_numeros(1, 2))
print(soma_todos_os_numeros(1, 2, 3))

# outro exemplo utilizando args
def verifica_info(*args):
    if 'geek' in args and 'university' in args:
        return 'bem vindo'
    return 'eu não tenho certeza de quem você é...'

print(verifica_info()) # não é obrigado retornar algo
print(verifica_info(1, True, 'geek', 'university'))
print(verifica_info(1, 'university', 443))

numero = [1, 2, 3, 4, 5]
# print(soma_todos_os_numeros(numero)) não vai pegar porque é uma lista, mas podemos desempacotar

num1, num2, num3, num4, num5 = numero
print(soma_todos_os_numeros(num1, num2, num3, num4, num5)) # ou
print(soma_todos_os_numeros(*numero))

""" OBS.: o asterísco serve para informarmos ao Python que estamos passando um argumento com coleção de dados, desta forma, ele saberá que precisará
antes desempacotar estes dados
"""