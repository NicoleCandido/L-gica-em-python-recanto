#Faça um programa que conte quantos numeros impares 
# e numeros pares foram digitados. Pelo Usuário;
#Usando estrutura de decisão dentro do loop.
#Formula para números pares(n % 2 == 0)

impar = 0
par = 0

for i in range(1,11):
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
print("Numeros pares digitados: ", par)
print("Numeros impares digitados: ", impar)