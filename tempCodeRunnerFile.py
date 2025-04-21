# Ex 3 - Métodos: custo uniforme, gulosa e A*

import heapq

grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 3},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

heuristica = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 1,
    'F': 0
}

def custo_uniforme(inicio, objetivo):
    fila = [(0, [inicio])]

    while fila:
        (custo, caminho) = heapq.heappop(fila)
        no = caminho[-1]

        if no == objetivo:
            return caminho, custo

        for vizinho, peso in grafo[no].items():
            heapq.heappush(fila, (custo + peso, caminho + [vizinho]))

def busca_gulosa(inicio, objetivo):
    fila = [(heuristica[inicio], [inicio])]

    while fila:
        (_, caminho) = heapq.heappop(fila)
        no = caminho[-1]

        if no == objetivo:
            return caminho

        for vizinho in grafo[no]:
            heapq.heappush(fila, (heuristica[vizinho], caminho + [vizinho]))

def busca_a_estrela(inicio, objetivo):
    fila = [(heuristica[inicio], 0, [inicio])]

    while fila:
        (f, custo, caminho) = heapq.heappop(fila)
        no = caminho[-1]

        if no == objetivo:
            return caminho, custo

        for vizinho, peso in grafo[no].items():
            g = custo + peso
            f = g + heuristica[vizinho]
            heapq.heappush(fila, (f, g, caminho + [vizinho]))

print("Custo Uniforme:", custo_uniforme("A", "F"))
print("Busca Gulosa:", busca_gulosa("A", "F"))
print("Busca A*:", busca_a_estrela("A", "F"))