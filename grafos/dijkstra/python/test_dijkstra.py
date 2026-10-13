# Nome: Teste Dijkstra
# Categoria: grafos
# Descrição: Teste ilustrativo do algoritmo de Dijkstra com um caso conhecido.
# Complexidade: O((V+E) log V) tempo.
# Autor: GEMP-IF
# Data: 2026-10-12

from dijkstra import dijkstra


def test_dijkstra_single_source():
    adj = [[] for _ in range(5)]
    adj[0].append((1, 4))
    adj[0].append((2, 1))
    adj[2].append((1, 2))
    adj[1].append((3, 1))
    adj[2].append((3, 5))
    adj[3].append((4, 3))

    assert dijkstra(5, adj, 0) == [0, 3, 1, 4, 7]
