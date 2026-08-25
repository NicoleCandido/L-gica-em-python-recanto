#Primeira Questão - Faça um programa que peça duas notas, 
# depois calcule a média delas e coloque:
# se a media for maior ou igual 7 = "Aprovado"
# se for menor ou igual a 6 = "Reprovado"

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
media = (nota1 + nota2) / 2 

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")