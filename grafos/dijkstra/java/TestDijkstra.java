/*
 * Nome: Teste Dijkstra
 * Categoria: grafos
 * Descrição: Teste ilustrativo do algoritmo de Dijkstra com um caso conhecido.
 * Complexidade: O((V+E) log V) tempo.
 * Autor: GEMP-IF
 * Data: 2026-10-12
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class TestDijkstra {
  public static void main(String[] args) {
    int n = 5;
    List<List<int[]>> adj = new ArrayList<>();
    for (int i = 0; i < n; i++) {
      adj.add(new ArrayList<>());
    }
    adj.get(0).add(new int[] {1, 4});
    adj.get(0).add(new int[] {2, 1});
    adj.get(2).add(new int[] {1, 2});
    adj.get(1).add(new int[] {3, 1});
    adj.get(2).add(new int[] {3, 5});
    adj.get(3).add(new int[] {4, 3});

    int[] expected = {0, 3, 1, 4, 7};
    int[] got = Dijkstra.dijkstra(n, adj, 0);
    if (!Arrays.equals(got, expected)) {
      System.out.println("FAIL");
      System.exit(1);
    }
  }
}
