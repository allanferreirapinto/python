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

'''

ano = int(input('Informe o ano desejado: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é Bissexto!')
else:
    print(f'O ano de {ano} não é Bissexto!')
