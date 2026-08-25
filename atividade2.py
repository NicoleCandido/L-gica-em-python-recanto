#Segunda questão - faça um programa que receba um número inteiro,
#logo depois o sistema deve falar se ele é impar ou par. 
#Usa % ao invés de mod 

num = int(input("Digite um número inteiro: "))

if num % 2 == 0:
    print("par")
else:
    print("Impar")