"""
Operadores lógicos - Aula 2
and = vai realizar duas comparações (as duas expressões devem ser verdadeiras)
or = pergunta se uma das comprações é verdadeira
not = inverte o valor da expressão
in = para verificar se um valor existe dentro de uma expressão
not in

Para realizar duas comparações ou mais
"""

a = 3
b = 5
c = 3
d = 4

nome = 'Ana Carolina'

# Aqui estou perguntando se a tem o mesmo valor que c e se o valor de c é menor do que d
# As duas comparações devem ser verdadeiras para retornar TRUE, caso uma não seja vai retornar FALSE
print(a == c and c < d)

# Aqui estou perguntando se d é maior que b ou se d tem o mesmo valor que c
# Uma das duas comparações deve ser verdadeira para retornar TRUE
print(d < b or d == c)

# Aqui estou perguntando se algo existe dentro da variável
if 'Mir' in nome:
    print('Existe')
else:
    print('Não existe')

# Aqui estou perguntando se algo NÃO existe dentro da váriavel, se não existir vai retornar TRUE
if 'An' not in nome:
    print('Não esta presente')
else:
    print('Esta presente')

senha = ''

# Aqui estou validando se existe um valor dentro da variável
if not senha:
    print('Por favor informe sua senha')
else:
    print('Senha correta')


usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'ana'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você esta logado no sistema')
else:
    print('Usuário ou senha inválidos')







