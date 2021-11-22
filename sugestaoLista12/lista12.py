'''
1. Faça um programa utilizando o comando while que mostra a contagem regressiva na tela,
iniciando em 10 e terminando com 0. Mostrar uma mensagem "Fim!" ap´os a contagem.

i = 10
while i > 0:
    print(f'{i} ', end='')
    i = i - 1
print('Fim!')

2. Crie um programa utilizando o comando while que mostre na tela a seguinte contagem: 0 2
4 6 8 10 12 Fim!

cont = 0
while cont < 13:
    print(f'{cont} ', end='')
    cont = cont + 2
print('Fim!')

3.Desenvolva um programa utilizando o comando while que mostre na tela a seguinte contagem:
100 95 90 85 80 ... 0 Acabou!

cont = 100
while cont > - 1:
    print(f'{cont} ', end='')
    cont -= 1
print('Acabou!')

4. Faça um programa que leia 10 números inteirose imprima sua média.

cont = 1
média = soma = 0
while cont < 10:
    num = float(input(f'Informe o {cont}.o número: '))
    soma += num
    média = soma/cont
    cont += 1
print(f'A média dos {cont} números digitado é igual a {média:.2f}!')

5. Faça um programa que peça ao usuário para digitar 10 valores e some-os.

i = 1
soma = cont = 0
while i < 11:
    num = float(input(f'Informe o {i:2}.o valor: '))
    soma += num
    cont += 1
    i += 1
print(f'Você informou {cont} números e a soma deles foi {soma}!')

6. Faça m programa que apresente um menu de opções para o cálculo das seguintes operações
entre dois números:
1 - adição
2 - subtração
3 - multiplicação
4 - divisão
5 - Sair

O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do resultado
e a volta ao menu de opções. O programa só termina quando a opção for sair.

from time import sleep
número1 = int(input('Informe o primeiro valor: '))
número2 = int(input('Informe o segundo valor: ' ))
opção = 0
while opção != 5:
    print('Menu de opções:')

    print('1 - adição \n2 - subtração \n3 - multiplicar \n4 - divisão \n5 - sair do programa')
    opção = int(input('Escolhar qual é a sua opção? '))
    if opção == 1:
        soma = número1 + número2
        print(f'A soma entre {número1} e {número2} é igual a {soma}.')
    elif opção == 2:
        sub = número1 - número2
        print(f'A subtração entre {número1} - {número2} é igual a {sub}.')
    elif opção == 3:
        produto = número1 * número2
        print(f'A multiplicação {número1} x {número2} é igual a {produto}.')
    elif opção == 4:
        div = número1 / número2
        print(f'A divisão de {número1} / {número2} é igual a {div}.')
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente.')
    print('-=' * 23)
    sleep(3)
print('Programa finalizado com sucesso! Volte sempre!')

7. Faça um programa que leia um número inteiro e mostre o seu fatorial.

num = int(input('Informe um número para o cálculo do seu Fatorial: '))
cont = num
fatorial = 1
print(f'Calculando {num}! = ', end='')
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fatorial *= cont
    cont -= 1
print(f'{fatorial}.')

8.Crie um programa que leia um número inteiro e mostre na tela os primeiros elementos da
Sequência de Fibonacci.

print('-='*14)
print('-= Sequencia de Fibonacci -=')
print('-='*14)
número = int(input('Qual é o número de termos que você quer mostrar? '))
termo1 = 0
termo2 = 1
print(f'{termo1}, {termo2}', end='')
cont = 3
while cont <= número:
    termo3 = termo1 + termo2
    print(f', {termo3}', end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print(', Fim!')

9. Crie um programa que leia vários números pelo teclado e mostre no final a quantidade de
números que foram digitados e o somatório entre eles.
Obs: O programa será interrompido quando o número 1111 for digitado

número = cont = soma = 0
número = int(input('Digite um numero [111 para sair]: '))
while número != 111:
    soma += número
    cont += 1
    número = int(input('Digite um número [111 para sair]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')

10. Faça um programa que leia os números inteiros e imprima a média entre todos os valores,
qual foi o maior e o menor dos valores recebidos. O programa deve perguntar se o usuário
quer ou não continuar digitando os valores.

'''

resp = 'S'
soma = cont = média = maior = menor = 0
while resp in 'Ss':
    número = int(input('Digite um número: '))
    soma += número
    cont += 1
    if cont == 1:
        maior = menor = número
    else:
        if número > maior:
            maior = número
        if número < menor:
            menor = número
    resp = str(input('Deseja continual? [S/N] '))
média = soma / cont
print(f'Você digitou {cont} números e a média foi {média}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
