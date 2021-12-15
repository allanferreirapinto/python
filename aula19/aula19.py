'''
Listas em Python

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]  # tipo de dado int
lista2 = ['C', 'E', 'F', 'E', 'T']  # tipo de dado str
lista3 = []
lista4 = list(range(11))
lista5 = list('CEFET')
lista6 = ['CEFET', 'UFMG']


# Podemos checar se determinado valor está dentro na lista
num = int(input('Entre com o número: '))
if num in lista4:
    print(f'Encontrei o número {num}.')
else:
    print(f'Não encontrei o número {num}.')

# Podemos facilmente ordenar uma lista

lista1.sort()
print(lista1)

# Podemos contar o número de ocorrências de um valor numa lista

print(lista1.count(1))
print(lista5.count('E'))

# Podemos adcionar elementos em listas
print(lista1)
lista1.append(42)
print(lista1)
lista1.append([8, 3, 1])
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista!')
else:
    print('Não encontrei a lista!')

lista1.extend([123, 44, 67])  # Coloca cada elemento da lista como valor adicional à lista
print(lista1)

lista1.insert(2, 'Novo Valor')
print(lista1)

'''

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]  # tipo de dado int
lista2 = ['C', 'E', 'F', 'E', 'T']  # tipo de dado str
lista3 = []
lista4 = list(range(11))
lista5 = list('CEFET')
lista6 = ['CEFET', 'UFMG']

lista1 = lista1 + lista2
print(lista1)
