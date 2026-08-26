#Façam um programa que guarde 4 notas de 3 alunos, onde:
#O codigo deve pecorrer linha por linha,
#para cada aluno, calcule a soma das 4 notas e a depois dê a média delas,
#Diga se o aluno foi "Aprovado" (média >=6.0) ou Reprovado.
#Por fim deve imprimir, a média tirada e se foi aprovado ou reprovado.

notas = [
    [9.5, 6.7,5.4, 8.5],
    [7.5, 5.3,3.4, 8.7],
    [3.4, 7.8,4.5, 9.0]
]

for linha in notas:
    numero_aluno = 1
    soma = 0
    for nota in linha:
        soma = soma + nota

    media = soma/len(linha)

    if media >= 6.0:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print(f"Aluno{numero_aluno}: média{media:.2f}-{situacao}")
numero_aluno += 1