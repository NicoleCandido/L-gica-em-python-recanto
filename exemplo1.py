#Faça um programa que adapte para 
# calcular a soma de números 
#DIGITADOS PELO USUÁRIO
#"Usar o input, dentro do LOOP, ler N
# vezes."

soma = 0
for i in range(1,9):
    numero = int(input("Digite um numero:"))
    soma = soma + numero
print("A soma dos numeros é: ", soma)