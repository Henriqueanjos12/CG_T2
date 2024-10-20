import numpy as np

import q2


# Função para calcular o centro de massa de um conjunto de vértices
def calcular_centro_massa(vertices):
    return np.mean(vertices, axis=0)


# Determinar o octante que será o volume de visão (octante com objetos)
def esta_no_octante(centro_massa, octante):
    x_sign, y_sign, z_sign = octante
    return ((x_sign > 0 and centro_massa[0] > 0) or (x_sign < 0 and centro_massa[0] < 0)) and \
        ((y_sign > 0 and centro_massa[1] > 0) or (y_sign < 0 and centro_massa[1] < 0)) and \
        ((z_sign > 0 and centro_massa[2] > 0) or (z_sign < 0 and centro_massa[2] < 0))


# Escolher o octante com os objetos como o volume de visão (exemplo: primeiro octante)
octante_objetos = (1, 1, 1)  # Exemplo: primeiro octante (x > 0, y > 0, z > 0)

# Filtrar os sólidos que estão no volume de visão (octante com objetos)
objetos_no_octante = {}
for nome, (vertices, faces, cor_vertice, cor_arestas, cor_faces) in q2.mundo_trans.items():
    centro_massa = calcular_centro_massa(vertices)
    print(f"Centro de massa de {nome}: {centro_massa}")  # Diagnóstico
    if esta_no_octante(centro_massa, octante_objetos):
        objetos_no_octante[nome] = (vertices, faces, cor_vertice, cor_arestas, cor_faces)

# Verificar se há sólidos no volume de visão
if len(objetos_no_octante) == 0:
    raise ValueError("Nenhum sólido foi encontrado no volume de visão (octante selecionado).")

# Calcular o ponto médio dos centros de massa dos sólidos no volume de visão
centros_de_massa = [calcular_centro_massa(obj[0]) for obj in objetos_no_octante.values()]
ponto_medio = np.mean(centros_de_massa, axis=0)
print(f"Ponto médio entre os objetos no volume de visão: {ponto_medio}")  # Diagnóstico

# Escolher um octante vazio para posicionar a câmera (exemplo: terceiro octante)
origem_camera = np.array([-10, -10, 10])  # (x < 0, y < 0, z > 0)

# a. Computar a base vetorial do sistema de coordenadas da câmera
n_camera = ponto_medio - origem_camera  # Vetor que aponta da câmera para os objetos
n_camera = n_camera / np.linalg.norm(n_camera)  # Normalizar o vetor

u_camera = np.cross([0, 1, 0], n_camera)  # Vetor 'u' ortogonal ao eixo y
u_camera = u_camera / np.linalg.norm(u_camera)  # Normalizar

v_camera = np.cross(n_camera, u_camera)  # Vetor 'v' perpendicular a 'n' e 'u'
v_camera = v_camera / np.linalg.norm(v_camera)  # Normalizar

# Não rotacionamos os objetos, apenas ajustamos a visualização da câmera
# Criar uma nova figura 3D para a visão da câmera
fig = plot.plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotar os objetos no sistema de coordenadas original (sem aplicar transformações nos objetos)
for objeto, dados in objetos_no_octante.items():
    vertices, faces, cor_vertice, cor_arestas, cor_faces = dados
    plot.plota_cenario(ax, vertices, faces, cor_vertice=cor_vertice, cor_arestas=cor_arestas, cor_faces=cor_faces)

# Ajustar os limites do volume de visão
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)

# Ajustar a visualização da câmera (usando a base vetorial da câmera)
ax.view_init(elev=np.arcsin(n_camera[2]) * 180 / np.pi, azim=np.arctan2(n_camera[1], n_camera[0]) * 180 / np.pi)

# Definir o título "Coordenada da câmera"
ax.set_title("Coordenada da câmera", fontsize=14, color='red')

# Configurar o grid e mostrar a visualização final
plot.plt.grid()
plot.plt.show()
