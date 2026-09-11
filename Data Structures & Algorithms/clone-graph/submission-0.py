"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copy = {}

        if not node:
            return

        def clone(node):
            if node in copy:
                return copy[node]

            copiedNode = Node(node.val)
            copy[node] = copiedNode

            for neighbor in node.neighbors:
                copiedNeighbor = clone(neighbor)
                copiedNode.neighbors.append(copiedNeighbor)

            return copiedNode


        return clone(node)