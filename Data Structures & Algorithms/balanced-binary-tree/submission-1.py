# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            return 1 + max(get_depth(node.left), get_depth(node.right))

        if not root:
            return True

        if abs(get_depth(root.left) - get_depth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)