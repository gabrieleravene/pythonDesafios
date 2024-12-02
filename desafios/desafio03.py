# adivinhe o número

# o programa deve gerar aleatoriamente um número inteiro entre 1 e 100 (usar módulo random)
# peça ao usuário para adivinhar o número gerado
# informe ao usuário se o núero digitado é maior, menor ou igual ao número gerado
# repita o processo até que o usuário acerte o número
# quando o usuário acertar, exiba o número de tentativas realizadas

import random
from idlelib.sidebar import temp_enable_text_widget
from urllib.parse import uses_relative

num = random.randint(1, 100)

user_num = int(input('Tente adivinhar o número de 1 a 100: '))

tentativas = 0

while user_num != num:

    if user_num > num:
        print(f'É menor do que {user_num}. Tente novamente.')
    else:
        print(f'É maior do que {user_num}. Tente novamente.')

    tentativas += 1
    user_num = int(input('Tente adivinhar o número de 1 a 100: '))

tentativas += 1
print(f'Você acertou! Você acertou o numero {num} em {tentativas} tentativas.')