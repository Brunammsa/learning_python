'''
- Funções são pequenas partes de códigos que realizam tarefas específicas;
- Pode ou não receber entrada de dados e retornar saída de dados;
- Muito úteis para executar procedimentos similares por repetidas vezes;

OBS.: Se você escrever uma função que realiza várias tarefas dentro delas, é bom fazer uma verificação para que a função seja verificada;
'''

#  Exemplo de utilização para funções já conhecidas
# Utilizando funções integradas (Bulti-in - que já vem na linguagem de programação)

cores = ['amarelo', 'rosa', 'azul', 'branco']
#print(cores)

curso = 'Programação em Python'
#print(curso)

cores.append('roxo')
#print(cores)

#curso.append('essencial') - AttributeError - não da p usar append em str

cores.clear() # limpa tudo
#print(cores)

''' 
Mas então, como definir uma função?

Em Python, a forma de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:

nome_da_funcao - SEMPRE COM LETRAS MINÚSCULAS E SE FOR NOME COMPOSTO, SEPARADO POR UNDERLINE (Snake Case);
parametros_de_entrada - são opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_funcao - também chamado de corpo da função, ou implementação, é onde o processamento da função acontece, neste bloco,
pode ter ou não retorno da função;

OBS.: Veja que para definir uma função, utilizamos a palavra reservada 'def', informando ao Python que estamos definindo uma função,
também abrimos o bloco de código com o já conhecido ':', que é utilizado em Python para definir blocos;
'''

# Definindo a primeira função

# exemplo 1
def diz_oi(): # ta vazio pq não tem nenhum parâmetro de entrada
    print('oi!')

'''
OBS.:

1- Veja que, dentro das nossas funções podemos utilizar outras funções;
2- Veja que nossa função só executa uma tarefa, ou seja, a única cois que ela faz é dizer oi;
3- Veja que esta função não recebe nenhum parâmetro de entrada;
4- Veja que nossa função não retorna nada;
'''
# Utilizando funções

diz_oi()

# ATENÇÃO: Nunca esqueça de utilizar os parênteses ao executar uma função

# exemplo 2
def cantar_parabens():
    print('parabéns para você')
    print('nesta data querida')
    print('muitas felicidades')
    print('muitos anos de vida!')

cantar_parabens()

# com repetição
for n in range(3):
    cantar_parabens()

# Em Python, podemos inclusive criar variáveis do tipo de uma função e executar esta função através da variável;

canta = cantar_parabens # não é comum, algunas linguagens não fazem isso, e nem tem para que fazer isso
canta()