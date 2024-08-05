# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        def findDiameter(node, diameter):
            if not node:
                return 0
            lHeight = findDiameter(node.left, diameter)
            rHeight = findDiameter(node.right, diameter)

            diameter[0] = max(diameter[0], lHeight + rHeight)
            return 1+max(lHeight, rHeight)
        x = findDiameter(root, diameter)
        return diameter[0]