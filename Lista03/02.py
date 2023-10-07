# lembre de baixar as bibliotecas para que animação rode normalmente
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Função para rotacionar um ponto (x, y) em torno da origem (0, 0)
def rotate_point(x, y, theta):
    theta_rad = np.radians(theta)
    x_new = x * np.cos(theta_rad) - y * np.sin(theta_rad)
    y_new = x * np.sin(theta_rad) + y * np.cos(theta_rad)
    return x_new, y_new

# Inicializar a figura e os eixos
fig, ax = plt.subplots()

# Desenhar os eixos X e Y
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)

# Inicializar o ponto P(20, 20)
point, = ax.plot(20, 20, 'ro')  # 'ro' significa red color, round shape (círculo)

# Função de animação
def animate(i):
    global point
    # Rotacionar o ponto em 1 grau
    new_x, new_y = rotate_point(20, 20, i)
    point.set_data(new_x, new_y)
    return point,

# Configurar a animação
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 360, 1), interval=5)

# Definir os limites dos eixos (opcional)
plt.xlim(-30, 30)
plt.ylim(-30, 30)

# Adicionar rótulos para os eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adicionar um título para o gráfico
plt.title('Rotação Contínua de Ponto P(20,20)')

# Mostrar a animação
plt.grid(True)
plt.show()
