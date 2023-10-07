import matplotlib.pyplot as plt
import numpy as np

# Pontos A, B e C
points = {'A': (3, 2), 'B': (6, 8), 'C': (7, 3)}

# Coordenadas do ponto C
C = (7, 3)

# Adicionando ponto C aos pontos
points.update({'C': C})

# Definindo os pares de pontos para os lados do triângulo
triangle_sides = [('A', 'B'), ('B', 'C'), ('C', 'A')]

# Configurando o gráfico
plt.figure(figsize=(10, 10))  # Tamanho da figura
plt.xlim(0, 15)  # Limites do eixo X
plt.ylim(0, 15)  # Limites do eixo Y

# Desenhando os lados do triângulo com diferentes cores e espessuras
for i, (start, end) in enumerate(triangle_sides):
    x_values = [points[start][0], points[end][0]]
    y_values = [points[start][1], points[end][1]]
    
    plt.plot(x_values, y_values, label=f'Lado {i+1}', linewidth=np.random.randint(1, 4))

# Marcando os pontos A, B e C
for point, coord in points.items():
    plt.plot(coord[0], coord[1], 'o', markersize=8, label=f'Ponto {point}')

# Matriz de translação
T = np.array([[1, 0, 0, 3], 
              [0, 1, 0, 5], 
              [0, 0, 1, 0], 
              [0, 0, 0, 1]])

# Aplicando a matriz de translação aos pontos do triângulo
transformed_points = {point: np.dot(T, np.array([coord[0], coord[1], 0, 1]))[:2] for point, coord in points.items()}

# Definindo os pares de pontos para os lados do triângulo transformado
transformed_triangle_sides = [('A', 'B'), ('B', 'C'), ('C', 'A')]

# Desenhando os lados do triângulo transformado
for start, end in transformed_triangle_sides:
    x_values = [transformed_points[start][0], transformed_points[end][0]]
    y_values = [transformed_points[start][1], transformed_points[end][1]]
    
    plt.plot(x_values, y_values, label=f'{start}{end} (Transladado)', linestyle='--', linewidth=np.random.randint(1, 4))

# Configurando rótulos dos eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Título do gráfico
plt.title('Triângulo ABC e sua Translação')

# Mostrando a legenda
plt.legend()

# Mostrando o gráfico
plt.grid(True)  # Habilitando as grades
plt.show()
