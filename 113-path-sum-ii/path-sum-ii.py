# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def recursive(currNode, currTarget, path):
            if not currNode:
                return
            
            path.append(currNode.val)
            if not (currNode.left or currNode.right) and currTarget- currNode.val == 0:
                res.append(path[:])
            else:
                if currNode.left:
                    recursive(currNode.left, currTarget - currNode.val, path)
                if currNode.right:
                    recursive(currNode.right, currTarget - currNode.val, path)
            path.pop()
            return
        res = []
        recursive(root, targetSum, [])
        return res
            