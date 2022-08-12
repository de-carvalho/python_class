"""
* Criar variáveis para nome(str), idade(int),
* altura(float) e peso(float) de uma pessoa
* Criar variável de ano atual(int)
* Obter ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-strings (com chaves)
"""

nome = 'Ana Carolina'
idade = 24
altura = 1.77
peso = 100.0
ano_atual = 2022
ano_nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, pesa {peso}, nasceu em {ano_nascimento} e atualmente em {ano_atual} seu imc é de {imc:.2f}')
