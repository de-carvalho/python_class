"""
Operadores relacionais - servem para criar comparações entre coisas
== igualdade
> maior que
>= maior que ou igual a
< menor que
<= menor que ou igual a
!= diferente
"""

nome = input('Qual o seu nome?: ')
idade = int(input('Qual a sua idade?: '))

# Limite para pegar empréstimo
idade_menor = 20  # Muito jovem
idade_maior = 30  # Passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo')
else:
    print(f'{nome} NÃO pode pegar o emprésitmo')

