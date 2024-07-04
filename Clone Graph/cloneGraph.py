from typing import Optional
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        nodesToClear, cloneNodes = deque([node]), {node.val: Node(node.val, [] )}
        while nodesToClear:
            originalCurrentNode = nodesToClear.popleft()
            currentClonedNode = cloneNodes[originalCurrentNode.val]
            for neighbor in originalCurrentNode.neighbors:
                if neighbor.val not in cloneNodes:
                    cloneNodes[neighbor.val] = Node(neighbor.val, [])
                    nodesToClear.append(neighbor)
                currentClonedNode.neighbors.append(cloneNodes[neighbor.val])
        return cloneNodes[node.val] 