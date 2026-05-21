import heapq
from typing import Dict, List, Tuple
Graph = Dict[str, List[Tuple[str, int]]]

def dijkstra(graph: Graph, start: str) -> dict[str, float]:
    distances: dict[str, float] = {vertex: float("inf") for vertex in graph}
    distances[start] = 0
    priority_queue: list[tuple[float, str]] = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

if __name__ == "__main__":
    graph: Graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("C", 1), ("D", 5)],
        "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
        "D": [("B", 5), ("C", 8), ("E", 2), ("F", 6)],
        "E": [("C", 10), ("D", 2), ("F", 3)],
        "F": [("D", 6), ("E", 3)],
    }
    start_vertex = "A"
    result = dijkstra(graph, start_vertex)
    print(f"Shortest paths from vertex {start_vertex}:")
    for vertex, distance in result.items():
        print(f"{start_vertex} -> {vertex}: {distance}")
