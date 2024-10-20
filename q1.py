import numpy as np

import objetos as obj
import plot

# Parâmetros do cano
raio_cano = 2
P1 = np.array([0, 0, 0])  # Início da curva Hermite
P2 = np.array([5, 0, 5])  # Fim da curva Hermite
T1 = np.array([5, 5, 0])  # Vetor tangente inicial
T2 = np.array([-5, 5, 0])  # Vetor tangente final

# Plotar cada objeto separadamente

# 1. Caixa sem tampa
vertices_caixa, faces_caixa = obj.caixa_sem_tampa(4, 5, (0, 0, 0))
print("Plotando caixa sem tampa")
ax1 = plot.plt.figure().add_subplot(111, projection='3d')
plot.plot_3d(vertices_caixa, faces_caixa, ax=ax1, cor_vertice='black', cor_arestas='red', cor_faces='yellow')
ax1.set_title("Caixa sem Tampa", fontsize=14, color='red')

# 2. Cone
vertices_cone, faces_cone = obj.tronco_de_cone(3, 0, 6, 25)
print("Plotando cone")
ax2 = plot.plt.figure().add_subplot(111, projection='3d')
plot.plot_3d(vertices_cone, faces_cone, ax=ax2, cor_vertice='blue', cor_arestas='blue', cor_faces='cyan')
ax2.set_title("Cone", fontsize=14, color='red')

# 3. Tronco de cone
vertices_tronco_cone, faces_tronco_cone = obj.tronco_de_cone(3, 2, 6, 25)
print("Plotando tronco de cone")
ax3 = plot.plt.figure().add_subplot(111, projection='3d')
plot.plot_3d(vertices_tronco_cone, faces_tronco_cone, ax=ax3, cor_vertice='green', cor_arestas='green',
             cor_faces='lime')
ax3.set_title("Tronco de Cone", fontsize=14, color='red')

# 4. Cano
vertices_cano, faces_cano = obj.cano(P1, P2, T1, T2, raio_cano)
print("Plotando cano")
ax4 = plot.plt.figure().add_subplot(111, projection='3d')
plot.plot_3d(vertices_cano, faces_cano, ax=ax4, cor_vertice='purple', cor_arestas='purple', cor_faces='magenta')
ax4.set_title("Cano", fontsize=14, color='red')

# 5. Caneca
vertices_caneca, faces_caneca = obj.caneca(2, 5, 0.3)
print("Plotando caneca")
ax5 = plot.plt.figure().add_subplot(111, projection='3d')
plot.plot_3d(vertices_caneca, faces_caneca, ax=ax5, cor_vertice='red', cor_arestas='red', cor_faces='pink')
ax5.set_title("Caneca", fontsize=14, color='red')

# Exibir o grid e o gráfico
plot.plt.grid()
plot.plt.show()
