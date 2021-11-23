'''
1. Desenvolva um programa que leia vários números inteiros. O programa para apenas quando
o usuário digitar 111, que é a condição de parada. Por fim, mostre a quantidade de números
foram digitado e qual foi a soma do números. O flag deve ser desconsiderado.

número = soma = cont = 0
while True:
    número = int(input('Digite um número qualquer (111 para sair): '))
    if número == 111:
        break
    cont += 1
    soma += número
print(f'Você digitou {cont} números e a soma deles foi {soma}!')

2. Crie um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
que o usuário informar. Finalize a entrada de dados com um valor negativo.

while True:
    número = int(input('Para o cálculo da tabuada digite um número (negativos para sair): '))
    if número < 0:
        break
    for cont in range(1, 11):
        print(f'{número} x {cont:2} = {número*cont}')
print('PROGRAMA DA TABUADA FINALIZADO!')

3. Faça m programa que leia a idade e o sexo de várias pessoas. Para cada pessoa cadastrada,
o programa deve perguntar se o usário deseja ou não continuar. Por fim, mostre:

    a) quantas pessoas tem mais de 16 anos.
    b) quantas mulheres tem menos de 21 anos.
    c) quantos homens foram adicionados.

total16 = totalM21 = totalH = 0
while True:
    idade = int(input('Informe a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe qual é o sexo: [M/F] ')).strip().upper()[0]
        # Método strip() coloca as letras em maiúsculas e upper() para eliminar espaços em branco.
        # O [0], para considerar apenas a primeira letra
    if idade >= 16:
        total16 += 1
    if sexo == 'M':
        totalH += 1
    if sexo == 'F' and idade < 21:
        totalM21 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Todas as pessoas com mais de 16 anos, são: {total16}.')
print(f'E as mulheres com menos de 21 anos, são: {totalM21}.')
print(f'Os homens representa um total de: {totalH}.')

4. Desenvolva um programa que leia o nome e preço de vários produtos. O programa deve
perguntar ao usuário deseja continua. No final, mostre:
    a) qual é o total da compra.
    b) quantos produtos custam acima de R$500,00 reais.
    c) qual é o nome do produto com menor valor.

total = total500 = menor = cont = 0
barato = ''

while True:
    produto = str(input('Informe qual é nome do produto: '))
    preço = float(input('Qual o preço do produto R$ '))
    cont += 1
    total += preço
    if preço > 500:
        total500 += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'O valor total da compra foi R$ {total:.2f}!')
print(f'Foram {total500} produtos que custaram mais de R$ 500.00!')
print(f'O produto de menor valor foi {barato} que custa R$ {menor:.2f}')

5. Crie um programa que simule o funcionamento de um caixa eletrônico bancário. Peça ao
usuário qual o valor a ser sacado e o programa deverá informar quantas cédulas de cada valor
serão entregues. O caixa possui cédulas de R$ 10,00, R$ 20,00, R$ 50,00 e R$ 100,00.

'''

valor = int(input('Qual é o valor você quer sacar? R$ '))
total = valor
cédula = 100
totcédula = 0
while True:
    if total >= cédula:
        total -= cédula
        totcédula += 1
    else:
        if totcédula > 0:
            print(f'Total de {totcédula} cédulas de R$ {cédula}')
        if cédula == 100:
            cédula = 50
        elif cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 5
        elif cédula == 5:
            cédula = 1
        totcédula = 0
        if total == 0:
            break
print('Saque realizado com sucesso!')
