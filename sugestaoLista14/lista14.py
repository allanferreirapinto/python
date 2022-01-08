'''
1. Faça um programa que possua uma lista denominado A que armazene 6 números inteiros.
O programa deve executar os seguintes passos:
    a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
    b) Armazene em uma variável inteira (simples) a soma das posições A[0], A[1] e A[5] da
    lista e mostre na tela essa soma.
    c) Modifique a lista na posição 4, atribuindo a esta posição o valor 100.
    d) Mostre na tela cada valor da lista A, um em cada linha.

A = [1, 0, 5, - 2, - 5, 7]
soma = A[0] + A[1] + A[5]
print(f'A soma das posições 0, 1 e 5 é igual a: {soma}')
print(f'Lista A: {A}')
A[4] = 100
print(f'Lista A modificada: {A}')

2. Para a lista x = [10, 3, 3, 10, 10, 6, 6, 4, 8, 7] no Python, ordenar os valores dentra
da lista.

x = [10, 3, 3, 10, 10, 6, 6, 4, 8, 7]
x.sort()
print(f'A lista x dada, em ordem crescente é: x = {x}!')

3. Inverter a ordem dos elementos da seguinte lista B = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1].

b = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
b.reverse()
print(f'A lista b invertida é: b = {b}!')

4. Retiar o elemento 'a' da lista C = ['a', 'e', 'i', 'o', 'u'] no Python.

c = ['a', 'e', 'i', 'o', 'u']
c.remove(c[0])
print(f'Lista c sem o elemento "a": c = {c}!')

5. Dada a lista D = ['a', 'b', 'c', 'd'] remover e rotornar o elemento da prosição 2.

'''

d = ['a', 'b', 'c', 'd']
print(f'Lista d completa é: d = {d}!')
d.pop(2)
print(f'Lista d sem a posição 2 é: d = {d}!')
