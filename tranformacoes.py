import math

import numpy as np


def translator(vertices, tx=0, ty=0, tz=0):
    matriz_translator = np.array([[1, 0, 0, tx],
                                  [0, 1, 0, ty],
                                  [0, 0, 1, tz],
                                  [0, 0, 0, 1]])

    # Adiciona as coordenadas homogêneas
    vertices_homogeneous = np.column_stack((vertices, np.ones(len(vertices))))

    # Realiza a multiplicação da matriz de translação
    vertices_transformados_homogeneous = np.dot(vertices_homogeneous, matriz_translator.T)

    # Remove as coordenadas homogêneas
    vertices_transladados = vertices_transformados_homogeneous[:, :3]

    return vertices_transladados


def escala(vertices, tx=0, ty=0, tz=0):
    matriz_escala = np.array([[tx, 0, 0, 0],
                              [0, ty, 0, 0],
                              [0, 0, tz, 0],
                              [0, 0, 0, 1]])

    # Adiciona as coordenadas homogêneas
    vertices_homogeneous = np.column_stack((vertices, np.ones(len(vertices))))

    # Realiza a multiplicação da matriz de translação
    vertices_transformados_homogeneous = np.dot(vertices_homogeneous, matriz_escala.T)

    # Remove as coordenadas homogêneas
    vertices_transformados = vertices_transformados_homogeneous[:, :3]

    return vertices_transformados


def rotacao_x(vertices, angulo):
    matriz_rotacao_x = np.array([
        [1, 0, 0, 0],
        [0, math.cos(angulo), -math.sin(angulo), 0],
        [0, math.sin(angulo), math.cos(angulo), 0],
        [0, 0, 0, 1]])

    # Adiciona as coordenadas homogêneas
    vertices_homogeneous = np.column_stack((vertices, np.ones(len(vertices))))

    # Realiza a multiplicação da matriz de translação
    vertices_transformados_homogeneous = np.dot(vertices_homogeneous, matriz_rotacao_x.T)

    # Remove as coordenadas homogêneas
    vertices_transformados = vertices_transformados_homogeneous[:, :3]

    return vertices_transformados


def rotacao_y(vertices, angulo):
    matriz_rotacao_y = np.array([[math.cos(angulo), 0, math.sin(angulo), 0],
                                 [0, 1, 0, 0],
                                 [-math.sin(angulo), 0, math.cos(angulo), 0],
                                 [0, 0, 0, 1]])

    # Adiciona as coordenadas homogêneas
    vertices_homogeneous = np.column_stack((vertices, np.ones(len(vertices))))

    # Realiza a multiplicação da matriz de translação
    vertices_transformados_homogeneous = np.dot(vertices_homogeneous, matriz_rotacao_y.T)

    # Remove as coordenadas homogêneas
    vertices_transformados = vertices_transformados_homogeneous[:, :3]

    return vertices_transformados


def rotacao_z(vertices, angulo):
    matriz_rotacao_z = np.array([[math.cos(angulo), -math.sin(angulo), 0, 0],
                                 [math.sin(angulo), math.cos(angulo), 0, 0],
                                 [0, 0, 1, 0],
                                 [0, 0, 0, 1]])

    # Adiciona as coordenadas homogêneas
    vertices_homogeneous = np.column_stack((vertices, np.ones(len(vertices))))

    # Realiza a multiplicação da matriz de translação
    vertices_transformados_homogeneous = np.dot(vertices_homogeneous, matriz_rotacao_z.T)

    # Remove as coordenadas homogêneas
    vertices_transformados = vertices_transformados_homogeneous[:, :3]

    return vertices_transformados
