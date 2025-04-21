# Questão 1 - Busca por chaves na planta da casa

grafo = {
    'Sala': ['Cozinha', 'Quarto'],
    'Cozinha': ['Banheiro'],
    'Quarto': ['Escritório'],
    'Escritório': ['Chaves'],
    'Banheiro': [],
    'Chaves': []
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

print("Busca em Largura:", busca_largura("Sala", "Chaves"))
print("Busca em Profundidade:", busca_profundidade(["Sala"], "Chaves"))