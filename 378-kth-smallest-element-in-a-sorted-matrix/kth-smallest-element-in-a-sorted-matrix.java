public class Node {
    int row, col, val;
    Node(int val, int row, int col) {
        this.val=val;
        this.row=row;
        this.col=col;
    }
}
class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        PriorityQueue<Node> minHeap = new PriorityQueue<>(
            (a, b) -> Integer.compare(a.val, b.val)
        );
        for (int i=0; i<matrix.length; i++) {
            Node firstOfRow = new Node(matrix[i][0], i, 0);
            minHeap.offer(firstOfRow);
        }
        for (int j=1; j<k; j++) {
            Node top = minHeap.poll();
            if (top.col < matrix[0].length-1) {
                int r=top.row;
                int c=top.col+1;
                minHeap.offer(new Node(matrix[r][c], r, c));
            }
        }
        return minHeap.poll().val;
    }
}