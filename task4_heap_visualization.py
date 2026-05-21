import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key: int, color: str = "skyblue") -> None:
        self.left: Node | None = None
        self.right: Node | None = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def build_heap_tree(heap: list[int], index: int = 0) -> Node | None:
    if index >= len(heap):
        return None

    node = Node(heap[index])
    node.left = build_heap_tree(heap, 2 * index + 1)
    node.right = build_heap_tree(heap, 2 * index + 2)
    return node

def add_edges(graph: nx.DiGraph, node: Node | None, pos: dict, x: float = 0, y: float = 0, layer: int = 1) -> nx.DiGraph:
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)

        if node.left:
            graph.add_edge(node.id, node.left.id)
            left_x = x - 1 / 2**layer
            pos[node.left.id] = (left_x, y - 1)
            add_edges(graph, node.left, pos, x=left_x, y=y - 1, layer=layer + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            right_x = x + 1 / 2**layer
            pos[node.right.id] = (right_x, y - 1)
            add_edges(graph, node.right, pos, x=right_x, y=y - 1, layer=layer + 1)

    return graph

def draw_tree(tree_root: Node | None) -> None:
    if tree_root is None:
        print("Heap is empty.")
        return

    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)
    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}
    plt.figure(figsize=(9, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title("Binary Heap Visualization")
    plt.show()

def visualize_heap(values: list[int]) -> None:
    heap = values[:]
    heapq.heapify(heap)
    print("Min-heap array:", heap)
    root = build_heap_tree(heap)
    draw_tree(root)

if __name__ == "__main__":
    visualize_heap([10, 4, 7, 1, 3, 8, 5, 2])
