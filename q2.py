import numpy as np
import objetos as obj
import plot
import tranformacoes as trans

# Dicionário para objetos
mundo = {}
mundo_trans = {}


# Questão 2
cenario1 = plot.cria_cenario()

vertices_cilindro, arestas_cilindro = obj.cilindro(3, 8, 20)
mundo["cilindro"] = (vertices_cilindro, arestas_cilindro,'red')

vertices_cone, arestas_cone = obj.cone(raio=3, num_circunferencias=3, num_arestas_base=20)
mundo["cone"] = (vertices_cone, arestas_cone,'green')

vertices_cubo, arestas_cubo = obj.cubo(4)
mundo["cubo"] = (vertices_cubo, arestas_cubo,'blue')

vertices_piramide, arestas_piramide = obj.tronco_piramide(lado_menor=2, lado_maior=4, altura=8, num_trapezios=2, num_arestas_base=3)
mundo["tronco_piramide"] = (vertices_piramide, arestas_piramide,'yellow')

vertices_toroide, arestas_toroide = obj.toroide(R=4, r=1, centro=(0, 0, 0), num_fatias=15, num_arestas_meridiano=20)
mundo["toroide"] = (vertices_toroide, arestas_toroide,'pink')

vertices_esfera, arestas_esfera = obj.esfera(raio=4, centro=(0, 0, 0), num_fatias=10, num_arestas_meridiano=10)
mundo["esfera"] = (vertices_esfera, arestas_esfera, 'orange')

for objeto in mundo:
    print(objeto)
    vertices, arestas, cor = mundo[objeto]
    plot.plota_cenario(cenario1, vertices, arestas, cor)

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)

cenario1.plot_surface(X, Y, Z, color='red', alpha=0.1)
cenario1.plot_surface(X, Z, Y, color='green', alpha=0.1)
cenario1.plot_surface(Z, X, Y, color='blue', alpha=0.1)

plot.plt.grid()
plot.plt.show()

cenario2 = plot.cria_cenario()

# cilindro
vertices_transladados_cilindro = trans.translator(vertices_cilindro, 4, 8, 7)
vertices_escalonados_cilindro = trans.escala(vertices_transladados_cilindro, 1 / 2, 1 / 2, 1 / 2)
mundo_trans["cilindro"] = (vertices_escalonados_cilindro, arestas_cilindro,'red')
# cubo
vertices_rotacionadosZ_cubo = trans.rotacao_z(vertices_cubo, 30)
vertices_transladados_cubo = trans.translator(vertices_rotacionadosZ_cubo, 10, 7, 5)
vertices_escalonados_cubo = trans.escala(vertices_transladados_cubo, 1 / 2, 1 / 2, 1 / 2)
mundo_trans["cubo"] = (vertices_escalonados_cubo, arestas_cubo, 'blue')

# esfera
vertices_transladados_esfera = trans.translator(vertices_esfera, 10, 10, 7)
vertices_escalonados_esfera = trans.escala(vertices_transladados_esfera, 2 / 3, 2 / 3, 2 / 3)
mundo_trans["esfera"] = (vertices_escalonados_esfera, arestas_esfera, 'orange')

# cone
vertices_transladados_cone = trans.translator(vertices_cone, -5, -15, 7)
vertices_escalonados_cone = trans.escala(vertices_transladados_cone, 2 / 4, 2 / 4, 2 / 4)
mundo_trans["cone"] = (vertices_escalonados_cone, arestas_cone, 'green')

# piramide
vertices_rotacionadosZ_piramide = trans.rotacao_z(vertices_piramide, 45)
vertices_transladados_piramide = trans.translator(vertices_rotacionadosZ_piramide, -3, -4, 5)
vertices_escalonados_piramide = trans.escala(vertices_transladados_piramide, 2 / 4, 2 / 4, 2 / 4)
mundo_trans["piramide"] = (vertices_escalonados_piramide, arestas_piramide, 'yellow')

# toroide
vertices_rotacionadosZ_toroide = trans.rotacao_x(vertices_toroide, -30)
vertices_transladados_toroide = trans.translator(vertices_rotacionadosZ_toroide, -20, -10, 10)
vertices_escalonados_toroide = trans.escala(vertices_transladados_toroide, 1 / 3, 1 / 3, 1 / 3)
mundo_trans["toroide"] = (vertices_escalonados_toroide, arestas_toroide, 'pink')


for objeto in mundo_trans:
    print(objeto)
    vertices, arestas, cor = mundo_trans[objeto]
    plot.plota_cenario(cenario2, vertices, arestas, cor)

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)

cenario2.plot_surface(X, Y, Z, color='red', alpha=0.1)
cenario2.plot_surface(X, Z, Y, color='green', alpha=0.1)
cenario2.plot_surface(Z, X, Y, color='blue', alpha=0.1)

plot.plt.grid()
plot.plt.show()