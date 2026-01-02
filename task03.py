import heapq
from task01 import create_kyiv_metro_graph


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph.nodes}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]["weight"]
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


if __name__ == "__main__":
    graph = create_kyiv_metro_graph()
    shortest_paths = dijkstra(graph, "Akademmistechko")

    print("Shortest paths from Akademmistechko:")
    for node, distance in shortest_paths.items():
        print(f"{node}: {distance}")
