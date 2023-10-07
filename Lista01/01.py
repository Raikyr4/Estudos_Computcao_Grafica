import matplotlib.pyplot as plt

#Para instalar a biblioteca usa-se o comando :  !pip install matplotlib
# Definindo as coordenadas do ponto A
x_a = 5
y_a = 5

# Configurando o gráfico
plt.figure(figsize=(10, 10))  # Tamanho da figura
plt.xlim(-10, 10)  # Limites do eixo X
plt.ylim(-10, 10)  # Limites do eixo Y

# Desenhando o ponto A
plt.plot(x_a, y_a, 'ro', markersize=8)  # 'ro' indica vermelho e círculo ('r' - red, 'o' - circle)

# Configurando rótulos dos eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Título do gráfico
plt.title('Gráfico 2D com Ponto A')

# Mostrando o gráfico
plt.grid(True)  # Habilitando as grades
plt.show()
