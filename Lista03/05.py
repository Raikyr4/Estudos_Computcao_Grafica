import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Definir as coordenadas dos pontos A, B, C e D
points = {'A': (1, 1, 1), 'B': (1, -1, -1), 'C': (-1, 1, -1), 'D': (-1, -1, 1)}

# Definir os caracteres e cores correspondentes
labels = {'A': 'o', 'B': '+', 'C': '*', 'D': '0'}
colors = {'A': 'green', 'B': 'yellow', 'C': 'blue', 'D': 'red'}

# Inicializar a figura em 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Definir as arestas do tetraedro
edges = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]

# Desenhar as arestas com cores diferentes
edge_colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow']

# Armazenar as coordenadas originais dos pontos em um dicionário
original_points = dict(points)

# Função para aplicar a transformação de rotação
def apply_rotation(theta, alpha, delta):
    for point in points:
        x, y, z = original_points[point]
        # Aplicar a transformação de rotação
        x_new = x
        y_new = y * np.cos(np.radians(alpha)) - z * np.sin(np.radians(alpha))
        z_new = y * np.sin(np.radians(alpha)) + z * np.cos(np.radians(alpha))
        y = y_new
        z = z_new

        x_new = x * np.cos(np.radians(theta)) - z * np.sin(np.radians(theta))
        z_new = x * np.sin(np.radians(theta)) + z * np.cos(np.radians(theta))
        x = x_new
        z = z_new

        x_new = x * np.cos(np.radians(delta)) - y * np.sin(np.radians(delta))
        y_new = x * np.sin(np.radians(delta)) + y * np.cos(np.radians(delta))
        x = x_new
        y = y_new

        points[point] = (x, y, z)

# Animação da rotação
for angle in range(0, 360, 1):
    ax.clear()
    
    # Aplicar a transformação de rotação
    apply_rotation(angle, angle, angle)
    
    # Desenhar os pontos e rótulos
    for point, coord in points.items():
        ax.text(*coord, labels[point], color=colors[point], fontsize=12)
        ax.scatter(*coord, color=colors[point])

    # Desenhar as arestas com cores diferentes
    for i, edge in enumerate(edges):
        ax.plot(*zip(*[points[edge[0]], points[edge[1]]]), color=edge_colors[i])

    # Configurar os limites dos eixos
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])

    # Adicionar rótulos para os eixos
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_zlabel('Eixo Z')

    # Adicionar um título para o gráfico
    plt.title('Rotação 3D em torno de A')

    # Atualizar o gráfico
    plt.pause(0.01)

plt.show()
