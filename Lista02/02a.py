import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Defina os vértices do cubo
vertices = np.array([
    [0, 0, 0],  # Vértice 0 (origem)
    [1, 0, 0],  # Vértice 1
    [1, 1, 0],  # Vértice 2
    [0, 1, 0],  # Vértice 3
    [0, 0, 1],  # Vértice 4
    [1, 0, 1],  # Vértice 5
    [1, 1, 1],  # Vértice 6
    [0, 1, 1]   # Vértice 7
])

# Defina as faces do cubo
faces = [
    [vertices[0], vertices[1], vertices[2], vertices[3]],  # Face inferior
    [vertices[4], vertices[5], vertices[6], vertices[7]],  # Face superior
    [vertices[0], vertices[1], vertices[5], vertices[4]],  # Face frontal
    [vertices[2], vertices[3], vertices[7], vertices[6]],  # Face traseira
    [vertices[0], vertices[3], vertices[7], vertices[4]],  # Face esquerda
    [vertices[1], vertices[2], vertices[6], vertices[5]]   # Face direita
]

# Crie uma figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Desenhe o cubo
cubo = Poly3DCollection(faces, edgecolor='k', linewidths=1, alpha=0.5)
ax.add_collection3d(cubo)

# Aplicar cisalhamento em relação à face no plano XZ
shear_matrix = np.array([
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1]
])

sheared_vertices = np.dot(vertices, shear_matrix.T)

# Atualize os vértices do cubo após o cisalhamento
for i in range(len(vertices)):
    vertices[i] = sheared_vertices[i]

# Atualize as faces do cubo após o cisalhamento
faces = [
    [vertices[0], vertices[1], vertices[2], vertices[3]],
    [vertices[4], vertices[5], vertices[6], vertices[7]],
    [vertices[0], vertices[1], vertices[5], vertices[4]],
    [vertices[2], vertices[3], vertices[7], vertices[6]],
    [vertices[0], vertices[3], vertices[7], vertices[4]],
    [vertices[1], vertices[2], vertices[6], vertices[5]]
]

# Desenhe o cubo cisalhado
cubo_shear = Poly3DCollection(faces, edgecolor='r', linewidths=1, alpha=0.5)
ax.add_collection3d(cubo_shear)

# Configurar limites dos eixos
ax.set_xlim([0, 2])
ax.set_ylim([0, 2])
ax.set_zlim([0, 2])

# Exibir o gráfico
plt.show()
