from collections import deque
from task01 import create_kyiv_metro_graph


def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(
                neighbor for neighbor in graph.neighbors(vertex)
                if neighbor not in visited
            )

    return visited


if __name__ == "__main__":
    graph = create_kyiv_metro_graph()

    print("DFS path:")
    print(dfs(graph, "Akademmistechko"))

    print("BFS path:")
    print(bfs(graph, "Akademmistechko"))
