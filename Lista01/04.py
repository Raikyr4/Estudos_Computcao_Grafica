import matplotlib.pyplot as plt
import numpy as np

# Pontos A, B e C
points = {'A': (3, 2), 'B': (6, 8), 'C': (7, 3)}

# Definindo os pares de pontos para os lados do triângulo
triangle_sides = [('A', 'B'), ('B', 'C'), ('C', 'A')]

# Configurando o gráfico
plt.figure(figsize=(10, 10))  # Tamanho da figura
plt.xlim(0, 10)  # Limites do eixo X
plt.ylim(0, 10)  # Limites do eixo Y

# Desenhando os lados do triângulo com diferentes cores e espessuras
for start, end in triangle_sides:
    x_values = [points[start][0], points[end][0]]
    y_values = [points[start][1], points[end][1]]
    
    plt.plot(x_values, y_values, label=f'{start}{end}', linewidth=np.random.randint(1, 4))

# Marcando os pontos A, B e C
for point, coord in points.items():
    plt.plot(coord[0], coord[1], 'o', markersize=8, label=f'Ponto {point}')

# Configurando rótulos dos eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Título do gráfico
plt.title('Triângulo ABC com Lados Diferentes')

# Mostrando a legenda
plt.legend()

# Mostrando o gráfico
plt.grid(True)  # Habilitando as grades
plt.show()
