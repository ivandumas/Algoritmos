import sys
import collections

def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    start = 2
    graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
    metro = {
        "El Rosario" :  ["Instituto del Petroleo", "Tacuba"],
        "Instituto del Petroleo" :  ["El Rosario", "La Raza", "Deportivo 18 de Marzo"],
        "Tacuba" :  ["La Raza", "Deportivo 18 de Marzo"],
        "La Raza" :  ["El Rosario", "Deportivo 18 de Marzo"],
        "Deportivo 18 de Marzo" :  ["El Rosario", "La Raza"]
    }
    print(f"Following is Breadth First Traversal: (starting from {start})")
    bfs(metro, "El Rosario")
    print()