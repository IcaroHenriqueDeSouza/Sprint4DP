from main import dijkstra
from main import dijkstra


def teste_basico():
    grafo = {
        "Lead": {"Qualificação": 2, "Contato": 5},
        "Qualificação": {"Contato": 2},
        "Contato": {"Proposta": 4, "Negociação": 7},
        "Proposta": {"Negociação": 2, "Confirmação": 6},
        "Negociação": {"Confirmação": 3},
        "Confirmação": {}
    }

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


def teste_caminho_alternativo():
    grafo = {
        "Lead": {"A": 1, "B": 2},
        "A": {"Confirmação": 100},
        "B": {"Confirmação": 3},
        "Confirmação": {}
    }

    custo, caminho = dijkstra(grafo, "Lead", "Confirmação")

    assert caminho == ["Lead", "B", "Confirmação"]
    assert custo == 5

    print("Teste de decisão OK")


def teste_sem_caminho():
    grafo = {
        "Lead": {"Qualificação": 2},
        "Qualificação": {},
        "Confirmação": {}
    }

    custo, caminho = dijkstra(grafo, "Lead", "Confirmação")

    assert custo == float("inf")
    assert caminho == []

    print("Teste sem caminho OK")


def teste_com_ciclo():
    grafo = {
        "Lead": {"A": 1},
        "A": {"B": 2},
        "B": {"A": 2, "Confirmação": 3},
        "Confirmação": {}
    }

    custo, caminho = dijkstra(grafo, "Lead", "Confirmação")

    assert caminho == ["Lead", "A", "B", "Confirmação"]
    assert custo == 6

    print("Teste com ciclo OK")


def simular_cenarios():
    cenarios = [
        {"nome": "Processo atual", "peso_negociacao": 3},
        {"nome": "Negociação ineficiente", "peso_negociacao": 10},
    ]

    for c in cenarios:
        grafo = {
            "Lead": {"Qualificação": 2, "Contato": 5},
            "Qualificação": {"Contato": 2},
            "Contato": {"Proposta": 4, "Negociação": 7},
            "Proposta": {"Negociação": 2, "Confirmação": 6},
            "Negociação": {"Confirmação": c["peso_negociacao"]},
            "Confirmação": {}
        }

        custo, caminho = dijkstra(grafo, "Lead", "Confirmação")

        print(f"\nCenário: {c['nome']}")
        print("Caminho:", " -> ".join(caminho))
        print("Custo:", custo)


if __name__ == "__main__":
    teste_basico()
    teste_caminho_alternativo()
    teste_sem_caminho()
    teste_com_ciclo()
    simular_cenarios()