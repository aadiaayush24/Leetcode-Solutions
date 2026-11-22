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
    public int sumNumbers(TreeNode root) {
        int[] totalSum = new int[1];
        totalSum[0] = 0;
        int current_sum=0;
        HashSet<TreeNode> visited = new HashSet<TreeNode>();
        visit(root, current_sum, visited, totalSum);
        return totalSum[0];
    }
    public void visit(TreeNode node, int current_sum, HashSet<TreeNode> visited, int[] totalSum) {
        visited.add(node);
        current_sum = current_sum*10 + node.val;
        if ((node.left == null) && (node.right == null)) {
            totalSum[0] += current_sum;
        }
        if ((node.left != null) && (!visited.contains(node.left))) {
            visit(node.left, current_sum, visited, totalSum);
        }
        if ((node.right != null) && (!visited.contains(node.right))) {
            visit(node.right, current_sum, visited, totalSum);
        } 
    }
}