"""
Contar caracteres dentro de uma string
"""

usuario = input('Digite um nome de usuário: ')
qtd_caracteres = len(usuario)
print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres')
else:
    print('Você foi cadastrado no sistema')

string1 = input('Digite uma coisa: ')
string2 = input('Digite uma outra coisa: ')

print(f' A quantidade total de caracteres digitados foi {len(string1) + len(string2)}')
