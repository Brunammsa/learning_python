def notas_alunos(nota1, nota2, nota3, letra):
    if letra == 'a':
        media_aritimetica = (nota1 + nota2 + nota3) / 3
        return media_aritimetica
    elif letra == 'p':
        media_ponderada = ((nota1 * 5) + (nota2 * 3) + (nota3 * 2)) / (5 + 3 + 2)
        return media_ponderada
    
print(notas_alunos(6, 5, 8, 'a'))
print(notas_alunos(6, 5, 8, 'p'))