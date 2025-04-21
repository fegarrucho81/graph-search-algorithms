# Questão 2 - Busca no labirinto até o nó M

grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['H'],
    'G': ['M'],
    'H': [],
    'M': []
}

from collections import deque

def busca_largura(inicio, objetivo):
    fila = deque([[inicio]])
    visitados = set()

    while fila:
        caminho = fila.popleft()
        no = caminho[-1]

        if no == objetivo:
            return caminho

        if no not in visitados:
            visitados.add(no)
            for vizinho in grafo[no]:
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)

def busca_profundidade(caminho, objetivo, visitados=set()):
    no = caminho[-1]

    if no == objetivo:
        return caminho

    visitados.add(no)

    for vizinho in grafo[no]:
        if vizinho not in visitados:
            novo_caminho = busca_profundidade(caminho + [vizinho], objetivo, visitados)
            if novo_caminho:
                return novo_caminho

print("Busca em Largura:", busca_largura("A", "M"))
print("Busca em Profundidade:", busca_profundidade(["A"], "M"))