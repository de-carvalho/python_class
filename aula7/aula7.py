"""
Exibição de valores formatados
"""

nome = 'Ana Carolina'
idade = 23
altura = 1.78
e_maior = idade > 18
peso = 100
imc = peso / (altura * altura)

# F-string serve para podermos declarar as váriaveis com chaves dentro de uma string
# .2f -> Serve para formatar as casas decimais de um número do tipo float
print(f'{nome} tem {idade} anos de idade e seu imc é de {imc:.2f}')
print('{} tem {} anos e seu imc é de {:.2f}'.format(nome, idade, imc))  # não preencher as chaves neste formato


