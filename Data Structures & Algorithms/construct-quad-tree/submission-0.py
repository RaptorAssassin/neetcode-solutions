"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if all(cell == grid[0][0] for row in grid for cell in row):
            val = (True if grid[0][0] == 1 else False)
            return Node(val, True, None, None, None, None)

        mid = len(grid) // 2
        node = Node(True, False, self.construct([row[:mid] for row in grid[:mid]]), self.construct([row[mid:] for row in grid[:mid]]), self.construct([row[:mid] for row in grid[mid:]]), self.construct([row[mid:] for row in grid[mid:]]))

        return node