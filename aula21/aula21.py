'''
d = {'nome': 'Joao', 'idade': 20, 'matricula': 1}
for k in d:
    print(k)

d = {'nome': 'Joao', 'idade': 20, 'matricula': 1}
for k in d.keys():
    print(k)

d = {'nome': 'Joao', 'idade': 20, 'matricula': 1}
for v in d.values():
    print(v)

d = {'nome': 'Joao', 'idade': 20, 'matricula': 1}
for k, v in d.items():
    print(f'{k} = {v}')

'''

dados = dict()
dados = {'nome': 'Matheus', 'idade': 18}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'
print(dados)
del dados['idade']
print(dados)
