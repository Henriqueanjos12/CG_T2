import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection


def plot_3d(vertices, arestas, cor_vertice = 'black', cor_arestas = 'red'):
    print("Número de vértices:", len(vertices))
    print(vertices)
    print("Número de arestas:", len(arestas))
    print(arestas)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plotar vértices
    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color=cor_vertice, marker='o', label='Vértices')
    # Plotar arestas
    arestas_conjunto = set(map(tuple, arestas))
    ax.add_collection3d(
        Poly3DCollection([vertices[list(aresta)] for aresta in arestas_conjunto], color=cor_arestas, linewidths=1,
                         edgecolors='red', alpha=1))
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.legend()
    plt.show()


def plota_cenario(ax, vertices, arestas, cor):
    vertices_homogeneous = np.concatenate([vertices, np.ones((vertices.shape[0], 1))], axis=-1).T
    vertices_transformados = vertices_homogeneous[:3, :].T

    linhas = [(vertices_transformados[aresta[0]], vertices_transformados[aresta[1]]) for aresta in arestas]
    pontos_plotados = Line3DCollection(linhas, colors=cor)

    ax.add_collection3d(pontos_plotados)

    return pontos_plotados


def cria_cenario():
    fig = plt.figure(figsize=(15, 12))

    # fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.set_title('Coordenadas do Mundo')

    # Define os limites do gráfico
    limites = [-10, 10]
    for s in [-1, 1]:
        ax.plot([0, 0], [0, 0], [s * limites[0], s * limites[1]], color='k', linestyle='-', linewidth=1)
        ax.plot([0, 0], [s * limites[0], s * limites[1]], [0, 0], color='k', linestyle='-', linewidth=1)
        ax.plot([s * limites[0], s * limites[1]], [0, 0], [0, 0], color='k', linestyle='-', linewidth=1)
        # Legenda

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    return ax
