import math

import numpy as np


def cilindro_cone_cubo_piramide(raio_base, altura, centro=(0, 0, 0), raio_topo=0.5, num_fatias=10, num_arestas_base=4):
    lista_vertices = []  # Lista para armazenar os vértices da malha
    lista_arestas = []  # Lista para armazenar as arestas da malha
    # Inicializa as variáveis de coordenadas da seção anterior
    x_ant, y_ant, z_ant = None, None, None

    # Gera valores para a coordenada z ao longo da altura
    z_valores = np.linspace(centro[2] - altura / 2, centro[2] + altura / 2, num_fatias)

    for i in range(num_fatias):
        # Gera valores de theta (ângulo) para criar as seções circulares
        theta = np.linspace(0, 2 * np.pi, num_arestas_base, endpoint=False)
        raio = raio_base + (raio_topo - raio_base) * (i / (num_fatias - 1))

        # Calcula as coordenadas x, y e z para cada ponto na seção circular
        x = centro[0] + raio * np.cos(theta)
        y = centro[1] + raio * np.sin(theta)
        z_val = np.full_like(theta, z_valores[i])

        # Adiciona os vértices gerados à lista de vértices
        lista_vertices.extend(zip(x, y, z_val))

        # Cria as arestas conectando os vértices na seção atual com os da seção anterior
        if i > 0:
            lista_arestas.extend(zip(
                [lista_vertices.index((x_ant[j], y_ant[j], z_ant[j])) for j in range(len(x_ant))],
                [lista_vertices.index((x[j], y[j], z_val[j])) for j in range(len(x))]
            ))

        # Cria as arestas conectando os vértices na seção atual entre si
        lista_arestas.extend(zip(
            [lista_vertices.index((x[j], y[j], z_val[j])) for j in range(len(x) - 1)],
            [lista_vertices.index((x[j + 1], y[j + 1], z_val[j + 1])) for j in range(len(x) - 1)]
        ))

        # Conecta o último vértice ao primeiro vértice para fechar a seção circular
        lista_arestas.append(
            (lista_vertices.index((x[-1], y[-1], z_val[-1])), lista_vertices.index((x[0], y[0], z_val[0]))))

        # Atualiza as variáveis de coordenadas da seção anterior
        x_ant, y_ant, z_ant = x, y, z_val

    # Converte as listas de vértices e arestas em arrays numpy
    array_vertices = np.array(lista_vertices)
    array_arestas = np.array(lista_arestas)

    return array_vertices, array_arestas


def esfera(raio, centro=(0, 0, 0), num_fatias=100, num_arestas_meridiano=100):
    lista_vertices = []  # Lista para armazenar os vértices da malha
    lista_arestas = []  # Lista para armazenar as arestas da malha

    # Gera valores de inclinação (ângulo polar) na esfera
    phi = np.linspace(0, np.pi, num_fatias)

    # Gera valores de longitude (ângulo azimutal) na esfera
    theta = np.linspace(0, 2 * np.pi, num_arestas_meridiano + 1)

    for i in range(num_fatias):
        for j in range(num_arestas_meridiano + 1):
            # Coordenadas esféricas para cartesianas
            x = centro[0] + raio * np.sin(phi[i]) * np.cos(theta[j])
            y = centro[1] + raio * np.sin(phi[i]) * np.sin(theta[j])
            z = centro[2] + raio * np.cos(phi[i])

            lista_vertices.append((x, y, z))  # Adiciona o vértice à lista

            if i < num_fatias - 1 and j < num_arestas_meridiano:
                # Cria arestas conectando vértices adjacentes na mesma linha de longitude
                aresta1 = i * (num_arestas_meridiano + 1) + j
                aresta2 = aresta1 + 1
                aresta3 = (aresta1 + num_arestas_meridiano + 1) % (num_fatias * (num_arestas_meridiano + 1))
                aresta4 = (aresta2 + num_arestas_meridiano + 1) % (num_fatias * (num_arestas_meridiano + 1))

                lista_arestas.append((aresta1, aresta2))
                lista_arestas.append((aresta2, aresta4))
                lista_arestas.append((aresta4, aresta3))
                lista_arestas.append((aresta3, aresta1))

    # Adiciona os polos (norte e sul)
    lista_vertices.append((centro[0], centro[1], centro[2] + raio))
    lista_vertices.append((centro[0], centro[1], centro[2] - raio))

    # Converte as listas de vértices e arestas em arrays numpy
    array_vertices = np.array(lista_vertices)
    array_arestas = np.array(lista_arestas)

    return array_vertices, array_arestas


def esferas(raio, num_esferas=2, num_paralelos=3, num_meridianos=5):
    lista_vertices = []
    lista_arestas = []

    raios_intermediarios = np.linspace(1, raio, num_esferas)

    for r in raios_intermediarios:
        vertices_esfera, arestas_esfera = esfera(r, centro=(0, 0, 0), num_fatias=num_paralelos,
                                                 num_arestas_meridiano=num_meridianos)

        # Ajustar a forma das arrays resultantes da função gerar_esfera
        vertices_esfera = np.array(vertices_esfera)
        arestas_esfera = np.array(arestas_esfera)

        # Adicionar os vértices e ajustar os índices das arestas para a nova esfera
        if len(lista_vertices) > 0:
            arestas_esfera += len(lista_vertices)

        lista_vertices.extend(vertices_esfera)
        lista_arestas.extend(arestas_esfera)

    return np.array(lista_vertices), np.array(lista_arestas)


def toroide(R, r, centro=(0, 0, 0), num_fatias=10, num_arestas_meridiano=10):
    vertices = []  # Lista para armazenar os vértices da malha
    arestas = []  # Lista para armazenar as arestas da malha

    for i in range(num_fatias):
        phi = 2 * math.pi * i / num_fatias
        for j in range(num_arestas_meridiano):
            theta = 2 * math.pi * j / num_arestas_meridiano

            # Coordenadas paramétricas do toroide com raio externo R e raio interno r
            x = (R + r * math.cos(theta)) * math.cos(phi) + centro[0]
            y = (R + r * math.cos(theta)) * math.sin(phi) + centro[1]
            z = r * math.sin(theta) + centro[2]

            vertices.append((x, y, z))  # Adiciona o vértice à lista

            # Conectar com o próximo ponto na mesma fatia (meridiano)
            next_index = (j + 1) % num_arestas_meridiano
            arestas.append((i * num_arestas_meridiano + j, i * num_arestas_meridiano + next_index))

            # Conectar com o ponto na fatia seguinte (latitudinal)
            next_fatia = (i + 1) % num_fatias
            arestas.append((i * num_arestas_meridiano + j, next_fatia * num_arestas_meridiano + j))

    # Converte as listas de vértices e arestas em arrays numpy
    array_vertices = np.array(vertices)
    array_arestas = np.array(arestas)

    return array_vertices, array_arestas


def cilindro(raio, num_circunferencias, num_arestas_base):
    return cilindro_cone_cubo_piramide(raio_base=raio, altura=2 * raio, centro=(0, 0, 0), raio_topo=raio,
                                       num_fatias=num_circunferencias,
                                       num_arestas_base=num_arestas_base)


def cone(raio, num_circunferencias, num_arestas_base):
    return cilindro_cone_cubo_piramide(raio_base=raio, altura=3 * raio, centro=(0, 0, 0), raio_topo=0,
                                       num_fatias=num_circunferencias,
                                       num_arestas_base=num_arestas_base)


def cubo(lado, num_quadrados=2):
    return cilindro_cone_cubo_piramide(raio_base=lado * math.sqrt(2) / 2, altura=lado, centro=(0, 0, 0),
                                       raio_topo=lado * math.sqrt(2) / 2, num_fatias=num_quadrados,
                                       num_arestas_base=4)


def tronco_piramide(lado_menor, lado_maior, altura, num_trapezios=2, num_arestas_base=4):
    return cilindro_cone_cubo_piramide(raio_base=lado_maior * math.sqrt(2) / 2, altura=altura, centro=(0, 0, 0),
                                       raio_topo=lado_menor * math.sqrt(2) / 2, num_fatias=num_trapezios,
                                       num_arestas_base=num_arestas_base)
