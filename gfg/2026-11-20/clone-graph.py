'''
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
'''
from collections import deque

class Solution:
    def cloneGraph(self, node):
        if node is None:
            return None
        clones = {node: Node(node.val, [])}
        queue = deque([node])
        while queue:
            cur = queue.popleft()
            for nb in cur.neighbors:
                if nb not in clones:
                    clones[nb] = Node(nb.val, [])
                    queue.append(nb)
                clones[cur].neighbors.append(clones[nb])
        return clones[node]
