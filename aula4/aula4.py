"""
Tipos de dados
str - string - textos 'Assim' ou "Assim"
int - inteiro - números que não tenham pontos que sejam negativos ou positivos
float - real/ponto flutuante -  número negativo ou positivo com pontos 10.50, 20.01, 1.5
bool - booleano/lógico - true or false

a maioria das coisas que estiverem vazias sera retornada como false
uma string vazia, uma lista vazia e etc

o número zero também é avaliado em false
"""
print(type('string'))
print(10, type(10))
print(25.23, type(25.23))
print('l' == 'l', type('l' == 'l'))
print(bool(''))
print(bool(0))

print(type(int('0')))

# String: nome
print('Ana Carolina', type('Ana Carolina'))

# Int: idade
print(23, type(23))

# Float: altura
print(1.77, type(1.77))

# É maior de idade
print(23 > 18, type(23 > 18))


