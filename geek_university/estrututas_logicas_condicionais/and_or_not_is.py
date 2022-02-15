"""
Estruturas lógicas: and, or, not, is

operadores unários:
    - not
operadores binários:
    - and, or, is

para o "and", ambos os valores precisam ser True
para o "or", um ou outro precisa ser True
para o "not", o valor do booleano é invrtido, ou seja, se for True, vira false, se for False, vira True (operador de negação)
"""
ativo = False
logado = True


if ativo or logado: #binário
    print("bem vindo, usuário!")
else:
    print("Você precisa está ativo, por favo cheque seu e-mail")


"""
if not ativo: #unário
    print("por favor, verifique seu email para ativar sua conta novamente")
else:
    print("bem vindo, usuário!")
"""