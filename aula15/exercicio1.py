"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informa que não é um número inteiro.
"""

num1 = input('Digite um número: ')

if not num1.isdigit():
    print('Isso não é um número inteiro')
else:
    num1 = int(num1)

    print('Você digitou um número inteiro')

if not num1 % 2 == 0:
    print(f'{num1} é ímpar')
else:
    print(f'{num1} é par')
