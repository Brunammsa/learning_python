"""
Funções com Parâmetros Padrão (Default Paramters)
- Funções onde a passagem de parâmetro seja opcional;
"""

def exponencial(numero=2, potencia=2): # aqui a potencia esta pré determinada como 2
    return numero ** potencia

print(exponencial(3)) # mesmo se não colocarmos a potencia, ela vai automaticamente pelo padrão pré estabelecido, o 2
print(exponencial(3, 3)) # aqui foi estabelecida outra potencia, então ela subscreve a pré estabelecida, agora valendo 3 para está operação
print(exponencial()) # aqui também podemos deixar sem parâmetros, afinal, já pré estabelecemos eles na função

# Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração
'''
Ex.:

def teste(num=2, potencia):  ERRADO, o certo seria: potencia, num=2
    return numb ** potencia

print(teste(6)) pq aqui, eu estou definindo um valor para a primeira posição, e no caso errado, a potencia fica se número, então inverte e deixa a 
                potencia subscrevendo e já define a seg posição
'''

# Outros exemplos:

def soma(numb1, numb2):
    return numb1 + numb2

print(soma(4, 3))
# print(soma(4)) TypeError
# print(soma())  TypeError

'''
Por quê utilizar parâmetros com valor default?
- nos permite ser mais flexíveis nas funções;
- evita erros com parâmetros incorretos;
- nos permite trabalhar com exemplos mais legíveis de código;
'''

''' Quais tipos de dados podemos utilizar como valores default para parâmetro?
- números, strings, floats, booleanos, listas, tuplas, dicts, funções, etc.
'''
# Exemplos

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões

# Variáveis globais
# Variáveis locais

instrutor = 'geek' # variável global

def  diz_oi():
    instrutor = 'python' # variável local, se sobrepõe a global
    return 'Oi, {}'.format(instrutor)
print(diz_oi())

def diz_oi():
    prof = 'geek' # variável local
    return 'olá {}'.format(prof)
print(diz_oi())
# print(prof) # a variável local não existe fora do escopo, por isso dará NameError

# Atenção com variáveis globais, e se puder, evite

total = 0
# jeito errado
def incrementa():
#   total = total + 1  UnboundLocalError (o segundo total nao foi inicializado para ser realizada a soma com + 1)
    return total
print(incrementa())
# jeito certo
def incrementa():
    global total # agora estamos identificando a variável como global
    total = total + 1 
    return total
print(incrementa())
print(incrementa())
print(incrementa())

# Podemos ter funções que são declaradas detro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contador = 0
    def dentro():
        nonlocal contador # definindo que não é uma variável local e como também não é global, ela está numa função anterior

        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())