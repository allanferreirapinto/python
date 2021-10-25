'''
1. Faça um programa que leia um número inteiro e calcule a raíz quadrada, utilizando módulos do Python.
# Forma 1
import math
número = int(input('Digite um número inteiro qualquer: '))
raíz = math.sqrt(número)
print(f'A raíz quadrada do número {número} é igual a {raíz}!!!')

# Forma 2
from math import sqrt
número = int(input('Digite um número inteiro qualquer: '))
raíz = sqrt(número)
print(f'A raíz quadrada do número {número} é igual a {raíz}!!!')

2. Faça um programa que leia um número real qualquer e mostre na tela a sua porção inteira.
    Ex:
    Digite um número: 3.14159265359
    O número 3.14 possui a parte inteira igual a 3.
# Forma 1
import math
número = float(input('Digite um número real qualquer: '))
pi = math.floor(número)
print(f'A porção inteira do número {número:.2f} é {pi}.')

# Forma 2
from math import floor
número = float(input('Digite um número real qualquer: '))
pi = floor(número)
print(f'A porção inteira do número {número:.2f} é {pi}.')

3.Faça um programa que leia o cateto oposto e o cateto adjacente de um triângulo retângulo,
calcule e imprima na tela a sua hipotenusa.
# Forma 1
co = float(input('Informe o valor do cateto oposto do triângulo retângulo ....: '))
ca = float(input('Informe o valor do cateto adjacente do triângulo retângulo .: '))
h = (co**2 + ca**2) ** (1/2)
print(f'O valor da hipotenusa do triângulo retângulo vale {h}!')

# Forma 2
import math
co = float(input('Informe o valor do cateto oposto do triângulo retângulo ....: '))
ca = float(input('Informe o valor do cateto adjacente do triângulo retângulo .: '))
h = math.sqrt(co**2 + ca**2)
print(f'O valor da hipotenusa do triângulo retângulo vale {h}!')

# Forma 3
from math import sqrt
co = float(input('Informe o valor do cateto oposto do triângulo retângulo ....: '))
ca = float(input('Informe o valor do cateto adjacente do triângulo retângulo .: '))
h = sqrt(co**2 + ca**2)
print(f'O valor da hipotenusa do triângulo retângulo vale {h}!')

# Forma 4
import math
co = float(input('Informe o valor do cateto oposto do triângulo retângulo ....: '))
ca = float(input('Informe o valor do cateto adjacente do triângulo retângulo .: '))
h = math.hypot(co, ca)
print(f'O valor da hipotenusa do triângulo retângulo vale {h}!')

4. Peça do usuário um valor em graus para um ângulo. Converta-o para radianos e, usando funções da
biblioteca math, imprima o seno, cosseno e tangente deste ângulo.
# Forma 1
import math
ângulo = float(input('Digite o ângulo qualquer: '))
radianos = ângulo*3.14/180
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)
print(f'O ângulo de {ângulo:.1f} graus tem o SENO de {seno:.2f};')
print(f'O ângulo de {ângulo:.1f} graus tem o COSSENO de {cosseno:.2f};')
print(f'O ângulo de {ângulo:.1f} graus tem a TANGENTE de {tangente:.2f}.')

# Forma 2
import math
ângulo = float(input('Digite o ângulo qualquer: '))
seno = math.sin(math.radians(ângulo))
print(f'O ângulo de {ângulo} graus tem o SENO de {seno:.2f};')
cosseno = math.cos(math.radians(ângulo))
print(f'O ângulo de {ângulo} graus tem o COSSENO de {cosseno:.2f};')
tangente = math.tan(math.radians(ângulo))
print(f'O ângulo de {ângulo} graus tem a TANGENTE de {tangente:.2f}.')

# Forma 3
from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo qualquer: '))
seno = sin(radians(ângulo))
print(f'O ângulo de {ângulo} graus tem o SENO de {seno:.2f};')
cosseno = cos(radians(ângulo))
print(f'O ângulo de {ângulo} graus tem o COSSENO de {cosseno:.2f};')
tangente = tan(radians(ângulo))
print(f'O ângulo de {ângulo} graus tem o TANGENTE de {tangente:.2f}.')

5. Faça um programa que leia um número inteiro e mostre na tela seu fatorial.
# Forma 1
import math
número = int(input('Digite um número para calcular seu Fatorial: '))
fatorial = math.factorial(número)
print(f'O fatorial de {número} é {fatorial}!')

# Forma 2
from math import factorial
número = int(input('Digite um número para calcular seu Fatorial: '))
fatorial = factorial(número)
print(f'O fatorial de {número} é {fatorial}!')

6. Crie um programa que leia um número real qualquer para calcular o comprimento de uma
circunferência de raio r. Utilize a seguinte equação: C = 2 * π * r.
# Forma 1
import math
raio = float(input('Digite um número real qualquer: '))
c = 2 * math.pi * raio
print(f'O comprimento da circunferência de raio {raio:.2f} é {c:.2f}.')

# Forma 2
from math import pi
raio = float(input('Digite um número real qualquer: '))
c = 2 * pi * raio
print(f'O comprimento da circunferência de raio {raio:.2f} é {c:.2f}.')

7. Faça um programa que leia um número real qualquer e arredonda para cima, até o
inteiro mais próximo, imprimindo na tela.
# Forma 1
import math
número = float(input('Digite um número real qualquer: '))
pi = math.ceil(número)
print(f'A porção inteira do número {número:.2f} é {pi}.')

# Forma 2
from math import ceil
número = float(input('Digite um número real qualquer: '))
pi = ceil(número)
print(f'A porção inteira do número {número:.2f} é {pi}.')

8. Desenvolva um programa que leia um número qualquer e retorme o seu valor absoluto.
# Forma 1
import math
número = float(input('Digite um número real qualquer: '))
absuluto = math.fabs(número)
print(f'O valor abosuluto de {número:.2f} é {absuluto:.2f}.')

# Forma 2
from math import fabs
número = float(input('Digite um número real qualquer: '))
absuluto = fabs(número)
print(f'O valor abosuluto de {número:.2f} é {absuluto:.2f}.')

9. Faça um programa que defina uma variável com o raio de uma circunferência lida pelo usuário e
calcule sua área. Use a fórmula: area = π * (raio^2). Utilize a constante π definida na linguagem.
# Forma 1
import math
raio = float(input('Digite um número real qualquer: '))
área = math.pi * raio ** 2
print(f'A área da circunferência de raio {raio:.2f} é {área:.2f}.')

# Forma 2
from math import pi
raio = float(input('Digite um número real qualquer: '))
área = pi * raio ** 2
print(f'A área da circunferência de raio {raio:.2f} é {área:.2f}.')


10. O número neperiano também é muito útil em diversas situações, como em logaritmos naturais
por exemplo. Uma outra utilização é para o cálculo de juros compostos, onde o montante após
um tempo t, Mt , a uma taxa de juros composto r é definido como: Mt = Mi * e^(r*t), onde Mi
é o montante inicial. O programa deve pedir do usuário um montante inicial, a taxa mensal
de juros, e período em meses.

# Forma 1
import math
Mi = float(input('Digite o montante incial: '))
r = float(input('Digite a taxa mensal de juros: '))
t = float(input('Digite o período em meses: '))
Mt = Mi * math.e ** (r/100*t)
print(f'O montante total será de {Mt:.2f}.')

'''

# Forma 2
from math import e
Mi = float(input('Digite o montante incial: '))
r = float(input('Digite a taxa mensal de juros: '))
t = float(input('Digite o período em meses: '))
Mt = Mi * e ** (r/100*t)
print(f'O montante total será de {Mt:.2f}.')
