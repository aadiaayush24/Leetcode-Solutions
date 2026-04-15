/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    public List<TreeNode> generateTrees(int n) {
    List<TreeNode>[][] memo = new ArrayList[n+2][n+2];   

    if (n==0) {
        return new ArrayList<>();
    }
    return buildTrees(1, n, memo);
    }

    public List<TreeNode> buildTrees(int start, int end, List<TreeNode>[][] memo) {
         if (start>end) {
            memo[start][end] = new ArrayList<>();
            memo[start][end].add(null);
            return memo[start][end];
        }
        else if (memo[start][end] != null) {
            return memo[start][end];
        }
        else {
            memo[start][end] = new ArrayList<>();
            for (int root=start; root<=end; root++) {
                List<TreeNode> leftTrees = buildTrees(start, root-1, memo);
                List<TreeNode> rightTrees = buildTrees(root+1, end, memo);
                
                for (TreeNode leftTree: leftTrees) {
                    for (TreeNode rightTree: rightTrees) {
                        TreeNode node = new TreeNode(root);
                        node.left=leftTree;
                        node.right=rightTree;
                        memo[start][end].add(node);
                    }
                }
            }
            return memo[start][end];
        }
    }
}