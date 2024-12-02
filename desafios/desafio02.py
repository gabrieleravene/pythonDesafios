# verificador de palíndromos

# peça ao usuário para digitar uma palavra ou frase
#verifique se a entrada é um palíndromo (ou seja, se a palavra ou frase é igual quando lida de trás pra frente
# ignorando espaços e diferenças entre maiúsculas e minúsculas
# exiba uma mensagem dizendo se a entrada é ou não um palíndromo

str = input('Digite uma palavra ou frase: ')

str = str.replace(" ", "").lower()

if str == str[::-1]:
    print(f'A palavra ou frase {str} é um palíndromo!')
else:
    print(f'A palavra ou frase {str} NÃO é um palíndromo!')

