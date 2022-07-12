"""
Try/ Except/ Else/ Finally

** Quando e onde deve tratar o código? **
- Toda entrada deve ser tratada;

- Else, igual no if, só será executado se a opção acima não for, no caso para tratamento de erros, não ocorrer o erro;

- O bloco finally será sempre executado, independente se houver except ou não, geralmente sendo utilizado para fechar 
ou deslocar recursos;
"""

# Exemplo try com else:

try:
    num = int(input("informe um número: "))
except ValueError:
    print("Valor incorreto")
else:
    print(f"você digitou {num}")

# Exemplo try com else e finally:

try:
    num = int(input("informe um número: "))
except ValueError:
    print("Valor incorreto")
else:
    print(f"você digitou {num}")
finally:
    print("Execução finalizada, obrigada!")

# Exemplo complexo cornojob:

def dividir(a, b):

    return a/b

try:
    num_1 = int(input("informe o primeiro número: "))
except ValueError:
    print("o primeiro valor está incorreto, digite apenas número")

try:
    num_2 = int(input("informe o segundo número: "))
except ValueError():
    print("o segundo valor está incorreto, digite apenas número")

try:
    print(dividir(num_1, num_2))
except NameError:
    print("algum valor está incorreto, favor verificar e digitar apenas números.")

# Exemplo complexo correto, pythonica:

def soma(x, y):
    try:
        return int(x) / int(y)
    except ValueError:
        return "Alguma saída está incorreta, favor verificar e digitar apenas números."
    except ZeroDivisionError:
        return "Não é possível realizar uma divisão por zero, favor tentar outro número."
num_x = input(("Digite o primeiro número: "))
num_y = input(("Digite o segundo número: "))

print(soma(num_x, num_y))

# OBS.: poderíamos tratar vários erros num except só, mas ficaria genérico, a não  que se coloque um apelido para especificar:

def soma(x, y):
    try:
        return int(x) / int(y)
    except (ValueError, ZeroDivisionError) as err:
        return f"Ocorreu um erro: {err}. Favor verificar e tentar novamente."

num_x = input(("Digite o primeiro número: "))
num_y = input(("Digite o segundo número: "))

print(soma(num_x, num_y))
