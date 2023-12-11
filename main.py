import numpy as np

import objetos as obj
import plot
import tranformacoes as trans

# Questão 1
vertices, arestas = obj.cilindro(4, 3, 20)
plot.plot_3d(vertices, arestas, 'blue', 'red')

vertices, arestas = obj.cone(4, 3, 20)
plot.plot_3d(vertices, arestas, 'red', 'green')

vertices, arestas = obj.cubo(5, 2)
plot.plot_3d(vertices, arestas, 'green', 'blue')

vertices, arestas = obj.tronco_piramide(2, 4, 10, 2, 5)
plot.plot_3d(vertices, arestas, 'yellow', 'purple')

vertices, arestas = obj.esferas(5, 3, 10, 10)
plot.plot_3d(vertices, arestas, 'yellow', 'black')

vertices, arestas = obj.toroide(5, 5, (0, 0, 0), 10, 10)
plot.plot_3d(vertices, arestas, 'pink', 'black')

# Questão 2
cenario1 = plot.cria_cenario()

vertices_cilindro, arestas_cilindro = obj.cilindro(3, 8, 20)
plot.plota_cenario(cenario1, vertices_cilindro, arestas_cilindro, 'red')
vertices_cone, arestas_cone = obj.cone(raio=3, num_circunferencias=3, num_arestas_base=20)
plot.plota_cenario(cenario1, vertices_cone, arestas_cone, 'green')
vertices_cubo, arestas_cubo = obj.cubo(4)
plot.plota_cenario(cenario1, vertices_cubo, arestas_cubo, 'blue')
vertices_piramide, arestas_piramide = obj.tronco_piramide(lado_menor=2, lado_maior=4, altura=8, num_trapezios=2,
                                                          num_arestas_base=3)
plot.plota_cenario(cenario1, vertices_piramide, arestas_piramide, 'yellow')
vertices_toroide, arestas_toroide = obj.toroide(R=4, r=1, centro=(0, 0, 0), num_fatias=15, num_arestas_meridiano=20)
plot.plota_cenario(cenario1, vertices_toroide, arestas_toroide, 'black')
vertices_esfera, arestas_esfera = obj.esfera(raio=4, centro=(0, 0, 0), num_fatias=10, num_arestas_meridiano=10)
plot.plota_cenario(cenario1, vertices_esfera, arestas_esfera, 'orange')

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
plot.plota_cenario(cenario2, vertices_escalonados_cilindro, arestas_cilindro, 'red')

# cubo
vertices_rotacionadosZ_cubo = trans.rotacao_z(vertices_cubo, 30)
vertices_transladados_cubo = trans.translator(vertices_rotacionadosZ_cubo, 10, 7, 5)
vertices_escalonados_cubo = trans.escala(vertices_transladados_cubo, 1 / 2, 1 / 2, 1 / 2)
plot.plota_cenario(cenario2, vertices_escalonados_cubo, arestas_cubo, 'blue')

# esfera
vertices_transladados_esfera = trans.translator(vertices_esfera, 10, 10, 7)
vertices_escalonados_esfera = trans.escala(vertices_transladados_esfera, 2 / 3, 2 / 3, 2 / 3)
plot.plota_cenario(cenario2, vertices_escalonados_esfera, arestas_esfera, 'orange')

# cone
vertices_transladados_cone = trans.translator(vertices_cone, -5, -15, 7)
vertices_escalonados_cone = trans.escala(vertices_transladados_cone, 2 / 4, 2 / 4, 2 / 4)
plot.plota_cenario(cenario2, vertices_escalonados_cone, arestas_cone, 'green')

# piramide
vertices_rotacionadosZ_piramide = trans.rotacao_z(vertices_piramide, 45)
vertices_transladados_piramide = trans.translator(vertices_rotacionadosZ_piramide, -3, -4, 5)
vertices_escalonados_piramide = trans.escala(vertices_transladados_piramide, 2 / 4, 2 / 4, 2 / 4)
plot.plota_cenario(cenario2, vertices_escalonados_piramide, arestas_piramide, 'yellow')

# toroide
vertices_rotacionadosZ_toroide = trans.rotacao_x(vertices_toroide, -30)
vertices_transladados_toroide = trans.translator(vertices_rotacionadosZ_toroide, -20, -10, 10)
vertices_escalonados_toroide = trans.escala(vertices_transladados_toroide, 1 / 3, 1 / 3, 1 / 3)
plot.plota_cenario(cenario2, vertices_escalonados_toroide, arestas_toroide, 'black')

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)

cenario2.plot_surface(X, Y, Z, color='red', alpha=0.1)
cenario2.plot_surface(X, Z, Y, color='green', alpha=0.1)
cenario2.plot_surface(Z, X, Y, color='blue', alpha=0.1)

plot.plt.grid()
plot.plt.show()
