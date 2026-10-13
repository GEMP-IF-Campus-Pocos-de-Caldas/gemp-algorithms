# Dijkstra

Algoritmo de caminho mínimo de fonte única em grafos com pesos não-negativos.

## Complexidade

- Tempo: `O((V+E) log V)`
- Espaço: `O(V)`

## Arquivos

| Linguagem | Código | Teste |
|---|---|---|
| C++ | `cpp/dijkstra.cpp` | `cpp/test_dijkstra.cpp` |
| Python | `python/dijkstra.py` | `python/test_dijkstra.py` |
| Java | `java/Dijkstra.java` | `java/TestDijkstra.java` |

## Uso

### C++

```cpp
#include "dijkstra.cpp"

std::vector<std::vector<std::pair<int, int>>> adj(n);
std::vector<int> dist = dijkstra(n, adj, src);
```

### Python

```python
from dijkstra import dijkstra

dist = dijkstra(n, adj, src)
```

### Java

```java
int[] dist = Dijkstra.dijkstra(n, adj, src);
```

## Algoritmos

| Algoritmo | Linguagens | Verificação |
|---|---|---|
| dijkstra | C++, Python, Java | automatizada |
