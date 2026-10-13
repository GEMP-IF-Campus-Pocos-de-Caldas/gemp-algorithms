# Nome: Dijkstra
# Categoria: grafos
# Descrição: Caminho mínimo de fonte única em grafo com pesos não-negativos.
# Complexidade: O((V+E) log V) tempo, O(V) espaço.
# Autor: GEMP-IF
# Data: 2026-10-12

import heapq


def dijkstra(n, adj, src):
    inf = float("inf")
    dist = [inf] * n
    dist[src] = 0
    heap = [(0, src)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist
