'''
1. Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR.

número = int(input('Digite um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print(f'O número {número} é PAR!')
else:
    print(f'O número {número} é ÍMPAR!')

2. Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela e depois
mostre se ela pode ou não votar.

from datetime import date
nascimento = int(input('Informe o ano do seu nascimento: '))
anoatual = date.today().year
idade = anoatual - nascimento
if idade < 16:
    print(f'Com {idade} anos: NÃO VOTA.')
elif 16 <= idade < 18 or idade > 70:
    print(f'Com {idade} anos: VOTO OPCIONAL.')
else:
    print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')

3. Escreva um programa computacional no Python que pergunte a velocidade de um carro.
Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse
caso, exiba o valor da multa, cobrando R$ 5,00 por cada km acima da velocidade permitida.

velocidade = float(input('Informe a velocidade do veículo: '))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print('MULTADO! Você excedeu o limite permitido que é de 80 km/h!')
    print(f'Você deve pagar uma multa de {multa}!')
print('Tenha um bom dia! Dirija com segurança.')

4. Faça um script que leia um determinado ano e mostre se ele é ou não BISSEXTO.

ano = int(input('Informe o ano desejado: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é Bissexto!')
else:
    print(f'O ano de {ano} não é Bissexto!')

5. Elabore um programa que calcula a resistência elétrica de um circuito com a
aplicação da lei de Ohm. Neste programa o usuário deverá informar os valores de
tensão e corrente elétrica e após verificada condição, o programa deve efetuar os
cálculos, mostrando no final a mensagem com os resultados.

tensão = float(input('Digite o valor da tensão elétrica: '))
corrente = float(input('Digite o valor da corrente elétrica: '))
if corrente != 0:
    resistência = tensão / corrente
    print(f'O valor da Resistência Elétrica é igual a {resistência} ohms.')
else:
    print(f'Impossível divisão por zero!')

6. Crie um programa que leia o tamanho de três segmentos de reta. Analise seus
comprimentos e diga se é possível formar um triângulo com essas retas. Matematicamente,
para três segmentos formarem um triângulo, o comprimento de cada lado deve ser menor
que a soma dos outros dois.

reta1 = float(input('Informe o primeiro segmento de reta.: '))
reta2 = float(input('Informe o segundo segmento de reta..: '))
reta3 = float(input('Informe o terceiro segmento de reta.: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos informados formam um triângulo!')
else:
    print('Os segmentos acima não formam um triângulo!')

7. Elabore um programa no Python que leia dois números inteiros e compare-os,
mostrando na tela uma das mensagens abaixo:
    - O primeiro valor é o maior
    - O segundo valor é o maior
    - Não existe valor maior, os dois são iguais

número1 = int(input('Digite o primeiro número.: '))
número2 = int(input('Digite o segundo número..: '))
if número1 > número2:
    print('O primeiro número é maior!')
elif número2 > número1:
    print('O segundo número é maior!')
else:
    print('Os dois número são iguais!')


8. Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média atingida:
    - Média até 4.9: REPROVADO
    - Média entre 5.0 e 6.9: RECUPERAÇÃO
    - Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite o valor da primeira nota.: '))
nota2 = float(input('Digite o valor da segunda nota..: '))
média = (nota1 + nota2) / 2
if média >= 7:
    print(('O aluno está APROVADO!'))
elif 5 <= média < 7:
    print('O aluno está de RECUPERAÇÃO!')
else:
    print('O aluno está REPROVADO!')

9. Desenvolva um programa para o cálculo do Índice de Massa Corpórea (IMC). O IMC é um valor
calculado baseado na altura e no peso de uma pessoa. De acordo com o valor do IMC, podemos
classificar o indivíduo dentro de certas faixas.
    - abaixo de 18.5: Abaixo do peso
    - entre 18.5 e 25: Peso ideal
    - entre 25 e 30: Sobrepeso
    - entre 30 e 40: Obesidade
    - acima de 40: Obesidade mórbida
Obs: O IMC é calculado pela expressão peso/altura$^2$ (peso dividido pelo quadrado da altura)

peso = float(input('Informe qual é o seu peso: '))
altura = float(input(('Informe qual é a sua alura: ')))
imc = peso / altura ** 2
print(f'O seu IMC é de {imc:.2f}.')
if imc < 18.5:
    print('Você está abaixo do peso normal!')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de peso ideal!')
elif 25 <= imc < 30:
    print('Você esta com sobrepeso! Fique atento.')
elif 30 <= imc < 40:
    print('Você está em obesidade!')
else:
    print('Você está em obesidade mórmida! Tenha cuidado.')

10. Desenvolva um programa em Python para descrever como jogar pedra-papel-tesoura entre você
e o computador.

'''

from random import randint
from time import sleep
opções = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Escolha uma das opções: [ 0 ] PEDRA [ 1 ] PAPEL [ 2 ] TESOURA''')
jogador = int(input('Digite qual é a sua opção: '))
if jogador < 0 or jogador >= 3:
    print('Opção INVÁLIDA!!! Insira uma opção entre 0 e 2.')
    jogador = int(input('Escolha qual é a sua opção: '))
print('-=' * 13)
print('PEDRA')
sleep(0.5)
print('PAPEL')
sleep(1.5)
print('TESORA')
sleep(0.5)
print(f'Computador escolheu {opções[computador]}')
print(f'Jogador escolheu {opções[jogador]}')
print('-=' * 13)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
