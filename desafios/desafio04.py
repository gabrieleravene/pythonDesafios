# cadastro de pessoas
# criar uma classe chamada Pessoa com atributos:
# nome (string)
# idade (inteiro)
# email (string)
# a classe deve ter um método chamado exibir_informações
# que exiba as informações da pessoa em formato amigável
# no programa principal:
# crie 3 objetos da classe Pessoa, com dados fornecidos pelo usuário
# armazene os objetos em uma lista
# exiba as informações de todas as pessoas cadastradas

class Pessoas:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def exibir_info(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Email:{self.email}")

pessoas = []

for _ in range(3):
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    email = input('Digite o email: ')

    pessoa = Pessoas(nome, idade, email)
    pessoas.append(pessoa)


print("\nInformações das pessoas cadatradas:")
for pessoa in pessoas:
    pessoa.exibir_info()