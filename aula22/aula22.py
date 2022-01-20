import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(-5, 5, 0.01)
# y = x ** 2
# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()

# y_osc = np.exp(-x) * np.cos(2 * np.pi * x)
# fig, ax = plt.subplots()
# ax.plot(x, y_osc)
# plt.show()

# fig, ax, = plt.subplots()
# ax.plot(x, x ** 3)
# ax.plot(x, y_osc)
# plt.show()

# faixaEtaria = ['18-25', '26-35', '36-45', '46-55', '55+']
# renda = [1220.09, 2550.12, 3752.25, 4120.89, 3482.22]
# plt.bar(faixaEtaria, renda)
# plt.title('Renda média x Faixa etária')
# plt.xlabel('Faixa etária')
# plt.ylabel('Renda média')
# plt.show()

fig, ax = plt.subplots()
x = np.linspace(0, 10, 200)
plt.title('Função Seno')
plt.xlabel('x')
plt.ylabel('f(x)')
y = np.sin(x)
ax.plot(x, y, 'r', linewidth=5.0)
plt.grid()
plt.show()

