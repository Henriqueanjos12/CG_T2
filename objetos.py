import numpy as np


def caixa_sem_tampa(lado, altura, origem=(0, 0, 0)):
    ox, oy, oz = origem
    vertices = np.array([
        [ox, oy, oz],
        [ox + lado, oy, oz],
        [ox + lado, oy + lado, oz],
        [ox, oy + lado, oz],
        [ox, oy, oz + altura],
        [ox + lado, oy, oz + altura],
        [ox + lado, oy + lado, oz + altura],
        [ox, oy + lado, oz + altura]
    ])
    faces = [
        [0, 1, 2, 3],  # Base inferior
        [0, 1, 5, 4],  # Face lateral
        [1, 2, 6, 5],  # Face lateral
        [2, 3, 7, 6],  # Face lateral
        [3, 0, 4, 7]  # Face lateral
    ]
    return vertices, faces


# Função que retorna os vértices e faces de um tronco de cone
def tronco_de_cone(raio_base_inferior, raio_base_superior, altura, num_lados=20, origem=(0, 0, 0)):
    ox, oy, oz = origem

    # Vértices da base inferior e superior
    vertices_inferior = []
    vertices_superior = []
    for i in range(num_lados):
        angulo = (2 * np.pi * i) / num_lados
        x_inferior = ox + raio_base_inferior * np.cos(angulo)
        y_inferior = oy + raio_base_inferior * np.sin(angulo)
        vertices_inferior.append([x_inferior, y_inferior, oz])

        x_superior = ox + raio_base_superior * np.cos(angulo)
        y_superior = oy + raio_base_superior * np.sin(angulo)
        vertices_superior.append([x_superior, y_superior, oz + altura])

    # Vértices completos
    vertices = np.array(vertices_inferior + vertices_superior)  # Garantir que seja um numpy array

    # Criando as faces laterais
    num_vertices = len(vertices_inferior)
    faces = [
        [i, (i + 1) % num_vertices, (i + 1) % num_vertices + num_vertices, i + num_vertices]
        for i in range(num_vertices)
    ]

    # Face da base inferior
    faces.append([i for i in range(num_vertices)])

    # Face da base superior
    faces.append([i + num_vertices for i in range(num_vertices)])

    return vertices, faces


# Função para gerar pontos de uma curva de Hermite
def gerar_pontos_curva_hermite(p1, p2, t1, t2, num_pontos=20):
    t = np.linspace(0, 1, num_pontos)
    h1 = 2 * t ** 3 - 3 * t ** 2 + 1
    h2 = -2 * t ** 3 + 3 * t ** 2
    h3 = t ** 3 - 2 * t ** 2 + t
    h4 = t ** 3 - t ** 2
    return h1[:, None] * p1 + h2[:, None] * p2 + h3[:, None] * t1 + h4[:, None] * t2


# Função para criar o cano ao longo de uma curva de Hermite
def cano(p1, p2, t1, t2, raio_cano, num_pontos_trajetoria=20, num_lados=20):
    pontos_trajetoria = gerar_pontos_curva_hermite(p1, p2, t1, t2, num_pontos_trajetoria)
    vertices = []
    faces = []

    # Gerar os vértices para cada ponto da trajetória
    for i in range(num_pontos_trajetoria):
        centro = pontos_trajetoria[i]
        circunferencia = []
        for j in range(num_lados):
            angulo = (2 * np.pi * j) / num_lados
            x = centro[0] + raio_cano * np.cos(angulo)
            y = centro[1] + raio_cano * np.sin(angulo)
            z = centro[2]
            circunferencia.append([x, y, z])
        vertices += circunferencia

    # Criar as faces conectando as circunferências
    for i in range(num_pontos_trajetoria - 1):
        for j in range(num_lados):
            proximo_j = (j + 1) % num_lados
            face = [
                i * num_lados + j,
                i * num_lados + proximo_j,
                (i + 1) * num_lados + proximo_j,
                (i + 1) * num_lados + j
            ]
            faces.append(face)

    return np.array(vertices), faces


# Função para criar um cilindro com fundo
def cilindro_sem_tampa(raio, altura, num_lados=20):
    vertices_base_inferior = []
    vertices_base_superior = []

    # Gerar os vértices das bases
    for i in range(num_lados):
        angulo = (2 * np.pi * i) / num_lados
        x = raio * np.cos(angulo)
        y = raio * np.sin(angulo)
        vertices_base_inferior.append([x, y, 0])  # Base inferior no z = 0
        vertices_base_superior.append([x, y, altura])  # Base superior no z = altura

    # Combinar os vértices das bases
    vertices = vertices_base_inferior + vertices_base_superior
    faces = []

    # Criar faces laterais do cilindro
    for i in range(num_lados):
        proximo = (i + 1) % num_lados
        faces.append([i, proximo, num_lados + proximo, num_lados + i])

    # Adicionar o fundo da base inferior
    centro_base = len(vertices)  # Índice do centro da base inferior
    vertices.append([0, 0, 0])  # Centro da base inferior
    for i in range(num_lados):
        proximo = (i + 1) % num_lados
        faces.append([centro_base, i, proximo])

    return np.array(vertices), faces


# Função para combinar vértices e faces de dois objetos
def combinar_vertices_faces(vertices1, faces1, vertices2, faces2):
    """
    Combina os vértices e faces de dois sólidos 3D.
    """
    offset = len(vertices1)  # Deslocamento para ajustar os índices dos vértices do segundo objeto

    # Combina os vértices
    vertices_comb = np.vstack((vertices1, vertices2))

    # Atualiza e combina as faces, ajustando os índices dos vértices do segundo objeto
    faces_comb = faces1 + [[v + offset for v in face] for face in faces2 if
                           isinstance(face, (list, np.ndarray)) and all(isinstance(v, int) for v in face)]

    return vertices_comb, faces_comb


# Função para compor e visualizar a caneca com alça e fundo
def caneca(raio_caneca=2, altura_caneca=5, raio_alca=0.3):
    # Ajustar a posição inicial e final da alça para que fiquem na mesma face
    angulo_face = np.pi / 2  # Alça conectada em uma face ao longo do eixo Y
    p1 = np.array([raio_caneca * np.cos(angulo_face), raio_caneca * np.sin(angulo_face), altura_caneca * 0.75])
    p2 = np.array([raio_caneca * np.cos(angulo_face), raio_caneca * np.sin(angulo_face), altura_caneca * 0.25])
    t1 = np.array([0, 3, 0])
    t2 = np.array([0, -3, 0])

    # Criar o corpo da caneca (cilindro com fundo)
    vertices_caneca, faces_caneca = cilindro_sem_tampa(raio_caneca, altura_caneca)

    # Criar a alça da caneca
    vertices_alca, faces_alca = cano(p1, p2, t1, t2, raio_alca)

    # Combinar os vértices e faces da caneca e da alça
    vertices_comb, faces_comb = combinar_vertices_faces(
        vertices_caneca, faces_caneca,
        vertices_alca, faces_alca
    )

    # Retornar os vértices e faces combinados
    return vertices_comb, faces_comb
