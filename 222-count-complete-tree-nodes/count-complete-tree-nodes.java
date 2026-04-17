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
    public int countNodes(TreeNode root) {
        int left=getLeftMostHeight(root);
        int right=getRightMostHeight(root);

        if (left == right) {
            return (1 << left)-1;
        }
        else {
            return countNodes(root.left)+countNodes(root.right)+1;
        }
    }

    public int getLeftMostHeight(TreeNode node) {
        int count=0;
        while (node != null) {
            count++;
            node=node.left;
        }
        return count;
    }

    public int getRightMostHeight(TreeNode node) {
        int count=0;
        while (node != null) {
            count++;
            node=node.right;
        }
        return count;
    }
}