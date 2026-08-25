#Faça um programa que receba três pontos, onde ele mostrs qual dos três pontos
#é maior

p1 = float(input("Digite ponto 1: "))
p2 = float(input("Digite ponto 2: "))
p3 = float(input("Digite ponto 3: "))

if p1 > p2 and p1 > p3:
    print("O maior numero é o ponto 1: ")
elif p2 > p1 and p2 > p3:
    print("O maior numero é o ponto 2: ")
else:
    print("O maior numero é o ponto 3: ")