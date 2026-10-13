/*
 * Nome: Teste Dijkstra
 * Categoria: grafos
 * Descrição: Teste ilustrativo do algoritmo de Dijkstra com um caso conhecido.
 * Complexidade: O((V+E) log V) tempo.
 * Autor: GEMP-IF
 * Data: 2026-10-12
 */

#include <utility>
#include <vector>

#include "dijkstra.cpp"

int main() {
    int n = 5;
    std::vector<std::vector<std::pair<int, int>>> adj(n);
    adj[0].push_back({1, 4});
    adj[0].push_back({2, 1});
    adj[2].push_back({1, 2});
    adj[1].push_back({3, 1});
    adj[2].push_back({3, 5});
    adj[3].push_back({4, 3});

    std::vector<int> expected = {0, 3, 1, 4, 7};
    std::vector<int> got = dijkstra(n, adj, 0);
    if (got != expected) {
        return 1;
    }
    return 0;
}
