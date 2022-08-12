num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

# Vai checar números positivos isnumeric isdigit isdecimal
# (essas funções verificam se os valores retornados na string podem ser convertidos para números inteiros
"""
print(num1.isnumeric())
print(num2.isnumeric())
"""

# Aqui eu pesso para o Python tentar interpretar e executar o código
try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('ERROR')



