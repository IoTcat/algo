from lib.utils import measure_time
import time
import random

from collections import deque


class GraphNode:
    def __init__(self, data, adj = None):
        self.val = data
        self.adj = adj or []
        self.visited = False
        self.shortest_path_tree_p = None

    def __repr__(self) -> str:
        return f"GraphNode({self.val} p{self.shortest_path_tree_p and self.shortest_path_tree_p.val} v{self.visited} -> {self.adj})"
    

def dfs(n, p = None):
    if not n or n.visited:
        return
    
    n.visited = True

    if p:
        n.shortest_path_tree_p = p

    for adj in n.adj:
        dfs(adj, n)
    

def bfs(n):
    queue = deque([n])

    n.visited = True

    while queue:
        n = queue.popleft()
        for adj in n.adj:
            if not adj.visited:
                adj.visited = True
                adj.shortest_path_tree_p = n
                queue.append(adj)







def print_graph_vivid(node, visited = None):
    if not node:
        return
    if not visited:
        visited = set()
    if node in visited:
        return
    visited.add(node)
    print(f"{node.val} -> {[n.val for n in node.adj]}")
    for n in node.adj:
        print_graph_vivid(n, visited)




# test
g = GraphNode(1, [GraphNode(2), GraphNode(3)])
print(g)
# Output: GraphNode(1 -> [GraphNode(2 -> []), GraphNode(3 -> [])])
g.adj[0].adj.append(g)
print(g)
# Output: GraphNode(1 -> [GraphNode(2 -> [GraphNode(1 -> [GraphNode(2 -> []), GraphNode(3 -> [])])]), GraphNode(3 -> [])])
g.adj[1].adj.append(g.adj[0])
print(g)
# Output: GraphNode(1 -> [GraphNode(2 -> [GraphNode(1 -> [GraphNode(2 -> [GraphNode(1 -> [GraphNode(2 -> []), GraphNode(3 -> [])])]), GraphNode(3 -> [])]), GraphNode(3 -> [GraphNode(2 -> [GraphNode(1 -> [GraphNode(2 -> []), GraphNode(3 -> [])])])])])

print_graph_vivid(g)


bfs(g)


print(g)
