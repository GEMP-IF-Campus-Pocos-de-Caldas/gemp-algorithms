/*
 * Nome: Dijkstra
 * Categoria: grafos
 * Descrição: Caminho mínimo de fonte única em grafo com pesos não-negativos.
 * Complexidade: O((V+E) log V) tempo, O(V) espaço.
 * Autor: GEMP-IF
 * Data: 2026-10-12
 */

import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

public class Dijkstra {
  public static int[] dijkstra(int n, List<List<int[]>> adj, int src) {
    int inf = Integer.MAX_VALUE;
    int[] dist = new int[n];
    Arrays.fill(dist, inf);
    dist[src] = 0;
    PriorityQueue<int[]> queue = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
    queue.add(new int[] {0, src});
    while (!queue.isEmpty()) {
      int[] top = queue.poll();
      int d = top[0];
      int u = top[1];
      if (d > dist[u]) {
        continue;
      }
      for (int[] edge : adj.get(u)) {
        int v = edge[0];
        int w = edge[1];
        if (dist[u] + w < dist[v]) {
          dist[v] = dist[u] + w;
          queue.add(new int[] {dist[v], v});
        }
      }
    }
    return dist;
  }
}
