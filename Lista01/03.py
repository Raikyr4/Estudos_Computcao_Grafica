import matplotlib.pyplot as plt
import numpy as np

# Pontos A e B
x_a, y_a = 3, 2
x_b, y_b = 6, 8

# Parâmetros para a equação paramétrica da reta
t = np.linspace(0, 1, 100)  # Valores de t entre 0 e 1

# Equação paramétrica da reta
x = x_a + t * (x_b - x_a)
y = y_a + t * (y_b - y_a)

# Configurando o gráfico
plt.figure(figsize=(10, 10))  # Tamanho da figura
plt.xlim(0, 10)  # Limites do eixo X
plt.ylim(0, 10)  # Limites do eixo Y

# Desenhando a reta AB
plt.plot(x, y, 'r-', label='Reta AB')

# Marcando os pontos A e B
plt.plot(x_a, y_a, 'go', markersize=8, label='Ponto A')
plt.plot(x_b, y_b, 'b+', markersize=10, label='Ponto B')

# Configurando rótulos dos eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Título do gráfico
plt.title('Segmento de Reta AB utilizando Equação Paramétrica')

# Mostrando a legenda
plt.legend()

# Mostrando o gráfico
plt.grid(True)  # Habilitando as grades
plt.show()
