# números primos
# peça para o usuário digitar um número inteiro positivo
# verifique se o número é primo
# exiba uma mensagem informando se o número é primo ou nao
# regra: um número é primo se for maior que 1 e divisível apenas por 1 e por ele mesmo

num = int(input('Digite um número: '))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f'O número {num} não é primo.')
            break
    else:
        print(f'O número {num} é primo.')