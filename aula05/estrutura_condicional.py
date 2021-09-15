'''
Controle de fluxo - Estruturas condicionais

Condicional simples
x = int(input('Digite um número: '))
if x < 10:
    print('x<10')
print('Bom dia!')

Condicional composta
x = int(input('Digite um número: '))
if x < 10:
    print('x<10')
else:
    print('x>10')
print('Bom dia!')

Condicional aninhada
x = int(input('Digite um número: '))
if x < 10:
    print('x<10')
elif x == 10:
    print('x=10')
else:
    print('x>10')
print('Bom dia!')

ou

x = int(input('Digite um número: '))
if x < 10:
    print('x<10')
elif x == 10:
    print('x=10')
elif x > 10:
    print('x>10')
print('Bom dia!')
'''

x = int(input('Digite um número: '))
if x < 10:
    print('x<10')
elif x == 10:
    print('x=10')
else:
    print('x>10')
print('Bom dia!')
