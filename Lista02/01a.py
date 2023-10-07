import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define os vértices do tetraedro
vertices = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [0, 0, 0]
])

# Define as arestas do tetraedro
arestas = [
    [vertices[0], vertices[1], vertices[2]],
    [vertices[0], vertices[1], vertices[3]],
    [vertices[0], vertices[2], vertices[3]],
    [vertices[1], vertices[2], vertices[3]]
]

# Cria uma figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Desenha o tetraedro
tetraedro = Poly3DCollection(arestas, edgecolor='k', linewidths=1, alpha=0.5)
ax.add_collection3d(tetraedro)

# Configura os limites dos eixos
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# Mostra a reflexão do tetraedro à origem
vertices_refletidos = -vertices  # Reflexão em relação à origem
refletido_arestas = [
    [vertices_refletidos[0], vertices_refletidos[1], vertices_refletidos[2]],
    [vertices_refletidos[0], vertices_refletidos[1], vertices_refletidos[3]],
    [vertices_refletidos[0], vertices_refletidos[2], vertices_refletidos[3]],
    [vertices_refletidos[1], vertices_refletidos[2], vertices_refletidos[3]]
]

refletido_tetraedro = Poly3DCollection(refletido_arestas, edgecolor='r', linewidths=1, alpha=0.5)
ax.add_collection3d(refletido_tetraedro)

# Exibe o gráfico
plt.show()
