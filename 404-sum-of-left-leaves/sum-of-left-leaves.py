# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sumL = 0
        def recursive(root, isLeft= False):
            if not (root.left or root.right) and isLeft: self.sumL += root.val
            if root.left: recursive(root.left, True)
            if root.right: recursive(root.right, False)
            return
        recursive(root)
        return self.sumL
        