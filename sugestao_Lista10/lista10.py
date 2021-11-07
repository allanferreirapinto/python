'''
1. Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos para todos,
mas especialmente para mulheres. Faça um programa que leia nome, sexo e o valor das
compras do cliente e calcule o preço com desconto. Sabendo que:
    - Homens ganham 5% de desconto
    - Mulheres ganham 13% de desconto

nome = str(input('Qual é o seu nome? '))
sexo = str(input('Qual é o seu sexo? '))
preço = float(input('Qual foi o valor das compras? '))
if sexo == 'M':
    desconto = preço - preço * 0.05
else:
    desconto = preço - preço * 0.13
print(f'Nas compras de {preço:.2f} você irá pagar R$ {desconto:.2f} reais de desconto!')

2. Fa¸ca um programa que pergunte a distˆancia que um passageiro deseja percorrer em Km.
Calcule o preço da passagem, cobrando R$0.50 por Km para viagens até 200Km e R$0.45
para viagens mais longas.

distância = float(input('Qual é a distância em km? '))
if distância < 200:
    preço = distância * 0.5
else:
    preço = distância * 0.45
print(f'Para a distância de {distância:.2f} km rodados o preço cobrado será: R$ {preço:.2f}')

3. Elabore um programa no Python que leia dois números inteiros e compare-os,
mostrando na tela uma das mensagens abaixo:
    - O primeiro valor é o maior
    - O segundo valor é o maior
    - Não existe valor maior, os dois são iguais

n1 = int(input('Digite o primeiro número.: '))
n2 = int(input('Digite o segundo número..: '))
if n1 > n2:
    print('O primeiro número é maior!')
elif n2 > n1:
    print('O segundo número é maior!')
else:
    print('Os dois número são iguais!')

4. Faça um programa que leia a largura e o comprimento de um terreno retangular, calculando e
mostrando a sua área em m2. O programa também devemostrar a classificação desse terreno,
de acordo com a lista abaixo:
    - Abaixo de 100 m2 = TERRENO POPULAR
    - Entre 100 m2 e 500 m2 = TERRENO MASTER
    - Acima de 500 m2 = TERRENO VIP

comprimento = float(input('Digite o comprimento do terreno: '))
largura = float(input('Digite a largura do terreno: '))
área = comprimento * largura
if área < 100:
    print('TERRENO POPULAR')
elif área < 500:
    print('TERRENO MASTER')
else:
    print('TERRONO VIP')

5. Desenvolva um programa que leia o nome de um funcionário, seu salário, quantos anos ele
trabalha na empresa e mostre seu novo salário, reajustado de acordo com a tabela a seguir:
    - Até 3 anos de empresa: aumento de 3%
    - entre 3 e 10 anos: aumento de 12.5%
    - 10 anos ou mais: aumento de 20%
'''

nome = str(input('Qual é o nome do funcionário? '))
salário = float(input('Qual é o salário do funcionario? '))
anos = int(input('Qual é quantidade de anos na empresa pelo funcionário? '))
if anos < 3:
    novo = salário + (salário * 3 / 100)
elif anos < 10:
    novo = salário + (salário * 12.5 / 100)
else:
    novo = salário + (salário * 20 / 100)
print(f'Com {anos} anos na empresa, o funcionário passa a ganhar {novo:.2f} agora!')
