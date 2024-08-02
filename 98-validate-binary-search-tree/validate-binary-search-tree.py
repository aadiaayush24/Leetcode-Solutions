# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recursion(node, lower = float('-inf'), upper= float('inf')):
            if not node:
                return True
            elif node.val <= lower or node.val >= upper:
                return False
            return recursion(node.left, lower, node.val) and recursion(node.right, node.val, upper)
        return recursion(root)
            