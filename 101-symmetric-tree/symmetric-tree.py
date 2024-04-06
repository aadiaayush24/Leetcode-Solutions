# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if not (node1 or node2):
                return True
            elif node1 and node2:
                if node1.val == node2.val:
                    return dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
                else:
                    return False
            else:
                return False
        if root:
            if root.left and root.right:
                return dfs(root.left, root.right)
            elif root.left or root.right:
                return False
            else:
                return True
        else:
            return True