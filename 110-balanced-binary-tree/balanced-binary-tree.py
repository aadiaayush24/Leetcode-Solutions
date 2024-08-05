# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0
            lSubHeight = check(node.left)
            rSubHeight = check(node.right)

            if abs(lSubHeight - rSubHeight) > 1:
                return -1
            if lSubHeight ==-1 or rSubHeight == -1:
                return -1 
            return 1 + max(lSubHeight, rSubHeight) 
        return check(root) != -1