"""
1. Faça um programa que leia um número real e imprima o resultado do quadrado desse número.
número = float(input('Digite um número qualquer: '))
raíz = número ** (1/2)
print(f'A raíz de {número} é {raíz}!')

2. Faça um programa que solicita ao usuário as medidas de uma sala retangular, em metros, e calcula
e apresenta a sua área, em metros quadrados.
l = float(input('Informe a largura da sala, em metros: '))
c = float(input('Informe o comprimento da sala, em metros: '))
área = l * c
print(f'A área da sala de largura {l} e comprimento {c} é {área} m²!')

3. Elabore um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
    Ex:
    Digite um número: 9
    O antecessor de 9 é 8
    O sucessor de 9 é 10
n = int(input('Digite um número inteiro qualquer: '))
print(f'O antecessor do número {n} é {n-1}!')
print(f'O sucessor do número {n} é {n+1}!')

4. Faça um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = float(input('Digite um número qualquer: '))
print(f'O dobro do número {n} é {n*2}!')
print(f'O triplo do número {n} é {n*3}!')
print(f'A raíz quadrada do número {n} é {n**(1/2)}!')

5. Faça um programa que leia as duas notas de um aluno em uma matéria e mostre na tela
a sua média na disciplina.
    Ex:
    Nota 1: 4.5
    Nota 2: 8.5
    A média entre 4.5 e 8.5 é igual a 6.5
nota1 = float(input('Digite primeira nota.: '))
nota2 = float(input('Digite segunda nota..: '))
média = (nota1 + nota2) / 2
print(f'A média da nota {nota1} e a nota {nota1} é igual a {média}!')

6. Crie um script Python que leia um valor em metros e exiba convertido em centímetros e milímetros.
medida = float(input('Informe a distância em metros: '))
cm = int(medida * 100)
mm = int(medida * 1000)
print(f'A distância de {medida} m corresponde a:\n{cm} cm! \n{mm} mm!')

7. Faça um programa que leia um número inteiro e mostre a sua tabuada de multiplicação.
número = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
print(f'{número} x {1:2} = {número*1}')
print(f'{número} x {2:2} = {número*2}')
print(f'{número} x {3:2} = {número*3}')
print(f'{número} x {4:2} = {número*4}')
print(f'{número} x {5:2} = {número*5}')
print(f'{número} x {6:2} = {número*6}')
print(f'{número} x {7:2} = {número*7}')
print(f'{número} x {8:2} = {número*8}')
print(f'{número} x {9:2} = {número*9}')
print(f'{número} x {10} = {número*10}')
print('-' * 12)

8. Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
e a quantidade de tinta necessária pintá-la, sabendo que cada litro de tinta pinta uma área de 2 m².
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
print(f'A sua parede tem a dimensão de {largura}x{altura} e sua área é de {largura*altura} m².')
print(f'Para pintar essa parede, você precisará de {(largura*altura)/2} litros de tinta.')

9. Faça um programa que receba do usuário o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('Qual é o preço do produto? R$ '))
novo = preço - (preço * 5 / 100)
print(f'O produto que custava R$ {preço:.2f} passa valer {novo:.2f} com 5% de desconto.')

10. Leia o salário de um colaborador de uma determinada empresa e mostre seu novo salário, com 15\% de aumento.
salário = float(input('Qual é o salário do funcionario? R$ '))
novo = salário + (salário * 15 / 100)
print(f'O funcionário que ganhava R$ {salário:.2f} passa a ganhar {novo:.2f} com 15% de aumento.')
"""
