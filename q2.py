import numpy as np
import objetos as obj
import plot
import q1
import transformacoes as trans

# Dicionário para objetos
mundo = {}
mundo_trans = {}

# Questão 2
cenario1 = plot.cria_cenario()  # cenario1 é o eixo (ax) retornado por cria_cenario

# Caixa sem tampa (Cubo)
vertices_caixa, faces_caixa = obj.caixa_sem_tampa(4, 5, (0, 0, 0))
mundo["caixa"] = (vertices_caixa, faces_caixa, 'black', 'blue', 'yellow')

# Cone
vertices_cone, faces_cone = obj.tronco_de_cone(3, 0, 6, 25)
mundo["cone"] = (vertices_cone, faces_cone, 'red', 'green', 'orange')

# Tronco de cone
vertices_tronco_cone, faces_tronco_cone = obj.tronco_de_cone(3, 2, 6, 25)
mundo["tronco_cone"] = (vertices_tronco_cone, faces_tronco_cone, 'green', 'cyan', 'lime')

# Parâmetros do cano
raio_cano = 2
P1 = q1.P1  # Início da curva Hermite
P2 = q1.P2  # Fim da curva Hermite
T1 = q1.T1  # Vetor tangente inicial
T2 = q1.T2  # Vetor tangente final

# Cano
vertices_cano, faces_cano = obj.cano(P1, P2, T1, T2, raio_cano)
mundo["cano"] = (vertices_cano, faces_cano, 'purple', 'magenta', 'pink')

# Cilindro sem Tampa
vertices_cilindro, faces_cilindro = obj.cilindro_sem_tampa(2, 5)
mundo["cilindro"] = (vertices_cilindro, faces_cilindro, 'orange', 'salmon', 'brown')

# Criar a caneca
vertices_caneca, faces_caneca = obj.caneca(2, 5, 0.3)
mundo["caneca"] = (vertices_caneca, faces_caneca, 'blue', 'lightblue', 'skyblue')

# Loop para plotar todos os objetos com suas cores definidas no cenário 1
for objeto in mundo:
    print(f"Plotando {objeto}")
    vertices, faces, cor_vertice, cor_arestas, cor_faces = mundo[objeto]
    plot.plota_cenario(cenario1, vertices, faces, cor_vertice=cor_vertice, cor_arestas=cor_arestas, cor_faces=cor_faces)

# Criação das superfícies para o cenário
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)

# Plotar as superfícies no mesmo eixo (cenario1)
cenario1.plot_surface(X, Y, Z, color='red', alpha=0.1)
cenario1.plot_surface(X, Z, Y, color='green', alpha=0.1)
cenario1.plot_surface(Z, X, Y, color='blue', alpha=0.1)

# Definir o título para o primeiro cenário
cenario1.set_title("Mundo Original", fontsize=14, color='red')

# Exibir o grid e o gráfico
plot.plt.grid()
plot.plt.show()

# Criação do segundo cenário com cores iguais, mas objetos transformados
cenario2 = plot.cria_cenario()

# **Transformação da Caixa**
vertices_escalonados_caixa = trans.escala(vertices_caixa, 0.5, 0.5, 0.5)
vertices_transladados_caixa = trans.translacao(vertices_escalonados_caixa, -5, 5, 3)
mundo_trans["caixa"] = (vertices_transladados_caixa, faces_caixa, mundo["caixa"][2], mundo["caixa"][3], mundo["caixa"][4])

# **Transformação do Cone**
vertices_rotacionadosZ_cubo = trans.rotacao_z(vertices_cone, 30)
vertices_transladados_cone = trans.translacao(vertices_cone, 10, 7, 5)
vertices_escalonados_cone = trans.escala(vertices_transladados_cone, 1 / 2, 1 / 2, 1 / 2)
mundo_trans["cone"] = (vertices_escalonados_cone, faces_cone, mundo["cone"][2], mundo["cone"][3], mundo["cone"][4])

# **Transformação do Cano**
vertices_transladados_cano = trans.translacao(vertices_cano, 4, 8, 7)
vertices_escalonados_cano = trans.escala(vertices_transladados_cano, 2 / 3, 2 / 3, 2 / 3)
mundo_trans["cano"] = (vertices_escalonados_cano, faces_cano, mundo["cano"][2], mundo["cano"][3], mundo["cano"][4])

# **Transformação do Tronco de Cone**
vertices_transladados_tronco_cone = trans.translacao(vertices_tronco_cone, -5, -15, 7)
vertices_escalonados_tronco_cone = trans.escala(vertices_transladados_tronco_cone, 2 / 4, 2 / 4, 2 / 4)
mundo_trans["tronco_cone"] = (vertices_escalonados_tronco_cone, faces_tronco_cone, mundo["tronco_cone"][2], mundo["tronco_cone"][3], mundo["tronco_cone"][4])

# **Transformação da Caneca**
vertices_rotacionadosZ_caneca = trans.rotacao_z(vertices_caneca, 45)
vertices_transladados_caneca = trans.translacao(vertices_caneca, -3, -4, 5)
vertices_escalonados_caneca = trans.escala(vertices_transladados_caneca, 2 / 4, 2 / 4, 2 / 4)
mundo_trans["caneca"] = (vertices_escalonados_caneca, faces_caneca, mundo["caneca"][2], mundo["caneca"][3], mundo["caneca"][4])

# Loop para plotar todos os objetos no cenário 2
for objeto in mundo_trans:
    print(f"Plotando {objeto}")
    vertices, faces, cor_vertice, cor_arestas, cor_faces = mundo_trans[objeto]
    plot.plota_cenario(cenario2, vertices, faces, cor_vertice=cor_vertice, cor_arestas=cor_arestas, cor_faces=cor_faces)

# Criação das superfícies para o cenário 2
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)

cenario2.plot_surface(X, Y, Z, color='red', alpha=0.1)
cenario2.plot_surface(X, Z, Y, color='green', alpha=0.1)
cenario2.plot_surface(Z, X, Y, color='blue', alpha=0.1)

# Definir o título para o segundo cenário
cenario2.set_title("Mundo Transformado", fontsize=14, color='red')

plot.plt.grid()
plot.plt.show()
