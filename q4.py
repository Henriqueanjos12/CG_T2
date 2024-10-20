import numpy as np
import matplotlib.pyplot as plt
import q3  # Certifique-se de que q3 contém os objetos filtrados no volume de visão
import transformacoes as tf  # Importando as funções de rotação refatoradas


# Função para projetar um ponto 3D em 2D usando uma projeção em perspectiva
def projecao_perspectiva(vertices, origem_camera, plano_projecao_z):
    vertices_projetados = []
    for vertice in vertices:
        z_relativo = vertice[2] - origem_camera[2]
        if z_relativo != 0:  # Evitar divisão por zero
            fator_projecao = plano_projecao_z / z_relativo
            x_proj = fator_projecao * (vertice[0] - origem_camera[0])
            y_proj = fator_projecao * (vertice[1] - origem_camera[1])
            vertices_projetados.append([x_proj, y_proj])
        else:
            print(f"Vértice {vertice} está na mesma posição da câmera, projeção não possível.")
    return np.array(vertices_projetados)


# Função para plotar os sólidos projetados em 2D
def plotar_2d_solid(ax, vertices_projetados, faces, cor_arestas):
    for face in faces:
        for i in range(len(face)):
            p1 = vertices_projetados[face[i]]
            p2 = vertices_projetados[face[(i + 1) % len(face)]]
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=cor_arestas)


# Verificar se há sólidos no volume de visão
if len(q3.objetos_no_octante) == 0:
    raise ValueError("Nenhum sólido foi encontrado no volume de visão (octante selecionado).")

# Definir a origem da câmera e o plano de projeção
origem_camera = np.array([-10, -10, 10])  # Posição da câmera
plano_projecao_z = 10  # Distância do plano de projeção em relação à câmera

# Criar figura 2D para exibir a projeção
fig, ax = plt.subplots()

# Definir o ângulo de rotação (em radianos)
angulo_rotacao = np.radians(45)

# Escolher o eixo de rotação (pode ser alterado para 'x', 'y' ou 'z')
eixo_rotacao = 'y'  # Pode ser 'x', 'y' ou 'z'

# Projeção em perspectiva e plotagem dos sólidos em 2D
for nome, (vertices, faces, cor_vertice, cor_arestas, cor_faces) in q3.objetos_no_octante.items():
    # Aplicar a rotação nos vértices do sólido usando as funções de rotação refatoradas
    if eixo_rotacao == 'x':
        vertices_rotacionados = tf.rotacao_x(vertices, angulo_rotacao)
    elif eixo_rotacao == 'y':
        vertices_rotacionados = tf.rotacao_y(vertices, angulo_rotacao)
    elif eixo_rotacao == 'z':
        vertices_rotacionados = tf.rotacao_z(vertices, angulo_rotacao)
    else:
        raise ValueError("Eixo de rotação inválido. Escolha entre 'x', 'y' ou 'z'.")

    # Projetar os vértices do sólido em 2D
    vertices_projetados = projecao_perspectiva(vertices_rotacionados, origem_camera, plano_projecao_z)

    # Plotar o sólido projetado em 2D
    plotar_2d_solid(ax, vertices_projetados, faces, cor_arestas)

# Ajustar limites do gráfico para que os objetos fiquem visíveis
ax.set_xlim(-25, -8)
ax.set_ylim(-25, -8)

# Manter a proporção dos eixos x e y para evitar distorções
ax.set_aspect('equal')

# Ocultar os números dos ticks, mas manter o grid
ax.tick_params(axis='both', which='both', bottom=False, top=False, left=False, right=False, labelbottom=False,
               labelleft=False)

# Manter o grid ativo
ax.grid(True)

# Definir título para a visualização 2D
ax.set_title("Projeção em Perspectiva dos Sólidos Rotacionados em 2D", fontsize=14)

# Mostrar a figura
plt.show()
