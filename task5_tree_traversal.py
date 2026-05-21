import uuid
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key: int, color: str = "#0B3D91") -> None:
        self.left: Node | None = None
        self.right: Node | None = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def generate_colors(count: int) -> list[str]:
    if count <= 1:
        return ["#1296F0"]

    colors = []
    for i in range(count):
        ratio = i / (count - 1)
        r = int(18 + ratio * (180 - 18))
        g = int(60 + ratio * (220 - 60))
        b = int(120 + ratio * (255 - 120))
        colors.append(f"#{r:02X}{g:02X}{b:02X}")
    return colors

def dfs_iterative(root: Node | None) -> list[Node]:
    if root is None:
        return []
    
    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result

def bfs_iterative(root: Node | None) -> list[Node]:
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

def apply_traversal_colors(nodes: list[Node]) -> None:
    colors = generate_colors(len(nodes))
    for node, color in zip(nodes, colors):
        node.color = color

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

def draw_tree(root: Node, title: str) -> None:
    graph = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(graph, root, pos)

    colors = [node[1]["color"] for node in graph.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in graph.nodes(data=True)}

    plt.figure(figsize=(9, 6))
    nx.draw(graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(title)
    plt.show()

def create_sample_tree() -> Node:
    root = Node(0)
    root.left = Node(4)
    root.right = Node(1)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right.left = Node(3)
    root.right.right = Node(8)
    return root

if __name__ == "__main__":
    tree_root = create_sample_tree()

    dfs_order = dfs_iterative(tree_root)
    apply_traversal_colors(dfs_order)
    print("DFS order:", [node.val for node in dfs_order])
    draw_tree(tree_root, "DFS Traversal Visualization")

    tree_root = create_sample_tree()
    bfs_order = bfs_iterative(tree_root)
    apply_traversal_colors(bfs_order)
    print("BFS order:", [node.val for node in bfs_order])
    draw_tree(tree_root, "BFS Traversal Visualization")
