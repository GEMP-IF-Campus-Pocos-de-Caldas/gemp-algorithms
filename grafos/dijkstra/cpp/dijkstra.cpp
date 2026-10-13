/*
 * Nome: Dijkstra
 * Categoria: grafos
 * Descrição: Caminho mínimo de fonte única em grafo com pesos não-negativos.
 * Complexidade: O((V+E) log V) tempo, O(V) espaço.
 * Autor: GEMP-IF
 * Data: 2026-10-12
 */

#include <limits>
#include <queue>
#include <utility>
#include <vector>

std::vector<int> dijkstra(int n, const std::vector<std::vector<std::pair<int, int>>> &adj,
                          int src) {
    const int inf = std::numeric_limits<int>::max();
    std::vector<int> dist(n, inf);
    using Node = std::pair<int, int>;
    std::priority_queue<Node, std::vector<Node>, std::greater<Node>> queue;
    dist[src] = 0;
    queue.push({0, src});
    while (!queue.empty()) {
        int d = queue.top().first;
        int u = queue.top().second;
        queue.pop();
        if (d > dist[u]) {
            continue;
        }
        for (const auto &edge : adj[u]) {
            int v = edge.first;
            int w = edge.second;
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                queue.push({dist[v], v});
            }
        }
    }
    return dist;
}
