'''
1. Desenvolva um programa que atribua à variável `msg' o seguinte conteúdo ``Olá, Mundo!'',
depois imprima o valor desta variável na tela do console Python.
print('-'*12)
msg = 'Olá, Mundo!'
print(msg)
print('-'*12)

2. Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas
de acordo com o valor digitado.
nome = input('Qual é o seu nome? ')
print(f'Seja bem vindo, {nome}!')

3. Faça um programa que leia um número inteiro e o imprima.
número = int(input('Digite um número inteiro: '))
print(f'O número digitado é {número}!')

4. Faça um programa que leia um número real e o imprima.
número = float(input('Digite um número real: '))
print(f'O número digitado é {número}!')

5. Peça ao usuário para digitar três valores inteiros e imprima a soma deles.
número1 = int(input('Digite o primeiro número.: '))
número2 = int(input('Digite o segundo número..: '))
número3 = int(input('Digite o terceiro número.: '))
soma = número1 + número2 + número3
print(f'A soma de {número1}, {número2} e {número3} é igual a {soma}.')

6. Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa
e mostre um mensagem com a data formatada.
dia = input('Dia do nascimento = ')
mes = input('Mês do nascimento = ')
ano = input('Ano do nascimento = ')
print('Você nasceu no dia ' + dia + ' de ' + mes + ' de ' + ano + '. Correto??')

7. Leia um número real e imprima a quinta parte deste número.
número = float(input('Digite um número real: '))
quinta = número / 5
print(f'A quinta parte de {número} é igual a {quinta}!')

8. Faça um programa que leia quanto dinheiro uma pessoa tem na carteira (em R$) e
mostre quantos dólares ela pode comprar. Considere US$ 1,00 = R$ 5,34.
real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dólar = real / 5.34
print(f'Com R$ {real:.2f} você pode comprar US$ {dólar:.2f}.')

9. Faça um programa que receba do usuário uma medida de temperatura, em Fahrenheit,
e converta para graus Celsius. Utilize a seguinte expressão: C = 5.0x(F-32.0)/9.0.
F = float(input('Digite a temperatura em graus Fahrenheit '))
C = 5.0 * (F - 32.0) / 9.0
print(f'A temperatura de {F:.2f} graus Fahrenheit equivale a {C:.2f} graus Celsius.')

10. Leia uma velocidade de um veículo em km/h (quilômetros por hora) e apresente-a
convertida em m/s (metros por segundo). A expressão é: M = K/3.6, sendo K a velocidade
em km/h e M em m/s.

'''

K = float(input('Informe a velocidade do veículo em km/h '))
M = K / 3.6
print(f'A velocidade de {K:.2f} km/h do veículo equivale a {M:.2f} m/s.')
