'''teste = 'ELE1'
for i in teste:
    if i == 'L':
        print('Pass executado')
        pass
    print(i)

  for i in range(0, 200000):
    print(i)
    if i == 5:
        break

from random import randint
while True:
    x = randint(0, 10)
    print(x)
    if x == 5:
        break

for x in range(0, 10):
    if x == 5:
        continue
    print(x)

i = 1
while i <= 10:
    print(f'{i} ', end='')
    i = i + 1
print('\nFim!')

'''

n = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 111:
        break
    soma = soma + n
print(f'A soma é {soma}')
