import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def plot_3d(vertices, faces, ax=None, cor_vertice='black', cor_arestas='red', cor_faces='green', title=None):
    print("Número de vértices:", len(vertices))
    print(vertices)
    print("Número de faces:", len(faces))
    print(faces)

    # Se um eixo não for fornecido, criar uma nova figura e eixo 3D
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

    # Plotar vértices
    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color=cor_vertice, marker='o', label='Vértices')

    # Plotar faces com cor específica
    ax.add_collection3d(
        Poly3DCollection([vertices[face] for face in faces], facecolors=cor_faces, linewidths=1, edgecolors=cor_arestas,
                         alpha=0.5)
    )

    # Definir os rótulos dos eixos
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Definir o título, se fornecido
    if title:
        ax.set_title(title, fontsize=14)

    # Mostrar a legenda
    ax.legend()

    # Mostrar o gráfico se não houver um eixo fornecido
    if ax is None:
        plt.show()


def plota_cenario(ax, vertices, faces, cor_vertice='black', cor_arestas='red', cor_faces='green'):
    """
    Função para plotar um cenário 3D com vértices e faces.

    :param ax: Axes 3D para plotagem.
    :param vertices: Array de vértices 3D.
    :param faces: Lista de listas, onde cada lista define os índices dos vértices que formam uma face.
    :param cor_vertice: Cor dos vértices.
    :param cor_arestas: Cor das arestas (contorno das faces).
    :param cor_faces: Cor das faces.
    """
    # Plotar vértices
    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color=cor_vertice, marker='o', label='Vértices')

    # Criar as faces como polígonos 3D
    face_polys = Poly3DCollection([vertices[face] for face in faces], facecolors=cor_faces, linewidths=1,
                                  edgecolors=cor_arestas, alpha=0.5)

    # Adicionar as faces ao gráfico
    ax.add_collection3d(face_polys)

    # Definir os rótulos dos eixos
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    return face_polys


def cria_cenario():
    """
    Função que cria o cenário base 3D com os eixos coordenados e limites definidos.
    """
    fig = plt.figure(figsize=(15, 12))

    # Criar o subplot 3D
    ax = fig.add_subplot(111, projection='3d')
    # ax.set_title('Coordenadas do Mundo')

    # Definir os limites do gráfico
    limites = [-10, 10]
    ax.set_xlim(limites)
    ax.set_ylim(limites)
    ax.set_zlim(limites)

    # Desenhar as linhas dos eixos coordenados
    for s in [-1, 1]:
        ax.plot([0, 0], [0, 0], [s * limites[0], s * limites[1]], color='k', linestyle='-', linewidth=1)
        ax.plot([0, 0], [s * limites[0], s * limites[1]], [0, 0], color='k', linestyle='-', linewidth=1)
        ax.plot([s * limites[0], s * limites[1]], [0, 0], [0, 0], color='k', linestyle='-', linewidth=1)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    return ax
