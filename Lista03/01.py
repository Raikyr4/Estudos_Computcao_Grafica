import matplotlib.pyplot as plt

# Criar os eixos
fig, ax = plt.subplots()

# Desenhar os eixos X e Y
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)

# Adicionar o ponto P(20,20)
ax.plot(20, 20, 'ro')  # 'ro' significa red color, round shape (círculo)

# Definir os limites dos eixos (opcional)
plt.xlim(-10, 30)
plt.ylim(-10, 30)

# Adicionar rótulos para os eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adicionar um título para o gráfico
plt.title('Tela 2D com Ponto P(20,20)')

# Mostrar o gráfico
plt.grid(True)
plt.show()
