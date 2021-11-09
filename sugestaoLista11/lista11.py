'''
1. Escreva um programa que mostre na tela a seguinte contagem: 6 7 8 9 10 11 Acabou!

for i in range(6, 12):
    print(i)
print('Acabou')

2. Faça um programa que mostre na tela a seguinte contagem: 10 9 8 7 6 5 4 3 Acabou!

for cont in range(10, 2, -1):
    print(cont)
print('Acabou!')

3. Crie um programa que mostre na tela a seguinte contagem: 0 3 6 9 12 15 18 Acabou!

for i in range(0, 19, 3):
    print(i)
print('Acabou!')

4. Desenvolva um programa que mostre na tela a seguinte contagem: 100 95 90 85 80 ... 0 Acabou!

for i in range(100, -1, -1):
    print(i)
print('Acabou!')

5. Faça um programa que pergunte ao usuário um número inteiro e positivo qualquer e mostre
uma contagem até esse valor:
Ex: Digite um valor: 35
Contagem: 1 2 3 4 5 6 7 ... 33 34 35 Acabou!

número = int(input('Digite um valor: '))
for i in range(0, número + 1):
    print(i)
print('Acabou!')

6. Faça um programa que receba um número inteiro, e verifique se o número fornecido é primo
ou não.

número = int(input('Digite um número: '))
qtde = 0
for i in range(1, número + 1):
    if número % i == 0:
        print(end='')
        qtde += 1
    else:
        print(end='')
    print(f'{i} ', end='')
print(f'\nO número {número} foi divisível {qtde} vezes')
if qtde == 2:
    print('Portanto, é um número PRIMO!')
else:
    print('Portanto, não é um número primo!')

7. Faça um programa que receba o peso de 10 pessoas. Depois mostre qual o maior e o menor peso.

maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input(f'Informe o pesso da {i}ª pessoa: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso recebido foi de {maior} kg.')
print(f'O menor peso recebido foi de {menor} kg.')

8. Escreva um programa utilizando o comando for que mostre na tela a seguinte contagem:
10, 9, 8, 7, 6, 5, 4, 3, 2, 1 e 0. Faça um delay de 1 segundo para a apresentação dos números
na tela e mostrar uma mensagem "FIM!" após a contagem.

from time import sleep
for cont in range(10, -1, -1):
    print(f'{cont} ', end='')
    sleep(1)
print('\nFim!')

9. Faça um programa que mostre na tela os 50 primeiros números pares.

for i in range(2, 51, 2):
    print(i, end=' ')
print('Fim!')

10. Faça um programa que receba cinco números, calcule e mostra a soma apenas dos números pares.

soma = 0
cont = 0
for i in range(1, 6):
    num = int(input(f'Informe o {i}.o valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} números pares e a soma deles foi {soma}!')

11. IDEM 7. LISTA 7) Faça um programa que leia um número inteiro e mostre a sua tabuada.
Use a estrutura de repetição for neste caso.

'''

num = int(input('Digite um número qualquer para ver sua tabuada: '))
for i in range(1, 11):
    print(f'{num} x {i:2} = {num * i}')

