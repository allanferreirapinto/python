'''
1. Crie um programa que lê 6 valores iteiros e, em seguida, mostre na tela os valores lidos.

lista = []
for i in range(0, 6):
    lista.append(int(input(f'Entre o com valor da posição {i}: ')))
print(f'A lista completa é {lista}')

2. Faça um programa que receba do usuário 5 valores e inserindo-os em uma lista. Em seguida
deverá ser impresso o maior e o menor elemento da lista.

lista = []
maior = menor = 0
for i in range(0, 5):
    lista.append(int(input(f'Digite o valor da posição {i}: ')))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
print(f'Os valores informados são {lista}')
print(f'O maior valor informado foi {maior}')
print(f'O menor valor informado foi {menor}')

3. Faça um programa que receba do usuário vários números inteiros coloque-os em uma lista.
Por fim, mostre uma lista com os números pares e outra lista com os números ímpares.

número = [list(), list()]
valor = 0
for i in range(1, 8):
    valor = int(input(f'Entre com o {i}º número: '))
    if valor % 2 == 0:
        número[0].append(valor)
    else:
        número[1].append(valor)
número[0].sort()
número[1].sort()
print(f'A lista com os valores pares foram: {número[0]}')
print(f'A lista com os valores ímpares foram: {número[1]}')

4. Crie um programa para o usuário inserir vários números em uma lista. Caso o número
informado já tenha sido inserido, ele deverá ser ignorado e não deve ser inserido na lista. Por
fim, mostre na tela os valores inserido em ordem crescente.

números = list()
while True:
    num = int(input('Digite um número inteiro qualquer: '))
    if num not in números:
        números.append(num)
    else:
        print('Número já informado! Informe outro valor...')
    resp = str(input('Deseja continuar informando valores? [S/N] '))
    if resp in 'Nn':
        break
números.sort()
print(f'Você digitou os valores {números}')

5. Faça um programa que leia vários números e adicione-o em uma lista. Mostre na tela quantos
números foram digitados, a lista ordeanda em ordem decrescente e se o valor 8 foi digitado
ou não na lista.

'''

números = []
while True:
    números.append(int(input('Digite um número inteiro qualquer: ')))
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'Você digitou {len(números)} números.')
números.reverse()
print(f'Os números em ordem decrescente são {números}')
if 8 in números:
    print('O valor 8 está na lista!')
else:
    print('O valor 8 não está na lista!')
