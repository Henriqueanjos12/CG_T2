import objetos as obj
import plot

# Questão 1
objetos={}
vertices, arestas = obj.cilindro(4, 3, 20)
objetos["cilindro"] = (vertices, arestas, 'red')

vertices, arestas = obj.cone(4, 3, 20)
objetos["cone"] = (vertices, arestas, 'green')

vertices, arestas = obj.cubo(5, 2)
objetos["cubo"] = (vertices, arestas, 'blue')

vertices, arestas = obj.tronco_piramide(2, 4, 10, 2, 5)
objetos["piramide"] = (vertices, arestas, 'yellow')

vertices, arestas = obj.esferas(5, 3, 10, 10)
objetos["esfera"] = (vertices, arestas, 'pink')

vertices, arestas = obj.toroide(5, 5, (0, 0, 0), 10, 10)
objetos["toroide"] = (vertices, arestas, 'orange')


for objeto in objetos:
    print(objeto)
    vertices, arestas, cor = objetos[objeto]
    plot.plot_3d(vertices, arestas, 'black', cor)