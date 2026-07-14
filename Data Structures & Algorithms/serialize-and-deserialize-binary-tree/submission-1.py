# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        nodes = []

        def preorder(node: Optional[TreeNode]) -> None:
            if not node:
                nodes.append("#")
                return
            nodes.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
    
        preorder(root)

        return ",".join(nodes)
                    
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = data.split(",")
        iterator = iter(preorder)

        def build_tree() -> Optional[TreeNode]:
            val = next(iterator)
            if val == "#":
                return None

            root = TreeNode(int(val))
            root.left = build_tree()
            root.right = build_tree()

            return root
        
        return build_tree()