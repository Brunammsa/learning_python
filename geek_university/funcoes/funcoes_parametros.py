"""
Funções que recebem dados para serem processados dentro da mesma;

Se pensarmos em um programa qualquer, geralmente temos:
- entrada -> processamento -> saída

Se pensarmos em uma função, já sabemos que temos funções que:
- não possuem entradas;
- não possuem saída;
- possuem entrada, mas não saída;
- não possuem entrada, mas possuem saída;
- possuem entrada e saída;
"""

# Refatorando uma função

def quadrado(numero):
    #return numero * numero
    return numero ** 2

print(quadrado(4))
ret = quadrado(6)
print(ret)

def cantar_parabens(aniversariante):
    print('parabéns para você')
    print('nesta data querida')
    print('muitas felicidades')
    print('muitos anos de vida!')
    print('Viva a {}'.format(aniversariante))

cantar_parabens('Bruna')

""" Função pode ter vários parâmetros de entrada, ou seja, podemos receber como entrada em uma função, quantos parâmetros forem necessários;
Eles são separados por vírgula;
"""

# Exemplos

def soma(a, b):
    return a + b

def multiplica(numb1, numb2):
    return numb1 * numb2

def outra(numb1, b, msg):
    return (numb1 + b) * msg

print(soma(2, 2))
print(multiplica(2, 4))
print(outra(4, 6, 'oi '))

# OBS.: Se a gente informar um número errado no parâmtro ou argumento, teremos TypeError

# Nomeando parâmetros

def nome_completo(nome, sobrenome):
    return 'seu nome completo é {} {}'.format(nome, sobrenome)

print(nome_completo('Angelina', 'Joli'))

"""
Diferença entre parâmetros e argumentos:

- Parâmtros são variáveis declaradas na definção de uma função;
- Argumentos são dados passados durante a execução de uma função;
"""

# A ordem dos parâmetros importa!

nome = 'Victor'
sobrenome = 'Sá'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem;

print(nome_completo(nome='Bruna', sobrenome='Melo'))
print(nome_completo(nome= nome, sobrenome= sobrenome))
print(nome_completo(sobrenome='Marques', nome='Arthur'))

# Erros comuns no return

def soma_impares(numeros):
    total = 0
    for numb in numeros:
        if numb % 2 != 0:
            total = total + numb
    return total

lista = [1, 2, 3, 4, 5, 6]
print(soma_impares(lista))