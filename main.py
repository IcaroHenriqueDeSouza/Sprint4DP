import heapq


def dijkstra(grafo, inicio, fim):
    fila = [(0, inicio, [])]
    visitados = set()

    while fila:
        custo, no_atual, caminho = heapq.heappop(fila)

        if no_atual in visitados:
            continue

        caminho = caminho + [no_atual]
        visitados.add(no_atual)

        if no_atual == fim:
            return custo, caminho

        for vizinho, peso in grafo[no_atual].items():
            if vizinho not in visitados:
                heapq.heappush(fila, (custo + peso, vizinho, caminho))

    return float("inf"), []


def criar_grafo(peso_negociacao=3):
    return {
        "Lead": {"Qualificação": 2, "Contato": 5},
        "Qualificação": {"Contato": 2},
        "Contato": {
            "Proposta": 4,
            "Negociação": 7  # 🔥 penalizado (antes era 6)
        },
        "Proposta": {"Negociação": 2, "Confirmação": 6},
        "Negociação": {"Confirmação": peso_negociacao},
        "Confirmação": {}
    }


def teste_basico():
    grafo = criar_grafo()

    custo, caminho = dijkstra(grafo, "Lead", "Confirmação")

    assert caminho == [
        "Lead",
        "Qualificação",
        "Contato",
        "Proposta",
        "Negociação",
        "Confirmação"
    ]

    assert custo == 13

    print("Teste básico OK")


def simular_cenarios():
    cenarios = [
        {"nome": "Processo atual", "peso_negociacao": 3},
        {"nome": "Negociação ineficiente", "peso_negociacao": 10},
    ]

    for c in cenarios:
        grafo = criar_grafo(peso_negociacao=c["peso_negociacao"])

        custo, caminho = dijkstra(grafo, "Lead", "Confirmação")

        print(f"\nCenário: {c['nome']}")
        print("Caminho:", " -> ".join(caminho))
        print("Custo:", custo)


if __name__ == "__main__":
    teste_basico()
    simular_cenarios()