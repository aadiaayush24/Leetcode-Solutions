/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> minHeap = new PriorityQueue<>(
            (a, b) -> Integer.compare(a.val, b.val)
        );
        ListNode head= new ListNode(-1);
        ListNode tail = head;
        for (ListNode node: lists) {
            if(node != null)
            minHeap.offer(node);
        }
        while (!minHeap.isEmpty()) {
            ListNode min=minHeap.poll();
            if (min.next !=null) {
                minHeap.offer(min.next);
            }
            tail.next=min;
            tail=tail.next;
            // tail.next=null;
        }
        return head.next;

    }
}