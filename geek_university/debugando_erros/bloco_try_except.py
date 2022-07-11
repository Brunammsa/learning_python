"""
Bloco Try/Except - Tratamento de erro

- Utilizamos para tratar erros que podem ocorrer no nosso código, prevenindo que o código pare de funcionar e o usuário receba
mensagens de erros inesperadas;

A forma geral mais simples é:

** exemplo de erro genérico **

try:
    geek()
except:
    print("Há algum problema aqui")

OBS.: a melhor forma de tratar erros, são de forma específica.

** exemplo de erro específico **
OBS.: podemos tratar vários tipos de erros juntos

try:
    len("bruna"[6])
except TypeError as erra:                                     # por o tipo de erro que estiver tentando
    print(d"A aplicação gerou o seguinte erro: {err}")        # no err vai dizer qual tipo de erro
except NameError as errb:
    print(d"A aplicação gerou o seguinte erro: {err}")
except:
    print("Deu um erro diferente")

"""