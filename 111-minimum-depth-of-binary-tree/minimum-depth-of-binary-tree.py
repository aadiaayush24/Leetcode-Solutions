# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def findDepth(node, depth):
            if node:
                if not (node.left or node.right):
                    return depth + 1
                elif not node.left:
                    return findDepth(node.right, depth+1)
                elif not node.right:
                    return findDepth(node.left, depth+1)
                else:
                    return min(findDepth(node.left, depth+1), findDepth(node.right, depth+1))
            else:
                return depth

        if root:
            return findDepth(root, 0)
        else:
            return 0