# soma de números pares
# peça ao usuário para digitar um número inteiro positivo
# verifique se o número é positivo, caso contrário peça novamente até que seja fornecido um número válido
# calcule e exiba a soma de todos os números pares de 1 até o número informado pelo usuário

num = int(input('Digite um número inteiro positivo: '))

while num < 0:
    num = int(input('Digite um número inteiro positivo: '))

soma = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        soma += i

print(f'A soma dos números pares de 1 até {num} é {soma}.')
