from random import randint


vetor_a = [1,1,1,1,1,1,1,1,1,1]
vetor_b = [2,2,2,2,2,2,2,2,2,2]
vetor_c = []
"""
for elementos in range(10):
    numeros_a = randint(0, 9)
    vetor_a.append(numeros_a)
    numeros_b = randint(0,9)
    vetor_b.append(numeros_b)"""
print(vetor_a)
print(vetor_b)

index = 0
for index in range(10):
    if index % 2 == 0:
        vetor_c.append(vetor_a[index])
    elif index % 2 != 0:
        vetor_c.append(vetor_b[index - 1])
    index += 1
            
print('{}\n'.format(vetor_c))
print(len(vetor_c))

# ta certo, mas ta errado