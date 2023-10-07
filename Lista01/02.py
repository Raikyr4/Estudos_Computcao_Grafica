import matplotlib.pyplot as plt

# Definindo as coordenadas dos pontos A e B
x_a, y_a = 3, 2
x_b, y_b = 6, 8

# Configurando o gráfico
plt.figure(figsize=(10, 10))  # Tamanho da figura
plt.xlim(0, 10)  # Limites do eixo X
plt.ylim(0, 10)  # Limites do eixo Y

# Desenhando o ponto A (verde - 'o')
plt.plot(x_a, y_a, 'go', markersize=8, label='Ponto A')

# Desenhando o ponto B (azul - '+')
plt.plot(x_b, y_b, 'b+', markersize=10, label='Ponto B')

# Configurando rótulos dos eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Título do gráfico
plt.title('Gráfico 2D com Pontos A e B')

# Mostrando a legenda
plt.legend()

# Mostrando o gráfico
plt.grid(True)  # Habilitando as grades
plt.show()
