import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Definir as coordenadas dos pontos A, B, C e D
points = {'A': (1, 1, 1), 'B': (1, -1, -1), 'C': (-1, 1, -1), 'D': (-1, -1, 1)}

# Definir os caracteres e cores correspondentes
labels = {'A': 'o', 'B': '+', 'C': '*', 'D': '0'}
colors = {'A': 'green', 'B': 'yellow', 'C': 'blue', 'D': 'red'}

# Inicializar a figura em 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Desenhar os pontos e rótulos
for point, coord in points.items():
    ax.text(*coord, labels[point], color=colors[point], fontsize=12)
    ax.scatter(*coord, color=colors[point])

# Definir as arestas do tetraedro
edges = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]

# Desenhar as arestas
for edge in edges:
    ax.plot(*zip(*[points[edge[0]], points[edge[1]]]), color='black')

# Definir as faces do tetraedro
faces = [[points[edge[0]], points[edge[1]], points[other_point]] for edge in edges for other_point in edge]

# Desenhar as faces
ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

# Configurar os limites dos eixos
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

# Adicionar rótulos para os eixos
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')

# Adicionar um título para o gráfico
plt.title('Tetraedro 3D com Rótulos e Cores')

# Mostrar o gráfico
plt.show()
