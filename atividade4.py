#Quarta questão - Faça um programa que peça a idade do usuário e depois mostre as seguintes 
# informações:
# Se ele tiver entre 0 até 12 anos mostre: criança
# Se ele tiver entre 13 até 17 anos mostre: adolescente
# Se ele tiver entre 18 até 25 anos mostre: jovem adulto
# Se ele tiver entre 26 até 59 anos mostre: adulto
# Se ele tiver mais de 60 anos mostre: idoso

idade = int(input("Digite sua idade: "))

if idade <= 12:
    print("O usuario é uma criança")
elif idade <= 17:
    print("O usuario é um adolescente")
elif idade <= 25:
    print("O usuario é um jovem adulto")
elif idade <= 59:
    print("O usuario é um adulto")
else:
    print("O usuario é um idoso")